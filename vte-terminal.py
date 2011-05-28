#!/usr/bin/env python
import vte
import pygtk
pygtk.require('2.0')
import gtk

if __name__=='__main__':
        v=vte.Terminal()
        v.connect("child-exited",lambda term: gtk.main_quit())
        v.fork_command()

        window=gtk.Window()
        window.add(v)
        window.connect('delete_event',lambda widnow,event:gtk.main_quit())

        window.show_all()

        gtk.main()

