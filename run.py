#-*- coding: utf-8 -*-
#author:freetstar
#mail:lgxwqq@gmail.com
#blog:www.freetstar.com
#Useage:A desktop software for linux server system administrators
#
from serverTree import *
from config import *
from portscan import *
from terminal import *
from ssh import *
from pychartdir import *
import sys
import os
from xml.etree import ElementTree as ET

try:
    import pygtk
    pygtk.require('2.0')
except:
    pass

try:
    import gtk
except:
    error=gtk.MessageDialog(None,gtk.DIALOG_MODEL,gtk.MESSAGE_ERROR, "GTK+ Not Avaliable!")
    error.run()
    sys.exit(1)

try:
    import vte
except:
    error=gtk.MessageDialog(None,gtk.DIALOG_MODEL,gtk.MESSAGE_ERROR,'you need to install python bindings for libvtr')
    error.run()
    sys.exit(1)

class systemCM:
    """系统管理员的工具"""

    def on_window_destroy(self,widget,data=None):
        gtk.main_quit()

    def __init__(self):
        """init all stuff and signals"""

        #从xml文件中读取数据,并链接必要的信号
        self.builder=gtk.Builder()
        self.file=sys.path[0]+"/run.glade"
        self.builder.add_from_file(self.file)
        self.builder.connect_signals(self)
        for widget in  self.builder.get_objects():
            if issubclass(type(widget),gtk.Buildable):
                name=gtk.Buildable.get_name(widget)
                setattr(self,name,widget)


        #创建一个Terminal的实例,并且添加到登录管理的标签页中
        self.myterm=MyTerm()
        self.vbox6.add(self.myterm.terminal)

        #创建一个treeview的实例
        self.stInstance=serverTree(self.treestore,self.treeview)
        #创建一个cfInstance实例
        self.cfInstance=config()
        #创建一个pyScan的实例
        self.pInstance=pyScan()

        #创建ListStore用来在增加server时补全显示group的信息
        #从及时输入的信息和xml中获取信息
        self.liststore=gtk.ListStore(str)
        self.entrycompletion.set_model(self.liststore)
        self.addservergroupentry1.set_completion(self.entrycompletion)
        self.entrycompletion.set_text_column(0)
        if os.path.isfile('./server.xml'):
            for child in ET.parse('server.xml').getroot():
                self.liststore.append([child.tag])

        #获取statusbar的id
        self.context_id=self.statusbar.get_context_id("Linux Server")

        #显示所有窗体
        self.window.set_size_request(800,500)
        self.window.show_all()
        #先暂时关闭这个用来显示硬盘图形信息的image控件
        self.fulltextimage.hide()

    #设置标题栏的行为
    #设置增加单个服务器窗口的行为
    #弹出增加服务器对话框
    def on_addserver_activate(self,widget,data=None):
        self.addserverdialog.run()

    #点击增加服务器对话框窗口的ok按钮时
    def on_addserverok_clicked(self,widget,data=None):
        self.addservertext=self.addserverentry.get_text()
        self.addservergroupentry1text=self.addservergroupentry1.get_text()
        self.cfInstance.configAddServer(self.addservertext,self.addservergroupentry1text)
        self.stInstance.updateTree()
        self.addserverdialog.hide()

    #点击增加服务器对话框窗口的cancle按钮时
    def on_addservercancle_clicked(self,widget,data=None):
        self.addserverdialog.destroy()

    #设置增加服务器组窗口的行为
    #弹出增加服务器组对话框
    def on_addservergroup_activate(self,widget,data=None):
        self.addservergroupdialog.run()

    #点击增加服务器组ok按钮
    def on_addservergroupok_clicked(self,widget,data=None):
        self.addservergroupentry2text=self.addservergroupentry2.get_text()
        self.cfInstance.configAddServerGroup(self.addservergroupentry2text)
        self.stInstance.updateTree()
        self.liststore.append([self.addservergroupentry2text])
        self.addservergroupdialog.hide()

    #点击增加服务器组cancle按钮
    def on_addservergroupcancle_clicked(self,widget,data=None):
        self.addservergroupdialog.destroy()

    #删除服务器窗口的行为
    #单击删除服务器
    def on_delserver_activate(self,widget,data=None):
        self.delserverdialog.run()

    #点击删除服务器ok按钮
    def on_delserverok_clicked(self,widget,data=None):
        self.delserverentrytext=self.delserverentry.get_text()
        self.delservergroupentrytext=self.delservergroupentry.get_text()
        self.cfInstance.configDelServer(self.delserverentrytext,self.delservergroupentrytext)
        self.stInstance.updateTree()
        self.delserverdialog.hide()

    def on_delservercancle_clicked(self,widget,data=None):
        self.delserverdialog.destroy()

    #单击删除服务器组的行为
    def on_delservergroup_activate(self,widget,data=None):
        pass

    def on_delservergroupon_clicked(self,widget,data=None):
        pass

    def on_delservergroupcancle_clicked(self,widget,data=None):
        pass

    #单击aboutme窗体时的行为
    def on_about_activate(self,widget,data=None):
        self.aboutdialog.run()

    #定义首选项按钮被选中时的行为
    def on_preference_activate(self,widget,data=None):
        self.preferencedialog.run()

    #定义首选项对话框的保存按钮按下时的行为
    def on_preferenceokbutton_clicked(self,widget,data=None):
        pass

    #定义首选项对话框的关闭按钮按下是的行为
    def on_preferenceclosebutton_clicked(self,widget,data=None):
        self.preferencedialog.destroy()

    def on_tabup_toggled(self,widget,data=None):
        self.notebook.set_tab_pos(gtk.POS_TOP)

    def on_tabdown_toggled(self,widget,data=None):
        self.notebook.set_tab_pos(gtk.POS_BOTTOM)

    def on_tableft_toggled(self,widget,data=None):
        self.notebook.set_tab_pos(gtk.POS_LEFT)

    def on_tabright_toggled(self,widget,data=None):
        self.notebook.set_tab_pos(gtk.POS_RIGHT)

