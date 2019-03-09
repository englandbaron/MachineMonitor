import logging
import time
import ConfigParser

def GetConfig(section,key):
    cf = ConfigParser.ConfigParser()
    cf.read("Config.ini")
    return cf.get(section,key)

FILE_PATH= GetConfig("config","LogPath") #Default

def getLogger(DebugMode=False):
    if DebugMode:
        logging.basicConfig(level=logging.NOTSET, format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
        logger = logging.getLogger()
        return logger
    else:
        FILE_NAME = "%s.log" % time.strftime('%Y%m%d%H%M-%S', time.localtime(time.time()))

        fh = logging.FileHandler("%s/%s" % (FILE_PATH, FILE_NAME), mode='w')
        formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(fh)
        return logger

#if __name__=='__main__':
#    ConfigDic = GetConfig()
#    print ConfigDic
