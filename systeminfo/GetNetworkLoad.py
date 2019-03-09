#coding: utf-8
import functions
import time
import os
import psutil

class NetworkLoad(object):
    def __init__(self,NC=None):
        self.NC = NC
        net = psutil.net_io_counters(pernic=True)
        time.sleep(1)
        net1 = psutil.net_io_counters(pernic=True)
        self.net_stat_download = {}
        self.net_stat_upload = {}
        for k, v in net.items():
            for k1, v1 in net1.items():
                if k1 == k:
                    self.net_stat_download[k] = (v1.bytes_recv - v.bytes_recv) / 1000.
                    self.net_stat_upload[k] = (v1.bytes_sent - v.bytes_sent) / 1000.
        #ds = os.statvfs('/')
        #disk_str = {"Used": ((ds.f_blocks - ds.f_bfree) * ds.f_frsize) / 10 ** 9,
        #"Unused": (ds.f_bavail * ds.f_frsize) / 10 ** 9}

    def GetSentRatio(self):
        if(self.NC == None):
            return self.net_stat_upload
        else:
            return self.net_stat_upload[self.NC]

    def GetRecvRatio(self):
        if(self.NC == None):
            return self.net_stat_download
        else:
            return self.net_stat_download[self.NC]