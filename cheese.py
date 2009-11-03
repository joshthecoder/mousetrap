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

if sys.platform == 'linux2':
    import Xlib.display
    import Xlib.X
    import Xlib.ext.xtest
    mouse = X11Mouse()
elif sys.platform == 'win32':
    import win32api
    mouse = Win32Mouse()
else:
    raise ImportError("Unsupported platform")

