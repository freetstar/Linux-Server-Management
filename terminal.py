#-*- coding=utf-8 -*-
import vte
import gtk


class MyTerm():
    def __init__(self):
        """初始化一个term对象"""
        self.terminal=vte.Terminal()
        self.terminal.connect("child-exited",lambda term: self.vte_exit())
        self.terminal.fork_command()
        self.terminal.set_size(10,20)

    def vte_exit(self):
        """当terminal退出时，直接重新产生一个terminal，并clear初始化"""
        self.terminal.fork_command()
        self.terminal.feed_child("clear\n")

    def vte_message(self):
        pass

