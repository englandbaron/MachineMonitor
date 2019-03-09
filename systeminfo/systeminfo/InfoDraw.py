import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from systeminfo import LogFormat

FileFolder = LogFormat.FILE_PATH


def InfoDicCreator(FileName, Serialize=False):
    PE_LIST = []
    MEM_LIST = []
    NET_SENT_LIST = []
    NET_RECV_LIST = []

    FILE = open("%s/%s" % (FileFolder, FileName), 'r')
    FILE_READ = FILE.readline()

    Times = 0
    while FILE_READ:
        FILE_SPLIT = FILE_READ.split()
        PE = float(FILE_SPLIT[8])
        MEM = float(FILE_SPLIT[11])
        NET_SENT = float(FILE_SPLIT[15])
        NET_RECV = float(FILE_SPLIT[18])

        PE_LIST.append(PE)
        MEM_LIST.append(MEM)
        NET_SENT_LIST.append(NET_SENT)
        NET_RECV_LIST.append(NET_RECV)
        Times = Times + 1
        # print FILE_SPLIT
        # print "PE: %s, MEM: %s, NET_SENT: %s, NET_RECV: %s" % (PE,MEM,NET_SENT,NET_RECV)
        FILE_READ = FILE.readline()
    DIC = {"Times": Times, "PE_LIST": PE_LIST, "MEM_LIST": MEM_LIST, "NET_SENT_LIST": NET_SENT_LIST,
           "NET_RECV_LIST": NET_RECV_LIST}
    if Serialize:
        np.save("%s/npy/%s" % (FileFolder, FileName), DIC)
    return DIC

'''
EquipmentName ------
		|
		|--PE_LIST
		|
		|--MEM_LIST
		|
		|--NET_SENT_LIST
		|
		|--NET_RECV_LIST
'''
def Draw_OnlyOne(DIC,EquipmentName):
    Time_LIST = [i for i in range(DIC["Times"])]
    print DIC[EquipmentName]
    print Time_LIST
    plt.plot(Time_LIST, DIC[EquipmentName])
    #plt.title("%s Degeneration Plot" % EquipmentName)
    plt.show()

def Draw(DIC):
    Time_LIST = [i for i in range(DIC["Times"])]

    plt.subplot(2, 2, 1)
    plt.plot(Time_LIST, DIC["PE_LIST"])
    plt.title("PE Degeneration Plot")

    plt.subplot(2, 2, 2)
    plt.plot(Time_LIST, DIC["MEM_LIST"])
    plt.title("MEM Degeneration Plot")

    plt.subplot(2, 2, 3)
    plt.plot(Time_LIST, DIC["NET_SENT_LIST"])
    plt.title("NET_SENT Degeneration Plot")

    plt.subplot(2, 2, 4)
    plt.plot(Time_LIST, DIC["NET_RECV_LIST"])
    plt.title("NET_RECV Degeneration Plot")

    plt.suptitle("Machine Degeneration Plot")
    plt.show()

def Draw_Performance(FileName='Jmeter.npy'):
    NpyFile = np.load("%s/npy/%s" % (FileFolder,FileName)).tolist()[0]
    print NpyFile
    X = NpyFile[0][0]
    Y = []
    for tsp in X:
        print tsp
        Tmp_List = NpyFile[tsp]
        print len(Tmp_List)
        #Y.append(max(Tmp_List))
        Y.append(sum(Tmp_List)/len(Tmp_List))
    plt.plot(X,Y)
    plt.show()