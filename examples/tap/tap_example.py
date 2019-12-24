#!/usr/bin/env python2.5

import gtk
import hildon

# Simple example about using tap-and-hold.

class Prog(object):

    def __init__(self):
        object.__init__(self)
        self.window = hildon.Window()
        self.window.connect("destroy", gtk.main_quit)
        
        menu = gtk.Menu()
        for i in range(3):
            item = gtk.MenuItem("Item %d" % i)
            menu.append(item)
            item.show()
        
        menu.show()

        vbox = gtk.VBox()

        hboxX = gtk.HBox()
        hboxX.pack_start(gtk.Label("X coord"), False, False)
        self.spin_x = gtk.SpinButton(gtk.Adjustment(lower=-100,upper=100,
                                                    step_incr=5))
        hboxX.pack_start(self.spin_x, True, True)
        vbox.pack_start(hboxX)

        hboxY = gtk.HBox()
        hboxY.pack_start(gtk.Label("Y coord"), False, False)
        self.spin_y = gtk.SpinButton(gtk.Adjustment(lower=-100,upper=100,
                                                    step_incr=5))
        hboxY.pack_start(self.spin_y, True, True)
        vbox.pack_start(hboxY)

        self.check_push = gtk.CheckButton(label="Push-In")
        vbox.pack_start(self.check_push)

        self.button_box = gtk.HBox()

        self.button = gtk.Button("Tap test")
        #Registers this widget to listen to tap-and-hold signals.
        #The callback is used to position the menu.
        self.button.tap_and_hold_setup(menu=menu, callback=self.cb,
                                       data="Foo data")
        self.button_box.pack_start(self.button)

        but_del = gtk.Button("Delete Source")
        but_del.connect("clicked", self.del_source)
        self.button_box.pack_start(but_del)

        vbox.pack_start(self.button_box)
    
        self.window.add(vbox)

    def del_source(self, button, data=None):
        print "Deleting source button"
        self.button.destroy()

    def cb(self, menu, widget=None, data=None):

        print menu
        print widget
        print data

        req_w, req_h = menu.size_request()

        top = widget.get_toplevel()
        w_x, w_y = top.window.get_origin()

        point_x, point_y, mods = top.window.get_pointer()

        menu_x = point_x + w_x
        menu_y = point_y + w_y - req_h
        
        #if widget.get_direction == gtk.TEXT_DIR_RTL:
        #    menu_x = menu_x + widget.allocation.width - req_w

        scr_w = widget.get_screen().get_width()

        if (menu_x < w_x):
            menu_x = w_x
        elif (menu_x + req_w) > scr_w:
            menu_x -= ((menu_x + req_w) - scr_w)

        if menu_y < w_y:
                meny_y = w_y

        menu_x += int(self.spin_x.get_value())
        menu_y += int(self.spin_y.get_value())

        print "Setting menu at (%d, %d, %d)" % (menu_x, menu_y, self.check_push.get_active())

        return menu_x, menu_y, self.check_push.get_active()

    def run(self):
        self.window.show_all()
        gtk.main()

if __name__ == "__main__":
    prog = Prog()
    prog.run()