##########################################################################
#定义软件主界面区域的动作
##########################################################################

    def on_configok_clicked(self,widget,data=None):
        """获取服务器相应的值，并存到xml文档中"""
        (model,iter)=self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        text1=self.entry1.get_text()
        text2=self.entry2.get_text()
        text3=self.entry3.get_text()
        text4=self.entry4.get_text()
        self.cfInstance.addServerInfo(server,text1,text2,text3,text4)
        self.entry1.set_text("")
        self.entry2.set_text("")
        self.entry3.set_text("")
        self.entry4.set_text("")

    def on_configcancle_clicked(self,widget,data=None):
        """取消添加服务器信息,将所有的对话框重置为空"""
        self.entry1.set_text("")
        self.entry2.set_text("")
        self.entry3.set_text("")
        self.entry4.set_text("")

    #定义端口扫描按钮按下时的行为
    def on_portscanok_clicked(self,widget,data=None):
        """先将扫描端口的结果存放到文件中，然后再读取出来到buffer中"""
        self.sport=int(self.startport.get_text())
        self.eport=int(self.endport.get_text())

        #获取当前将要进行扫描的server的ip地址
        (model,iter)=self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        self.serverip=self.cfInstance.getServerIp(server)

       # self.pInstance.scan(self.serverip,self.sport,self.eport)
        self.portbuffer=self.porttextview.get_buffer()
        #打开文件，将文件中的内容发送到屏幕的textbuffer上
        infile=open(self.serverip,"r")
        if infile :
            string=infile.read()
            self.portbuffer.set_text(string)
            infile.close()
        self.statusbar.push(self.context_id,"Port Scan Done!")

    #定义服务器信息保存时要做的行为

    #定义aboutdialog的close按钮按下时的行为
    def on_aboutdialogaac(self,widget,data=None):
        self.aboutdialog-action_area.destroy()

    #定义一组6个网络查询的按钮情况

    #定义网络信息按钮按下时的行为
    def on_ifconfigbutton_clicked(self,widget,data=None):
        #首先获取选取的服务器的各种信息
        (model,iter) = self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        ip,port,username,passwd = self.cfInstance.getServerInfo(server)
        #然后通过ssh获取服务器的ifconfig信息,并保留在temp变量中
        temp=sshGetInfo(ip,int(port),username,passwd).exe('ifconfig')
        #展示到下边的textview上
        self.ifconfigbuffer=self.fulltextview.get_buffer()
        self.ifconfigbuffer.set_text(temp)

    #定义内存信息按钮按下时的行为
    def on_memorybutton_clicked(self,widget,data=None):
        #首先获取选取的服务器的各种信息
        (model,iter) = self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        ip,port,username,passwd = self.cfInstance.getServerInfo(server)
        #然后通过ssh获取服务器的memory信息,并保留在temp变量中
        temp=sshGetInfo(ip,int(port),username,passwd).exe('free')
        #展示到下边的textview上
        self.ifconfigbuffer=self.fulltextview.get_buffer()
        self.ifconfigbuffer.set_text(temp)

    #定义硬盘信息按钮按下时的行为
    def on_diskbutton_clicked(self,widget,data=None):
        """定义服务器信息"""
        #首先获取选取的服务器的各种信息
        (model,iter) = self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        ip,port,username,passwd = self.cfInstance.getServerInfo(server)
        #然后通过ssh获取服务器的fdisk信息,并保留在temp变量中
        temp=sshGetInfo(ip,int(port),username,passwd).exe("df  -h  / |tail -n1 |awk '{print $5,$6}'|sed 's/%//'")
        #展示到下边的textvie'上
        result=temp.split(' ')
        data=[int(result[0]),100-int(result[0])]
        Labels=["used","free"]
        c=PieChart(360,300)
        c.setPieSize(180,140,100)
        c.setData(data,Labels)
        c.makeChart("icons/result.png")
        self.fulltextview.hide()
        self.fulltextimage.show()
        self.fulltextimage.set_from_file("icons/result.png")


    #定义进程信息按钮按下时的行为
    def on_processbutton_clicked(self,widget,data=None):
        #首先获取选取的服务器的各种信息
        (model,iter) = self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        ip,port,username,passwd = self.cfInstance.getServerInfo(server)
        #然后通过ssh获取服务器的process信息,并保留在temp变量中
        temp=sshGetInfo(ip,int(port),username,passwd).exe('ps axu')
        #展示到下边的textview上
        self.ifconfigbuffer=self.fulltextview.get_buffer()
        self.ifconfigbuffer.set_text(temp)

    #定义网络链接信息按钮按下时的行为
    def on_networkbutton_clicked(self,widget,data=None):
        #首先获取选取的服务器的各种信息
        (model,iter) = self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        ip,port,username,passwd = self.cfInstance.getServerInfo(server)
        #然后通过ssh获取服务器的network信息,并保留在temp变量中
        temp=sshGetInfo(ip,int(port),username,passwd).exe('netstat -antu')
        #展示到下边的textview上
        self.ifconfigbuffer=self.fulltextview.get_buffer()
        self.ifconfigbuffer.set_text(temp)

    #定义负载信息按钮按下时的行为
    def on_overloadbutton_clicked(self,widget,data=None):
        #首先获取选取的服务器的各种信息
        (model,iter) = self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        ip,port,username,passwd = self.cfInstance.getServerInfo(server)
        #然后通过ssh获取服务器的overload信息,并保留在temp变量中
        temp=sshGetInfo(ip,int(port),username,passwd).exe('cat /proc/loadavg')
        #展示到下边的textview上
        self.ifconfigbuffer=self.fulltextview.get_buffer()
        self.ifconfigbuffer.set_text(temp)

   #定义刷新服务器信息按钮按下时的行为
    def on_refreshserverinfo_clicked(self,widget,data=None):
        print "刷新系统信息"
        #首先获取选取的服务器的各种硬件和软件的信息
        (model,iter) = self.stInstance.tsc.get_selected()
        server=self.stInstance.ts.get_value(iter,0)
        ip,port,username,passwd = self.cfInstance.getServerInfo(server)
        #然后通过ssh获取服务器的各种硬件信息,并保留在tmp1变量中
        tmp1=sshGetInfo(ip,int(port),username,passwd).exe('dmidecode')

        tmp2=sshGetInfo(ip,int(port),username,passwd).exe('cat /proc/cpuinfo|grep name|head -n1|cut -d: -f2;cat /proc/cpuinfo|grep "cache size" |head -n1|cut -d: -f2;getconf LONG_BIT;hostname;uname -r -m;cat /etc/issue|head -n1;echo $SHELL;gcc --version|head -n1')
        result=tmp2.split('\n')
        self.cpulabel2.set_text(result[0])
        self.cpucachelabel2.set_text(result[1])
        self.cpubitlabel2.set_text(result[2])
        self.hostnamelabel2.set_text(result[3])
        self.kernellabel2.set_text(result[4])
        self.oslabel2.set_text(result[5])
        self.shelllabel2.set_text(result[6])
        self.gcclabel2.set_text(result[7])
        #将此部分信息添加到server的配置文件中去
        self.cfInstance.addServerConf(server,result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7])
        #将获取的temp变量分别设置成label显示文本

    #定义退出按钮按下时的行为
    def on_quit_activate(self,widget,data=None):
        dialog = gtk.Dialog("Quit?",self.window,gtk.DIALOG_MODAL,(gtk.STOCK_CANCEL,gtk.RESPONSE_REJECT,gtk.STOCK_QUIT,gtk.RESPONSE_ACCEPT))
        label = gtk.Label("Do you really want to quit?")
        dialog.vbox.pack_start (label,True,True,0)
        label.show()

        res = dialog.run()
        if res == gtk.RESPONSE_ACCEPT:
            dialog.destroy()
            gtk.main_quit()
        else :
            dialog.destroy()

    #主循环
    def main(self):
        gtk.main()

if __name__=="__main__":
    cm=systemCM()
    cm.main()
