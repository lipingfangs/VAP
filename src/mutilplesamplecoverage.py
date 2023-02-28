import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def mutilplesamplecoveragebed(coveragebedfilename,dictracks,mutilplesamplecolor):
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    coveragerectedlist = []
    dicsamplesreadbottomtemp = {}
    samplesreadbottomtemplist =[]
    countsample = 0
    donerunsample = []
    coffcallist = []
    for i in coveragefileline:
        #print(i)
        samplename = i.split()[5]
        if samplename not in  samplesreadbottomtemplist:
            samplesreadbottomtemplist.append(samplename)
            dicsamplesreadbottomtemp[samplename] =  [countsample,mutilplesamplecolor[countsample]]
            countsample += 1
        coffcallist.append(float(i.split()[4]))
        
                           
    coff = max(coffcallist) +1       
    for j in dicsamplesreadbottomtemp.keys():    
        print(j)
        for i in coveragefileline:
            #print(i)
            samplename = i.split()[5]
            if samplename in donerunsample:
                continue
            i =i.strip()
            chrom = i.split()[3]
            if  chrom not in dictracks.keys():
                continue
            readbottomtemp = dictracks[chrom][0] + 0.1 + dicsamplesreadbottomtemp[j][0]
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])
            coveragescores =  float(i.split()[4]) /coff
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart

            left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
            coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=dicsamplesreadbottomtemp[j][1],
                                       linewidth=2) 
            coveragerectedlist.append(coveragerected)
        donerunsample.append(samplename)
    return coveragerectedlist
