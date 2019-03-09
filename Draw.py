import systeminfo.PerformanceTest as performancetest
import systeminfo.InfoDraw as infodraw
import sys

if __name__ == '__main__':
    DIC=performancetest.JmeterAnalysis(ReRun=False,Serialize=True)
    #print DIC
    infodraw.Draw_Performance()
    #DIC = infodraw.InfoDicCreator(sys.argv[1],Serialize=False)
    #infodraw.Draw_OnlyOne(DIC,'PE_LIST')