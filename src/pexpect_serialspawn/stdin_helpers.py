#!/usr/bin/env python
# Helper functions for reading single characters from stdin across platforms.

import sys
import os

if os.name == 'nt':  # Windows
    import msvcrt

    def read_char():
        return msvcrt.getch()

else:  # POSIX (Linux, macOS)
    import tty
    import termios

    def read_char():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
