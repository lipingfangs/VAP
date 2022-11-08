import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def readcoveragebed(coveragebedfilename,dictracks,coveragecolor):
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    coveragerectedlist = []
    for i in coveragefileline:
        #print(i)
        i =i.strip()
        chrom = i.split()[3]
        readbottomtemp = dictracks[chrom][0] + 0.1
        readstart  =int(i.split()[1]) 
        readend =int(i.split()[2])
        coveragescores =  float(i.split()[4]) *0.02
        
        readforpathpointlength = readstart - dictracks[chrom][1] 
        readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
        readlength = readend - readstart
           
        left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
        coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=coveragecolor,
                                   linewidth=2) 
        coveragerectedlist.append(coveragerected)
    return coveragerectedlist

def mutilplesamplecoveragebed(coveragebedfilename,dictracks,mutilplesamplecolor):
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    coveragerectedlist = []
    dicsamplesreadbottomtemp = {}
    samplesreadbottomtemplist =[]
    countsample = 0
    for i in coveragefileline:
        #print(i)
        samplename = i.split()[5]
        if samplename not in  samplesreadbottomtemplist:
            samplesreadbottomtemplist.append(samplename)
            dicsamplesreadbottomtemp[samplename] =  [countsample,mutilplesamplecolor[countsample]]
            countsample += 1
    for j in dicsamplesreadbottomtemp.keys():    
        for i in coveragefileline:
            #print(i)
            samplename = i.split()[5]
            i =i.strip()
            chrom = i.split()[3]
            readbottomtemp = dictracks[chrom][0] + 0.1 + dicsamplesreadbottomtemp[j][0]
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])
            coveragescores =  float(i.split()[4]) *0.005
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart

            left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
            coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=dicsamplesreadbottomtemp[j][1],
                                       linewidth=2) 
            coveragerectedlist.append(coveragerected)
    return coveragerectedlist
