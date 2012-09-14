ABM_NEW = 0x00000000
ABM_REMOVE = 0x00000001
ABM_QUERYPOS = 0x00000002
ABM_SETPOS = 0x00000003
ABM_GETSTATE = 0x00000004
ABM_GETTASKBARPOS = 0x00000005
ABM_ACTIVATE = 0x00000006
ABM_GETAUTOHIDEBAR = 0x00000007
ABM_SETAUTOHIDEBAR = 0x00000008
ABM_WINDOWPOSCHANGED = 0x0000009
ABN_STATECHANGE = 0x0000000
ABN_POSCHANGED = 0x0000001
ABN_FULLSCREENAPP = 0x0000002
ABN_WINDOWARRANGE = 0x0000003
ABS_AUTOHIDE = 0x0000001
ABS_ALWAYSONTOP = 0x0000002

AW_HOR_POSITIVE = 0x00000001
AW_HOR_NEGATIVE = 0x00000002
AW_VER_POSITIVE = 0x00000004
AW_VER_NEGATIVE = 0x00000008
AW_CENTER = 0x00000010
AW_HIDE = 0x00010000
AW_ACTIVATE = 0x00020000
AW_SLIDE = 0x00040000
AW_BLEND = 0x00080000
WS_EX_LAYERED = 0x00080000

SW_HIDE = 0
SW_SHOWNORMAL = 1
SW_NORMAL = 1
SW_SHOWMINIMIZED = 2
SW_SHOWMAXIMIZED = 3
SW_MAXIMIZE = 3
SW_SHOWNOACTIVATE = 4
SW_SHOW = 5
SW_MINIMIZE = 6
SW_SHOWMINNOACTIVE = 7
SW_SHOWNA = 8
SW_RESTORE = 9
SW_SHOWDEFAULT = 10
SW_MAX = 10

ABE_LEFT = 0
ABE_TOP = 1
ABE_RIGHT = 2
ABE_BOTTOM = 3

sideStrings = {0:'left', 1:'top', 2:'right', 3:'bottom'}

HWND_TOP = 0
HWND_BOTTOM = 1
HWND_TOPMOST = -1
HWND_NOTOPMOST = -2
SWP_NOSIZE          = 0x0001
SWP_NOMOVE          = 0x0002
SWP_NOZORDER        = 0x0004
SWP_NOREDRAW        = 0x0008
SWP_NOACTIVATE      = 0x0010
SWP_FRAMECHANGED    = 0x0020
SWP_SHOWWINDOW      = 0x0040
SWP_HIDEWINDOW      = 0x0080
SWP_NOCOPYBITS      = 0x0100
SWP_NOOWNERZORDER   = 0x0200
SWP_NOSENDCHANGING  = 0x0400
SWP_DRAWFRAME       = 0x0020
SWP_NOREPOSITION    = 0x0200
SWP_DEFERERASE      = 0x2000
SWP_ASYNCWINDOWPOS  = 0x4000

WS_EX_APPWINDOW = 0x40000
WS_EX_TOOLWINDOW = 0x80

# Windows message constants
GWL_WNDPROC = -4
GWL_STYLE = -16
GWL_EXSTYLE = -20
WM_SIZING = 0x214
WM_MOVING = 0x216
WM_ENTERSIZEMOVE = 0x231
WM_EXITSIZEMOVE = 0x232
WM_NCHITTEST = 0x084
WM_WINDOWPOSCHANGING = 0x046
WM_USER = 0x0400

WM_SYSCOMMAND = 0x0112
SC_MAXIMIZE = 0xF030
SC_MINIMIZE = 0xF020
SC_ZOOM = 61488

# hittest contants
HTNOWHERE = 0
HTCLIENT = 1
HTCAPTION = 2
HTSYSMENU = 3
HTGROWBOX = 4
HTSIZE = HTGROWBOX
HTMENU = 5
HTHSCROLL = 6
HTVSCROLL = 7
HTMINBUTTON = 8
HTMAXBUTTON = 9
HTLEFT = 10
HTRIGHT = 11
HTTOP = 12
HTTOPLEFT = 13
HTTOPRIGHT = 14
HTBOTTOM = 15
HTBOTTOMLEFT = 16
HTBOTTOMRIGHT = 17
HTBORDER = 18
HTREDUCE = HTMINBUTTON
HTZOOM = HTMAXBUTTON

WMSZ_LEFT = 1
WMSZ_RIGHT = 2
WMSZ_TOP = 3
WMSZ_TOPLEFT = 4
WMSZ_TOPRIGHT = 5
WMSZ_BOTTOM = 6
WMSZ_BOTTOMLEFT = 7
WMSZ_BOTTOMRIGHT = 8
