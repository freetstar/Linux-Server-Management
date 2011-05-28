#-*- coding=utf-8 -*-
#!/usr/bin/env python

import paramiko

class sshGetInfo:

    def __init__(self,host,port,username,password):
        self.hostname=host
        self.port=port
        self.username=username
        self.password=password

    def exe(self,str):
        paramiko.util.log_to_file('paramiko.log')
        self.s=paramiko.SSHClient()
        self.s.load_system_host_keys()
        self.s.connect(self.hostname,self.port,self.username,self.password)
        stdin,stdout,stderr=self.s.exec_command(str)
        #将标准输出的结果保存到result变量中并返回
        result=stdout.read()
        self.s.close()
        return  result
