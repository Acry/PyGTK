#!/usr/bin/env python2
# -*- coding: utf-8 -*-
u"""05 Draw PixBufAnim.py
"""

import gtk
import gobject
import os
import time

ICON_IMAGE = os.path.join('gtk-logo.svg')
FOURIER_IMAGE = os.path.join("Fourier_series_square_wave_circles_animation.gif")


class Draw5(gtk.Window):
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
        textview = gtk.TextView()
        textview.set_wrap_mode(gtk.WRAP_WORD)
        sw1 = gtk.ScrolledWindow()
        sw1.set_policy(1, 1)
        self.add(sw1)
        sw1.add(textview)

        # Create a new PixBufAnimation
        anim = gtk.gdk.PixbufAnimation(FOURIER_IMAGE)

        # Get the first PixbufAnimationIter
        _iter = anim.get_iter(start_time=0.0)
        pb = _iter.get_pixbuf()
        self.pb = pb
        del pb
        delay = _iter.get_delay_time()
        self.timer = gobject.timeout_add(delay, self.frame_update, _iter, textview)
        textview.connect("expose-event", self.expose)
        self.show_all()

    def frame_update(self, _iter, textview):
        if _iter.advance(time.time()):
            pb = _iter.get_pixbuf()
            self.pb = _iter.get_pixbuf()
            del pb
            textview.queue_draw()
        delay = _iter.get_delay_time()
        self.timer = gobject.timeout_add(delay, self.frame_update, _iter, textview)

    def expose(self, widget, event):
        win = widget.get_window(gtk.TEXT_WINDOW_TEXT)
        gc = gtk.gdk.GC(win)
        win.draw_pixbuf(gc, self.pb, 0, 0, 50, 50, width=-1, height=-1)


if __name__ == '__main__':
    Draw5()
    gtk.main()
