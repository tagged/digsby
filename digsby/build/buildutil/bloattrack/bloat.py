#!/usr/bin/python

import fileinput
import optparse
import os
import pprint
import re
import sys
import json

def format_bytes(bytes):
    """Pretty-print a number of bytes."""
    if bytes > 1e6:
        bytes = bytes / 1.0e6
        return '%.1fm' % bytes
    if bytes > 1e3:
        bytes = bytes / 1.0e3
        return '%.1fk' % bytes
    return str(bytes)


def symbol_type_to_human(type):
    """Convert a symbol type as printed by nm into a human-readable name."""
    return {
        'b': 'bss',
        'd': 'data',
        'r': 'read-only data',
        't': 'code',
        'w': 'weak symbol',
        'v': 'weak symbol'
        }[type]


def parse_nm(input):
    """Parse nm output.

    Argument: an iterable over lines of nm output.

    Yields: (symbol name, symbol type, symbol size, source file path).
    Path may be None if nm couldn't figure out the source file.
    """

    # Match lines with size + symbol + optional filename.
    sym_re = re.compile(r'^[0-9a-f]+ ([0-9a-f]+) (.) ([^\t]+)(?:\t(.*):\d+)?$')

    # Match lines with addr but no size.
    addr_re = re.compile(r'^[0-9a-f]+ (.) ([^\t]+)(?:\t.*)?$')
    # Match lines that don't have an address at all -- typically external symbols.
    noaddr_re = re.compile(r'^ + (.) (.*)$')

    for line in input:
        line = line.rstrip()
        match = sym_re.match(line)
        if match:
            size, type, sym = match.groups()[0:3]
            size = int(size, 16)
            type = type.lower()
            if type == 'v':
                type = 'w'  # just call them all weak
            if type == 'b':
                continue  # skip all BSS for now
            path = match.group(4)
            yield sym, type, size, path
            continue
        match = addr_re.match(line)
        if match:
            type, sym = match.groups()[0:2]
            # No size == we don't care.
            continue
        match = noaddr_re.match(line)
        if match:
            type, sym = match.groups()
            if type in ('U', 'w'):
                # external or weak symbol
                continue

        print >>sys.stderr, 'unparsed:', repr(line)


def filter_syms(types, symbols):
    for sym, type, size, path in symbols:
        if type in types:
            yield sym, type, size, path


def treeify_syms(symbols, strip_prefix=None):
    dirs = {}
    for sym, type, size, path in symbols:
        if path:
            path = os.path.normpath(path)
            if strip_prefix and path.startswith(strip_prefix):
                path = path[len(strip_prefix):]
            elif path.startswith('/usr/include'):
                path = path.replace('/usr/include', 'usrinclude')
            elif path.startswith('/'):
                path = path[1:]

        parts = None
        # TODO: make segmenting by namespace work.
        if False and '::' in sym:
            if sym.startswith('vtable for '):
                sym = sym[len('vtable for '):]
                parts = sym.split('::')
                parts.append('[vtable]')
            else:
                parts = sym.split('::')
            parts[0] = '::' + parts[0]
        elif path and os.sep in path:
            parts = path.split(os.sep)

        if parts:
            key = parts.pop()
            tree = dirs
            try:
                for part in parts:
                    assert part != '', path
                    if part not in tree:
                        tree[part] = {}
                    tree = tree[part]
                tree[key] = tree.get(key, 0) + size
            except:
                print >>sys.stderr, sym, parts, key
                raise
        else:
            key = 'symbols without paths'
            if key not in dirs:
                dirs[key] = {}
            tree = dirs[key]
            subkey = 'misc'
            if (sym.endswith('::__FUNCTION__') or
                sym.endswith('::__PRETTY_FUNCTION__')):
                subkey = '__FUNCTION__'
            elif sym.startswith('CSWTCH.'):
                subkey = 'CSWTCH'
            elif '::' in sym:
                subkey = sym[0:sym.find('::') + 2]
            else:
                print >>sys.stderr, 'unbucketed (no path?):', sym, type, size, path
            tree[subkey] = tree.get(subkey, 0) + size
    return dirs


