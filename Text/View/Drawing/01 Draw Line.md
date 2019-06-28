

# Draw a line on a Textview


Textview = tv

Drawing happens on the expose signal of the tv-widget.

Hook up to that event:
`tv.connect("expose-event", cb-name)`


## In the Callback

Note:
I skip part one of the cb-code, because it is not in the focus.

I ignore the event which is passed as second argument.
All i need is the calling widget, the tv.

Unlike the gtk.widget's method get_window,
TextView.get_window returns a gdk.window and takes a parameter which window one wants,
hence it is composed of multiple windows.

Here I use:
`gtk.TEXT_WINDOW_TEXT` - The window that holds the text

Getting the window and its size.

```python
win = widget.get_window(gtk.TEXT_WINDOW_TEXT)
width, _ = win.get_size()
```

Now I pick the Color I want:

```python
fg_spec = "#FF0000"
fg = gtk.gdk.color_parse(fg_spec)
```

Get the GDK Graphics Context and set line width.

```python
gc = gtk.gdk.GC(win, line_width=1)
gc.set_rgb_fg_color(fg)
```
Finally draw the line on the window with the modificated context.

```python
win.draw_line(gc, 0, self.y, width, self.y)
```
Draws the line from point one x,y to point two x,y.


## Links

GDK Drawable
https://developer.gnome.org/pygtk/stable/class-gdkdrawable.html

GDK Graphics Context
https://developer.gnome.org/pygtk/stable/class-gdkgc.html

GDK Color
https://developer.gnome.org/pygtk/stable/class-gdkcolor.html