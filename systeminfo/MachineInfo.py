import psutil
from GetCpuLoad import GetCpuLoad
from GetNetworkLoad import NetworkLoad

def GetCpuPercent():
    CPU = GetCpuLoad()
    return CPU.getcpuload()

def GetMemPercent():
    return psutil.virtual_memory().percent

def GetNetworkLoad(NC=None):
    NetInfo = NetworkLoad(NC)
    return {"SENT":NetInfo.GetSentRatio(),"RECV":NetInfo.GetRecvRatio()}

def GetNetworkLoad_Division(NC=None):
    NetInfo = NetworkLoad(NC)
    return "SENT %s , RECV %s" % (NetInfo.GetSentRatio(),NetInfo.GetRecvRatio())