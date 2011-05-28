#-*- coding=utf-8 -*-
#!/usr/bin/env python

class sysinfo:
        """获取系统信息"""
        def __init__(self):
            motherboard:dmidecode|grep Product|tail -n1|awk -F":" '{print $2}'

