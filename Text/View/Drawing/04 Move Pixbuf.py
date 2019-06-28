#!/usr/bin/env python2

"""
04 Move Pixbuf.py

Hover the mouse over the pixbuf.
Press Control and move the pixbuf.

"""

import gtk
import os

ICON_IMAGE = os.path.join('gtk-logo.svg')
RED_APPLE = os.path.join('apple-red.png')

TEXT = __doc__


class Pix:
    pb = None
    x = None
    y = None

    def __init__(self, pb, x=0, y=0):
        self.pb = pb
        self.x = x
        self.y = y

    def add(self, pb, x=0, y=0):
        self.pb = pb
        self.x = x
        self.y = y


class Draw0Demo(gtk.Window):
    pix_list = []
    moving_pic = False  # The moving pic
    pic_moving = None   # Is any pic moving?
    offset = 0

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

        pb = gtk.gdk.pixbuf_new_from_file(RED_APPLE)
        pix = Pix(pb, 50, 120)
        self.pix_list.append(pix)
        pix = Pix(pb, 150, 120)
        self.pix_list.append(pix)
        pix = Pix(pb, 250, 120)
        self.pix_list.append(pix)
        tv = gtk.TextView()
        buf = tv.get_buffer()
        buf.set_text(TEXT)
        tv.set_wrap_mode(gtk.WRAP_WORD)
        sw = gtk.ScrolledWindow()
        sw.set_policy(1, 1)
        self.add(sw)
        sw.add(tv)
        tv.connect("expose-event", self.expose)
        tv.connect("button-press-event", self.button_press_callback)
        tv.connect("button-release-event", self.button_release_callback)
        tv.connect("motion-notify-event", self.on_motion)
        self.show_all()

    def expose(self, widget, event):
        win = widget.get_window(gtk.TEXT_WINDOW_TEXT)
        gc = gtk.gdk.GC(win)
        for pix in self.pix_list:
            coords = widget.buffer_to_window_coords(gtk.TEXT_WINDOW_TEXT, pix.x, pix.y)
            win.draw_pixbuf(gc, pix.pb, 0, 0, coords[0], coords[1], width=-1, height=-1)

    def on_motion(self, widget, event):
        if self.moving_pic:
            b = self.get_border_width()
            b = int(b)
            coords = widget.get_pointer()
            self.pic_moving.x = coords[0] - self.offset[0]
            self.pic_moving.y = coords[1] - b - self.offset[1]
            widget.queue_draw()

    def button_release_callback(self, widget, event, data=None):
        if self.moving_pic:
            self.moving_pic = False

    def button_press_callback(self, widget, event, data=None):
        if (event.get_state() & gtk.gdk.CONTROL_MASK) and event.button == 1:
            coords = widget.get_pointer()
            for pix in self.pix_list:
                """
                D   A
                +---+
                |   |
                +---+
                C   B
                """
                w = pix.pb.get_width()
                h = pix.pb.get_height()
                ax = pix.x + w
                ay = pix.y
                bx = pix.x + w
                by = pix.y + h
                cx = pix.x
                cy = pix.y + h
                dx = pix.x
                dy = pix.y

                if check(ax, ay, bx, by, cx, cy, dx, dy, coords[0], coords[1]):
                    self.moving_pic = True
                    self.pic_moving = pix
                    b = self.get_border_width()
                    b = int(b)
                    self.offset = (coords[0]-self.pic_moving.x, (coords[1] - b) - self.pic_moving.y)
                    return True


def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) +
                x2 * (y3 - y1) +
                x3 * (y1 - y2)) / 2.0)


def check(x1, y1, x2, y2, x3,
          y3, x4, y4, x, y):
    # Calculate area of rectangle ABCD
    A = (area(x1, y1, x2, y2, x3, y3) +
         area(x1, y1, x4, y4, x3, y3))

    # Calculate area of triangle PAB
    A1 = area(x, y, x1, y1, x2, y2)

    # Calculate area of triangle PBC
    A2 = area(x, y, x2, y2, x3, y3)

    # Calculate area of triangle PCD
    A3 = area(x, y, x3, y3, x4, y4)

    # Calculate area of triangle PAD
    A4 = area(x, y, x1, y1, x4, y4);

    # Check if sum of A1, A2, A3
    # and A4 is same as A
    return A == A1 + A2 + A3 + A4


if __name__ == '__main__':
    Draw0Demo()
    gtk.main()