def jsonify_tree(tree, name):
    children = []
    total = 0
    files = 0

    for key, val in tree.iteritems():
        if isinstance(val, dict):
            subtree = jsonify_tree(val, key)
            total += subtree['data']['$area']
            children.append(subtree)
        else:
            total += val
            children.append({
                    'name': key + ' ' + format_bytes(val),
                    'data': { '$area': val }
                    })

    children.sort(key=lambda child: -child['data']['$area'])

    return {
        'name': name + ' ' + format_bytes(total),
        'data': {
            '$area': total,
            },
        'children': children,
        }


def dump_nm(nmfile, strip_prefix):
    dirs = treeify_syms(parse_nm(nmfile), strip_prefix)
    print 'var kTree = ' + json.dumps(jsonify_tree(dirs, '/'), indent=2)


def parse_objdump(input):
    """Parse objdump -h output."""
    sec_re = re.compile('^\d+ (\S+) +([0-9a-z]+)')
    sections = []
    debug_sections = []

    for line in input:
        line = line.strip()
        match = sec_re.match(line)
        if match:
            name, size = match.groups()
            if name.startswith('.'):
                name = name[1:]
            if name.startswith('debug_'):
                name = name[len('debug_'):]
                debug_sections.append((name, int(size, 16)))
            else:
                sections.append((name, int(size, 16)))
            continue
    return sections, debug_sections


def jsonify_sections(name, sections):
    children = []
    total = 0
    for section, size in sections:
        children.append({
                'name': section + ' ' + format_bytes(size),
                'data': { '$area': size }
                })
        total += size

    children.sort(key=lambda child: -child['data']['$area'])

    return {
        'name': name + ' ' + format_bytes(total),
        'data': { '$area': total },
        'children': children
        }


def dump_sections():
    sections, debug_sections = parse_objdump(open('objdump.out'))
    sections = jsonify_sections('sections', sections)
    debug_sections = jsonify_sections('debug', debug_sections)
    print 'var kTree = ' + json.dumps({
            'name': 'top',
            'data': { '$area': sections['data']['$area'] +
                               debug_sections['data']['$area'] },
            'children': [ debug_sections, sections ]})


usage="""%prog [options] MODE

Modes are:
  syms: output symbols json suitable for a treemap
  dump: print symbols sorted by size (pipe to head for best output)
  sections: output binary sections json suitable for a treemap

nm output passed to --nm-output should from running a command
like the following (note, can take a long time -- 30 minutes):
  nm -C -S -l /path/to/binary > nm.out

objdump output passed to --objdump-output should be from a command
like:
  objdump -h /path/to/binary > objdump.out"""

def main():
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('--nm-output', action='store', dest='nmpath',
                      metavar='PATH', default='nm.out',
                      help='path to nm output [default=nm.out]')
    parser.add_option('--objdump-output', action='store', dest='objdump',
                      metavar='PATH', default='objdump.out',
                      help='path to objdump output [default=objdump.out]')
    parser.add_option('--strip-prefix', metavar='PATH', action='store',
                      help='strip PATH prefix from paths; e.g. /path/to/src/root')
    parser.add_option('--filter', action='store',
                      help='include only symbols/files matching FILTER')
    opts, args = parser.parse_args()

    if len(args) != 1:
        parser.print_usage()
        sys.exit(1)

    mode = args[0]
    if mode == 'syms':
        nmfile = open(opts.nmpath, 'r')
        dump_nm(nmfile, strip_prefix=opts.strip_prefix)
    elif mode == 'sections':
        dump_sections()
    elif mode == 'dump':
        nmfile = open(opts.nmpath, 'r')
        syms = list(parse_nm(nmfile))
        # a list of (sym, type, size, path); sort by size.
        syms.sort(key=lambda x: -x[2])
        total = 0
        for sym, type, size, path in syms:
            if type in ('b', 'w'):
                continue  # skip bss and weak symbols
            if path is None:
                path = ''
            if opts.filter and not (opts.filter in sym or opts.filter in path):
                continue
            print '%6s %s (%s) %s' % (format_bytes(size), sym,
                                      symbol_type_to_human(type), path)
            total += size
        print '%6s %s' % (format_bytes(total), 'total'),
    else:
        print 'unknown mode'
        parser.print_usage()

if __name__ == '__main__':
    main()
