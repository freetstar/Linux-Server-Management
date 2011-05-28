#-*- coding:utf-8 -*-
import sys
import os
from xml.etree import ElementTree as ET

class config:
    """用来存储配置文件"""

    def __init__(self):
        """创建ET对象，创建main这个root标签"""
        self.root=ET.Element("root")
        self.tree=ET.ElementTree(self.root)

    def configAddServer(self,text1,text2):
        """添加server的配置文件,同时添加server对应的子元素，将ip等设置为tag，值设置为text
           如果要添加的服务器对应的group不存在，则首先创建一个group，然后再进行添加
        """
        if os.path.isfile('./server.xml'):
            self.root=ET.parse(r'server.xml').getroot()

        self.group=self.root.find(text2)
        if self.group is None:
            self.configAddServerGroup(text2)
            self.group=self.root.find(text2)
        self.server=ET.SubElement(self.group,text1)
        ET.SubElement(self.server,"ip")
        ET.SubElement(self.server,"port")
        ET.SubElement(self.server,"user")
        ET.SubElement(self.server,"password")
        ET.SubElement(self.server,"motherboard")
        ET.SubElement(self.server,"bios")
        ET.SubElement(self.server,"cpu")
        ET.SubElement(self.server,"cpucache")
        ET.SubElement(self.server,"network")
        ET.SubElement(self.server,"hostname")
        ET.SubElement(self.server,"cpubit")
        ET.SubElement(self.server,"kernel")
        ET.SubElement(self.server,"os")
        ET.SubElement(self.server,"shell")
        ET.SubElement(self.server,"gcc")
        ET.SubElement(self.server,"mem")

        ET.ElementTree(self.root).write("server.xml")

    def configDelServer(self,text1,text2):
        """删除特定的服务器"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root:
            if parent.tag == text2 :
                 for child in parent.getchildren():
                     if child.tag == text1:
                          parent.remove(child)
                          ET.ElementTree(self.root).write("server.xml")

    def configAddServerGroup(self,text):
        """在xml文件中创建servergroup元素"""
        if os.path.isfile('./server.xml'):
            self.root=ET.parse(r'server.xml').getroot()
        servergroup=ET.SubElement(self.root,text)
        ET.ElementTree(self.root).write("server.xml")

    def addServerInfo(self,server,text1,text2,text3,text4):
        """增加xml中各个server的配置信息"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root:
            for child in parent.getchildren():
                if child.tag == server  :
                    self.server=child
        self.server[0].text=text1
        self.server[1].text=text2
        self.server[2].text=text3
        self.server[3].text=text4
        ET.ElementTree(self.root).write("server.xml")

    def addServerConf(self,server,text1,text2,text3,text4,text5,text6,text7,text8):
            root=ET.parse("server.xml").getroot()
            for parent in root:
                for child in parent.getchildren():
                        if child.tag == server:
                            self.server=child
            self.server[6].text=text1
            self.server[7].text=text2
            self.server[9].text=text3
            self.server[10].text=text4
            self.server[11].text=text5
            self.server[12].text=text6
            self.server[13].text=text7
            self.server[14].text=text8
            ET.ElementTree(root).write("server.xml")

    def getServerIp(self,server):
        """获取server的IP信息"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root:
            for child in parent.getchildren():
                    if child.tag == server :
                            self.server=child
        return self.server[0].text

    def getServerPort(self,server):
        """获取server的Port信息"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root:
            for child in parent.getchildren():
                    if child.tag == server :
                            self.server=child
        return self.server[1].text

    def getServerUser(self,server):
        """获取server的User信息"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root:
            for child in parent.getchildren():
                    if child.tag == server :
                            self.server=child
                            return self.server[2].text

    def getServerPasswd(self,server):
        """获取server的Password信息"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root:
            for child in parent.getchildren():
                    if child.tag == server :
                            self.server=child
        return self.server[3].text

    def getServerInfo(self,server):
        """获取server的所有信息"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root:
            for child in parent.getchildren():
                    if child.tag == server :
                            self.server=child
        return (self.server[0].text,self.server[1].text,self.server[2].text,self.server[3].text)

    def findServerGroup(self,servergroup):
        """寻找特定的服务器组,并且返回tag值"""
        self.root=ET.parse("server.xml").getroot()
        for parent in self.root :
            if parent.tag == servergroup:
                print "找到的parent是" , parent.tag
                return parent.tag

