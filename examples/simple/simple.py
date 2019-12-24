#!/usr/bin/env python

# translation of the simple.c test in the gtk+ distribution, using the
# new() function from gobject (this is an example of creating objects
# with the properties interface).
#
# Adapted to hildon (Use hildon.Window instead of gtk.Window)
#
import pygtk
pygtk.require('2.0')
import gobject, gtk
import hildon

def hello(*args):
    print "Hello World"
    window.destroy()

def destroy(*args):
    window.hide()
    gtk.main_quit()

window = gobject.new(hildon.Window,
             type=gtk.WINDOW_TOPLEVEL,
             title='Hello World',
             allow_grow=False,
             allow_shrink=False,
             border_width=10)
window.connect("destroy", destroy)

button = gobject.new(gtk.Button, label="Hello World", parent=window)
button.connect("clicked", hello)

window.show_all()
gtk.main()
