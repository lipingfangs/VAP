import sys
import os

frqfilename = sys.argv[1].split(",")[0]
pathwaybedfilename = sys.argv[2]
populationmark = sys.argv[1].split(",")[1]

frqfile= open(frqfilename,"r")
frqfilelist =   frqfile.readlines()
frqfile.close()

dicfreq = {}
for i in frqfilelist[1:]:
    dicfreq[i.split()[1]] = {}
    if i.split()[2] == "A":
        dicfreq[i.split()[1]]["A"] = 1-float(i.split()[4])
        dicfreq[i.split()[1]]["G"] = float(i.split()[4])
    else:
        dicfreq[i.split()[1]]["A"] = float(i.split()[4])
        dicfreq[i.split()[1]]["G"] = 1- float(i.split()[4])
    
pathwaybedfile= open(pathwaybedfilename,"r")
pathwaybedfilelist =   pathwaybedfile.readlines()
pathwaybedfile.close()

for i in pathwaybedfilelist:
    pathchr = i.split()[0]
    pathst = int(i.split()[1])
    pathed = int(i.split()[2])
    if i.find("main") != -1:
        drawchr = pathchr
    else:
        drawchr = pathchr +"_"+str(pathst)+"_"+str(pathed)
    for j in dicfreq.keys():
        freqchr = j.split("_")[0]
        freqpoi  = int(j.split("_")[1])
        if freqchr==pathchr and pathst < freqpoi < pathed:
            print(freqchr,freqpoi-50,freqpoi+50,drawchr, dicfreq[j]["A"],populationmark)

