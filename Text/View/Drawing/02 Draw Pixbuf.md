

#Draw a Pixbuf on a Textview


gtk.gdk.Drawable.draw_pixbuf

def draw_pixbuf(gc, pixbuf, src_x, src_y, dest_x, dest_y, width=-1, height=-1, dither=gtk.gdk.RGB_DITHER_NORMAL, x_dither=0, y_dither=0)
gc : a gtk.gdk.GC, used for clipping, or None
pixbuf : a gtk.gdk.Pixbuf
src_x : Source X coordinate within pixbuf.
src_y : Source Y coordinate within pixbuf.
dest_x : Destination X coordinate within drawable.
dest_y : Destination Y coordinate within drawable.
width : Width of region to render, in pixels, or -1 to use pixbuf width. Must be specified in PyGTK 2.2.
height : Height of region to render, in pixels, or -1 to use pixbuf height. Must be specified in PyGTK 2.2
dither : Dithering mode for GdkRGB.
x_dither : X offset for dither.
y_dither : Y offset for dither.

## Links
https://developer.gnome.org/pygtk/stable/class-gdkdrawable.html#method-gdkdrawable--draw-pixbuf