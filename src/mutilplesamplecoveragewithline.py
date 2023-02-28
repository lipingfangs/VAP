import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from src.drawline import *
def mutilplesamplecoveragewithline(coveragebedfilename,dictracks,mutilplesamplecolor,maintracklength,anncolor):
    #import drawline
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    populationfrequencybedrectedlist = []
    dicsamplesreadbottomtemp = {}
    samplesreadbottomtemplist =[]
    countsample = 0
    donerunsample = []
    readbottomtemplist = []
    trackstartlist = []
    textwithdraw = maintracklength/100 
    dicfrequencyscores = {}
    trackstartandbottomlist = [] #accelerate the cycle, get rid of unnecessary
    coffcallist = []
    #dictrackbottomlist = {}
    for i in coveragefileline:
        #print(i)
        samplename = i.split()[5]
        if samplename not in  samplesreadbottomtemplist:
            samplesreadbottomtemplist.append(samplename)
            dicsamplesreadbottomtemp[samplename] =  [countsample,mutilplesamplecolor[countsample]]
            countsample += 1
        coffcallist.append(float(i.split()[4]))
   # print(samplesreadbottomtemplist)
    #print(dicsamplesreadbottomtemp)
    tempchrom = ""
    tempnowsamplename = ""
    tempscore = float(i.split()[4])
    coff = max(coffcallist) +1  
    for i in coveragefileline:
             
        samplename = i.split()[5]
        i =i.strip()
        chrom = i.split()[3]
        nowsamplename = dicsamplesreadbottomtemp[samplename][0]
        if chrom in dictracks.keys():
            readbottomtemp = dictracks[chrom][0] + 0.1 #+ dicsamplesreadbottomtemp[samplename][0]
            if [readbottomtemp,dictracks[chrom][2]] not in trackstartandbottomlist:
                trackstartandbottomlist.append([readbottomtemp,dictracks[chrom][2]])
           # if readbottomtemp not in readbottomtemplist:
                readbottomtemplist.append(readbottomtemp)
                #if dictracks[chrom][2] not in trackstartlist:
                trackstartlist.append(dictracks[chrom][2])
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])

        #drawcoverage       
            coveragescores =  float(i.split()[4]) * 1.5 /coff#*0.005
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart
            
            try:
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)].append(float(i.split()[4]))
            except:
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)] = [readbottomtemp]
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)].append(float(i.split()[4]))
            left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
            nowpoint = [readfordrawstart,coveragescores+bottom]
            if tempchrom == chrom and tempnowsamplename == nowsamplename:
                point = [temppoint,nowpoint]
                drawline(point,dicsamplesreadbottomtemp[samplename][1])
            #coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                           # fill=True,
                                           # color=dicsamplesreadbottomtemp[samplename][1],
                                           #linewidth=0.5) 
            #populationfrequencybedrectedlist.append(coveragerected)
            tempchrom = chrom
            tempnowsamplename = nowsamplename
            temppoint = nowpoint

    
    
    print(readbottomtemplist, trackstartlist)
    rulerlength = 5
    rulerheight = 1.5
    #trackstartlist = int(len(readbottomtemplist)/len(trackstartlist)) * trackstartlist
    
    #ruler of frequencey
    print(readbottomtemplist, trackstartlist,"ruler")
    for i in range(len(readbottomtemplist)): 
        left, bottom, width, height = (trackstartlist[i]-50 , readbottomtemplist[i],rulerlength,   rulerheight)
        coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        coveragerected=mpatches.Rectangle((left-5,bottom),width,height-0.75, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        plt.text(left-textwithdraw,bottom-0.05,"0",fontsize=8)
        coveragerected=mpatches.Rectangle((left-5,bottom+0.75),width,height-0.75, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        plt.text(left-textwithdraw,bottom+1.65,"1",fontsize=8)
        #plt.text("shahahs")
   # print(dicfrequencyscores)
    #difference annotation
    #for i in dicfrequencyscores.keys():
       # if len(dicfrequencyscores[i])>1:
           # if abs(dicfrequencyscores[i][1]-dicfrequencyscores[i][2])>0.2:
              #  left, bottom, width, height = (float(i.split("_")[0]), dicfrequencyscores[i][0]-0.6,float(i.split("_")[1]), 0.5) 
               # coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                      #          fill=True,
                               #                 color=anncolor,
                                     #          linewidth=0.5) 
            #    populationfrequencybedrectedlist.append(coveragerected)                
                
            
    
    return populationfrequencybedrectedlist,samplesreadbottomtemplist
