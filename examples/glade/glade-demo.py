#!/usr/bin/env python
import sys

import pygtk
pygtk.require('2.0')
import gtk
import gtk.glade

import hildon

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.glade'

# create widget tree ...
xml = gtk.glade.XML(fname)


def gtk_main_quit(*args):
    gtk.main_quit()

xml.signal_autoconnect(locals())

window = hildon.Window()
window.connect("destroy", gtk.main_quit)

# Reparenting the widgets and destroying the original window
xml.get_widget("vbox1").reparent(window)
xml.get_widget("window1").destroy()

window.show_all()

gtk.main()
