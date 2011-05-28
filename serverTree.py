#-*- coding:utf-8 -*-
import sys
import os
from xml.etree import ElementTree as ET
from config import *


try:
    import pygtk
    pygtk.require('2.0')
except:
    pass

try:
    import gtk
except:
    print "GTK Not avaliable!"
    sys.exit(1)

class serverTree:
    """serverTreeView Configuration
       为了删除特定的行，在添加时就记下当时的跌代器
       省的以后麻烦，我了个去的阿，这个难度有木有阿！
    """
    def __init__(self,treestore,treeview):
        self.ts=treestore
        self.tv=treeview
        self.serverlist=[]
        self.servergrouplist=[]

        #此迭代器记住每个servergroup所在的行
        self.sgiter={}
        self.siter={}

        self.piter={}

        #创建基本的treeviewcolumn
        self.tvcolumn=gtk.TreeViewColumn('Server Group')
        self.tv.append_column(self.tvcolumn)
        self.cell=gtk.CellRendererText()
        self.tvcolumn.pack_start(self.cell,True)
        self.tvcolumn.add_attribute(self.cell,'text',0)

        #找到selection
        self.tsc=self.tv.get_selection()
        self.mode=self.tsc.get_mode()

        #初始化左侧的目录树
        self.initTree()

    #初始化左侧目录树
    def initTree(self):
        """若服务器列表文件存在，则初始化左侧服务器列表"""
        if os.path.isfile('./server.xml'):
            root=ET.parse('server.xml').getroot()
            for parent in root.getchildren():
                self.piter[parent.tag]=self.ts.append(None,["%s" % parent.tag])
                for child in parent.getchildren():
                     self.piter[child.tag]=self.ts.append(self.piter[parent.tag],["%s" % child.tag])

    def updateTree(self):
        """对server或者servergroup改动后后更新,首先进行删除操作 """
        #首先将treestore中的列表清空
        self.ts.clear()
        #再重新初始化服务器列表
        if os.path.isfile('./server.xml'):
            root=ET.parse('server.xml').getroot()
            for parent in root.getchildren():
                self.piter[parent.tag]=self.ts.append(None,["%s" % parent.tag])
                for child in parent.getchildren():
                    self.piter[child.tag]=self.ts.append(self.piter[parent.tag],["%s" % child.tag])

    #增加Server时的行为
    def addServer(self,text1,text2):
        pass
    #增加ServerGroup时的行为
    def addServerGroup(self,text2):
        pass
    #增加删除server的行为
    def delServer(self,text):
        pass
    #此部分暂时没写好了
    def delServerGroup(self,text):
        pass
