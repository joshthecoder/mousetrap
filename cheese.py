"""
Platform independent module
for controlling the mouse and keyboard
"""
import sys

class Mouse:

    LEFT_BUTTON = 1
    MIDDLE_BUTTON = 2
    RIGHT_BUTTON = 3

    def move(self, x, y):
        """Move mouse pointer to specified location"""
        raise NotImplementedError

    def press(self, button):
        """Trigger mouse press of the specified button"""
        raise NotImplementedError

    def release(self, button):
        """Trigger mouse release of the specified button"""
        raise NotImplementedError

class X11Mouse(Mouse):

    def __init__(self):
        self.display = Xlib.display.Display()
        self.screen = self.display.screen()

    def move(self, x, y):
        self.screen.root.warp_pointer(x, y)
        self.display.sync()

    def press(self, button):
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonPress, button)
        self.display.sync()

    def release(self, button):
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonRelease, button)
        self.display.sync()

class Win32Mouse(Mouse):

    def move(self, x, y):
        # TODO: implement
        return

    def press(self, button):
        # TODO: implement
        return

    def release(self, button):
        # TODO: implement
        return

class Keyboard:

    def press(self, key):
        """Trigger key press"""
        raise NotImplementedError

    def release(self, key):
        """Trigger key release"""
        raise NotImplementedError

class X11Keyboard(Keyboard):

    js_to_x11_keycode = {
        8:22, 9:23, 13:36, 16:50, 17:37, 18:64, 19:127, 20:66, 27:9, 32:65, 33:112,
        34:117, 35:115, 36:110, 37:113, 38:111, 39:114, 40:116, 45:118, 46:119,
        48:19, 49:10, 50:11, 51:12, 52:13, 53:14, 54:15, 55:16, 56:17, 57:18,
        65:38, 66:56, 67:54, 68:40, 69:26, 70:41, 71:42, 72:43, 73:31, 74:44,
        75:45, 76:46, 77:58, 78:57, 79:32, 80:33, 81:24, 82:27, 83:39, 84:28,
        85:30, 86:55, 87:25, 88:53, 89:29, 90:52, 96:90, 97:87, 98:88, 99:89,
        100:83, 101:84, 102:85, 103:79, 104:80, 105:81, 106:63, 107:86,
        109:82, 110:91, 111:106, 112:67, 113:68, 114:69, 115:70, 116:71, 117:72,
        118:73, 119:74, 120:75, 121:76, 122:95, 123:96, 144:77, 145:78, 186:47,
        187:21, 188:59, 189:20, 190:60, 191:61, 192:49, 219:34, 220:51,
        221:35, 222:48
    }

    def __init__(self):
        self.display = Xlib.display.Display()

    def _lookup_keycode(self, js_keycode):
        try:
            return self.js_to_x11_keycode[js_keycode]
        except:
            raise RuntimeError('Invalid keycode: %s' % js_keycode)

    def press(self, js_keycode):
        x11_keycode = self._lookup_keycode(js_keycode)
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.KeyPress, x11_keycode)
        self.display.sync()

    def release(self, js_keycode):
        x11_keycode = self._lookup_keycode(js_keycode)
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.KeyRelease, x11_keycode)
        self.display.sync()

class Win32Keyboard(Keyboard):

    def press(self, key):
        return

    def release(self, key):
        return

if sys.platform == 'linux2':
    import Xlib.display
    import Xlib.X
    import Xlib.ext.xtest
    mouse = X11Mouse()
    keyboard = X11Keyboard()
elif sys.platform == 'win32':
    import win32api
    mouse = Win32Mouse()
    keyboard = Win32Keyboard()
else:
    raise ImportError("Unsupported platform")

