#!/usr/bin/env python2

"""
Draw Line.py

Drawing on a Textview Window.

Draw a static red horizontal line.
"""

import gtk
import os

ICON_IMAGE = os.path.join('gtk-logo.svg')
TEXT = __doc__


class Draw0Demo(gtk.Window):
    def __init__(self, parent=None):
        gtk.Window.__init__(self)
        try:
            self.set_screen(parent.get_screen())
        except AttributeError:
            self.connect('destroy', lambda *w: gtk.main_quit())
        self.set_title(self.__class__.__name__)
        self.set_default_size(450, 450)
        self.set_border_width(10)
        self.set_icon_from_file(ICON_IMAGE)
        tv = gtk.TextView()
        buf = tv.get_buffer()
        buf.set_text(TEXT)
        tv.set_wrap_mode(gtk.WRAP_WORD)
        sw = gtk.ScrolledWindow()
        sw.set_policy(1, 1)
        self.add(sw)
        sw.add(tv)
        tv.connect("expose-event", self.expose)
        self.show_all()

    def expose(self, widget, event):
        # Part 1

        # Getting Line 4's y-value
        buf = widget.get_buffer()
        text_iter = buf.get_iter_at_line(4)
        iter_rect = widget.get_iter_location(text_iter)
        # iter_rect is a gtk.gdk.Rectangle(0, 76, 0, 19)
        # x, y, width, height
        print iter_rect
        y = iter_rect[1]
        print y

        # Part 2
        win = widget.get_window(gtk.TEXT_WINDOW_TEXT)
        width, _ = win.get_size()
        fg_spec = "#FF0000"
        fg = gtk.gdk.color_parse(fg_spec)
        gc = gtk.gdk.GC(win, line_width=1)
        gc.set_rgb_fg_color(fg)
        win.draw_line(gc, 0, y, width, y)


if __name__ == '__main__':
    Draw0Demo()
    gtk.main()
