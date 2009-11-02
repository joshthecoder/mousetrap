"""
Platform independent module
for controlling the mouse and keyboard
"""
import sys

class Mouse:

    LEFT_BUTTON = 0
    MIDDLE_BUTTON = 1
    RIGHT_BUTTON = 2

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

    def move(self, x, y):
        # TODO: implement
        return

    def press(self, button):
        # TODO: implement
        return

    def release(self, button):
        # TODO: implement
         return

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
    import Xlib
    mouse = X11Mouse()
elif sys.platform == 'win32':
    import win32api
    mouse = Win32Mouse()
else:
    raise ImportError("Unsupported platform")

