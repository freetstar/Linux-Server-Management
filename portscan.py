#!/usr/bin/env python2
#-*- coding=utf-8 -*-
import socket as sk
import sys
import threading

#MAX HTREADING YOU CAN RUN AT ONE TIME
MAX_THREADS=20


class Scanner(threading.Thread):
    """具体的scanner类"""
    def __init__(self,host,port):
        threading.Thread.__init__(self)
        self.host=host
        self.port=port
        self.sd=sk.socket(sk.AF_INET,sk.SOCK_STREAM)

        #将扫描出来的文件放到特定文件中，以便共享

    def run(self):
        try:
            self.sd.connect((self.host,self.port))
            print "ok"
            string="%s:%d OPEN" % (self.host,self.port)
            self.filename="%s" % self.host
            self.f=open(self.filename,"w",0)
            self.f.write(string)
            self.f.write("\n")
            self.f.close()
        except:
            pass

class pyScan():
    """ Scan port opened;By default,pyscan scan 1 to 1024 port"""
    def __init__(self):
        self.start,self.stop=1,1024
        self.host="127.0.0.1"

        try:
            sk.gethostbyname(self.host)
        except:
            print "hostname '%s' unknow " % self.host

    def scan(self,host,start,stop):
        self.port=start
        while self.port<=stop and  threading.activeCount()<MAX_THREADS:
                Scanner(host,self.port).start()
                self.port+=1
                if self.port > 65535:
                    sys.exit(1);

if __name__=="__main__":
    pyScan()
