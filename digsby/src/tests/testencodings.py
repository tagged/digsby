import util.auxencodings
from timeit import Timer

def main():
    print Timer("assert s.encode('xml').decode('xml') == s",
                'from __main__ import s').timeit(50)


s = '''<html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8"><title>Google</title><style>body,td,a,p,.h{font-family:arial,sans-serif}.h{font-size:20px}.h{color:#3366cc}.q{color:#00c}.ts td{padding:0}.ts{border-collapse:collapse}#gbar{float:left;font-weight:bold;height:22px;padding-left:2px}#gbh{border-top:1px solid #c9d7f1;font-size:0;height:0;position:absolute;right:0;top:24px;width:200%}#gbi{background:#fff;border:1px solid;border-color:#c9d7f1 #36c #36c #a2bae7;font-size:13px;top:24px;z-index:1000}#guser{padding-bottom:7px !important}#gbar,#guser{font-size:13px;padding-top:1px !important}@media all{.gb1,.gb3{height:22px;margin-right:.73em;vertical-align:top}}#gbi,.gb2{display:none;position:absolute;width:8em}.gb2{z-index:1001}#gbar a,#gbar a:active,#gbar a:visited{color:#00c;font-weight:normal}.gb2 a,.gb3 a{text-decoration:none}.gb2 a{display:block;padding:.2em .5em}#gbar .gb2 a:hover{background:#36c;color:#fff}</style><script>window.google={kEI:"9ayDR7uNOYmMeZGfwVE",kEXPI:"17259,17735",kHL:"en"};
function sf(){document.f.q.focus()}
window.rwt=function(b,d,e,g,h,f,i){var a=encodeURIComponent||escape,c=b.href.split("#");b.href="/url?sa=t"+(d?"&oi="+a(d):"")+(e?"&cad="+a(e):"")+"&ct="+a(g)+"&cd="+a(h)+"&url="+a(c[0]).replace(/\+/g,"%2B")+"&ei=9ayDR7uNOYmMeZGfwVE"+(f?"&usg="+f:"")+i+(c[1]?"#"+c[1]:"");b.onmousedown="";return true};
window.gbar={};(function(){;var g=window.gbar,a,l,d;function m(b,f,e){b.display=b.display=="block"?"none":"block";b.left=f+"px";b.top=e+"px"}g.tg=function(b){var f=0,e,c,h,i=0,j=window.navExtra;!l&&(l=document.getElementById("gbar"));!d&&(d=l.getElementsByTagName("span"));(b||window.event).cancelBubble=true;if(!a){a=document.createElement(Array.every||window.createPopup?"iframe":"div");a.frameBorder="0";a.id="gbi";a.scrolling="no";a.src="#";document.body.appendChild(a);if(j&&d[8])for(var n in j){var k=document.createElement("span");k.appendChild(j[n]);k.className="gb2";d[0].parentNode.insertBefore(k,d[8])}document.onclick=g.close}for(;d[i];i++){c=d[i];h=c.className;if(h=="gb3"){e=c.offsetLeft;while(c=c.offsetParent)e+=c.offsetLeft;m(a.style,e,24)}else if(h=="gb2"){m(c.style,e+1,25+f);f+=20}}a.style.height=f+"px"};g.close=function(b){a&&a.style.display=="block"&&g.tg(b)};})();</script></head><body bgcolor=#ffffff text=#000000 link=#0000cc vlink=#551a8b alink=#ff0000 onload="sf();if(document.images){new Image().src='/images/nav_logo3.png'}" topmargin=3 marginheight=3><div id=gbar><nobr><span class=gb1>Web</a></span> <span class=gb1><a href="http://images.google.com/imghp?hl=en&tab=wi">Images</a></span> <span class=gb1><a href="http://maps.google.com/maps?hl=en&tab=wl">Maps</a></span> <span class=gb1><a href="http://news.google.com/nwshp?hl=en&tab=wn">News</a></span> <span class=gb1><a href="http://www.google.com/prdhp?hl=en&tab=wf">Shopping</a></span> <span class=gb1><a href="http://mail.google.com/mail?hl=en&tab=wm">Gmail</a></span> <span class=gb3><a href="http://www.google.com/intl/en/options/" onclick="this.blur();gbar.tg(event);return false"><u>more</u> <span style=font-size:11px>&#9660;</span></a></span> <span class=gb2><a href="http://blogsearch.google.com/?hl=en&tab=wb">Blogs</a></span> <span class=gb2><a href="http://books.google.com/bkshp?hl=en&tab=wp">Books</a></span> <span class=gb2><a href="http://www.google.com/calendar?hl=en&tab=wc">Calendar</a></span> <span class=gb2><a href="http://docs.google.com/?hl=en&tab=wo">Documents</a></span> <span class=gb2><a href="http://finance.google.com/finance?hl=en&tab=we">Finance</a></span> <span class=gb2><a href="http://groups.google.com/grphp?hl=en&tab=wg">Groups</a></span> <span class=gb2><a href="http://picasaweb.google.com/home?hl=en&tab=wq">Photos</a></span> <span class=gb2><a href="http://www.google.com/reader?hl=en&tab=wy">Reader</a></span> <span class=gb2><a href="http://scholar.google.com/schhp?hl=en&tab=ws">Scholar</a></span> <span class=gb2><a href="http://video.google.com/?hl=en&tab=wv">Video</a></span> <span class=gb2><a href="http://www.youtube.com/?hl=en&tab=w1">YouTube</a></span> <span class=gb2><a href="http://www.google.com/intl/en/options/">even more &raquo;</a></span> </nobr></div><div id=gbh></div><div align=right id=guser style="font-size:84%;padding:0 0 4px" width=100%><nobr><b>kevinwatters@gmail.com</b> | <a href="/url?sa=p&pref=ig&pval=3&q=http://www.google.com/ig%3Fhl%3Den&usg=AFQjCNEj49wK5T88bDwGcaZsW52jiYwJwg">iGoogle</a> | <a href="https://www.google.com/accounts/ManageAccount">My Account</a> | <a href="http://www.google.com/accounts/Logout?continue=http://www.google.com/">Sign out</a></nobr></div><center><br clear=all id=lgpd><img alt="Google" height=110 src="/intl/en_ALL/images/logo.gif" width=276><br><br><form action="/search" name=f><table cellpadding=0 cellspacing=0><tr valign=top><td width=25%>&nbsp;</td><td align=center nowrap><input name=hl type=hidden value=en><input maxlength=2048 name=q size=55 title="Google Search" value=""><br><input name=btnG type=submit value="Google Search"><input name=btnI type=submit value="I'm Feeling Lucky"></td><td nowrap width=25%><font size=-2>&nbsp;&nbsp;<a href=/advanced_search?hl=en>Advanced Search</a><br>&nbsp;&nbsp;<a href=/preferences?hl=en>Preferences</a><br>&nbsp;&nbsp;<a href=/language_tools?hl=en>Language Tools</a></font></td></tr></table></form><br><br><font size=-1><a href="/intl/en/ads/">Advertising&nbsp;Programs</a> - <a href="/services/">Business Solutions</a> - <a href="/intl/en/about.html">About Google</a></font><p><font size=-2>&copy;2008 Google</font></p></center></body></html>
'''

if __name__ == '__main__':
    print len(s)
    main()