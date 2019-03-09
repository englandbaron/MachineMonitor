import systeminfo.MachineInfo as MachineInfo
import systeminfo.LogFormat as Logger
#import systeminfo.InfoDraw as infodraw
import sys

Debug = True
#Debug = False
def Listener(NetCard='eth2'):
    logger = Logger.getLogger(DebugMode=Debug)
    while True:
        """
        logger.info("Mahcine PE : %s " % MachineInfo.GetCpuPercent()['cpu'])
        logger.info("Machine Memory : %s " % MachineInfo.GetMemPercent())
        logger.info("Machine Network : %s " % MachineInfo.GetNetworkLoad('eth2'))
        """
        logger.info("Machine PE %s , Memory %s , Network %s" % (
            MachineInfo.GetCpuPercent(), MachineInfo.GetMemPercent(),
            MachineInfo.GetNetworkLoad_Division(NetCard)))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        Listener()
    else:
        Listener(sys.argv[1])
    #DIC = infodraw.InfoDicCreator('201810261704-14.log',Serialize=True)
    #infodraw.Draw(DIC)
#Listener()
