#!/usr/bin/env python
#
# Small test to demonstrate glade.XML.signal_autoconnect on an instance
#

import pygtk
pygtk.require('2.0')
import gtk, gtk.glade

import hildon

class SimpleTest:
    def __init__(self):
        xml = gtk.glade.XML('test2.glade')
        xml.signal_autoconnect(self)

        window = hildon.Window()
        window.connect("destroy", gtk.main_quit)

        xml.get_widget("button1").reparent(window)
        xml.get_widget("window1").destroy()
        window.show_all()

    def on_button1_clicked(self, button):
        print 'foo!'

test = SimpleTest()
gtk.main()
