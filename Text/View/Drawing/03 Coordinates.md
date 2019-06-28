

# Textview Drawing - Coordinates


The tv has separate coordinates.

To deal with that, use:

`coords = widget.buffer_to_window_coords(gtk.TEXT_WINDOW_TEXT, x, y])`

and use the returned coords.

Now scroll, move, resize or do whatever to the window - the red apple will be where it is expected.


## Links

https://developer.gnome.org/pygtk/stable/class-gtktextview.html#method-gtktextview--get-window

https://developer.gnome.org/pygtk/stable/class-gtktextview.html#method-gtktextview--buffer-to-window-coords
