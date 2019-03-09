from systeminfo import LogFormat
import pandas as pd
import numpy as np
import os

FileFolder = LogFormat.FILE_PATH
#FileFolder = '/home/tang/PycharmProjects/SystemInfo/Logs'

def JmeterAnalysis(ReRun=False,Serialize=False):
    if os.path.exists("%s/npy/Jmeter.npy" % FileFolder):
        if ReRun:
            print "Has Exist"
        else:
            return
    CsvData = pd.read_csv("%s/%s" % (FileFolder,"Results.output")).sort_values(by='timeStamp',axis=0,ascending=True)
    CsvData['timeStamp'] = CsvData['timeStamp'].map(lambda x: x/10)

    RESULT_DIC = {}
    TimeStampeList = []
    for indexs in CsvData.index:
        Value = CsvData.loc[indexs].tolist()
        TimeStamp = Value[0]
        if TimeStamp not in TimeStampeList:
            TimeStampeList.append(TimeStamp)
#    print TimeStampeList
#    print len(TimeStampeList)

    for tsl in TimeStampeList:
        RESULT_DIC[tsl] = []
    RESULT_DIC[0] = []
    for indexs in CsvData.index:
        Value = CsvData.loc[indexs].tolist()
        TimeStamp = Value[0]
        Latency = Value[9]
        RESULT_DIC[TimeStamp].append(Latency)
    RESULT_DIC[0].append(TimeStampeList)
    if Serialize:
        np.save("%s/npy/%s" % (FileFolder, "Jmeter"), [RESULT_DIC])
    return RESULT_DIC

"""
if __name__=='__main__':
    print JmeterAnalysis()
"""