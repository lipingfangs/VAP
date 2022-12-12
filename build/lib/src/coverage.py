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
        if chrom not in dictracks.keys():
            continue
        readbottomtemp = dictracks[chrom][0] + 0.1
        readstart  =int(i.split()[1]) 
        readend =int(i.split()[2])
        coveragescores =  float(i.split()[4]) *0.01
        
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

