#!/usr/bin/env python2

"""
Draw Pixbuf.py

Drawing on a Textview Window.

"""

import gtk
import os

ICON_IMAGE = os.path.join('gtk-logo.svg')
RED_APPLE = os.path.join('apple-red.png')

TEXT = __doc__


class Draw0Demo(gtk.Window):
    pb = None

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
        self.pb = gtk.gdk.pixbuf_new_from_file(RED_APPLE)
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
        win = widget.get_window(gtk.TEXT_WINDOW_TEXT)
        gc = gtk.gdk.GC(win)
        win.draw_pixbuf(gc, self.pb, 0, 0, 75, 150, width=-1, height=-1)


if __name__ == '__main__':
    Draw0Demo()
    gtk.main()
