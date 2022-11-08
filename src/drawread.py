import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def sortread(readedistribution,readstart,readend,readbottomtemp):
    #print(readedistribution)
    mcount = 0
    while True:
        countn = 0
        mcount += 1
        for i in readedistribution:
            #print(countn)
            #print(len(readedistribution))
            haveusestart = int(i[0])
            haveuseend = int(i[1])
            haveusebottomtemp = float(i[2])
           # print( readbottomtemp,haveusebottomtemp)
            if readbottomtemp == haveusebottomtemp:
                #print("sa",countn)
                if  haveusestart <= readstart <=haveuseend or haveusestart <= readend<=haveuseend:
                    readbottomtemp += 0.2
                    break
            countn +=1
        if countn == len(readedistribution):
            #print(countn,len(readedistribution))
            readedistribution.append([readstart,readend,readbottomtemp])
            break
        if mcount > 8:
            break
    return readedistribution,readstart,readend,readbottomtemp


def readreadbed(readsbedfilename,dictracks,colors):
    readsbedfile = open(readsbedfilename,"r")
    readsbedfileline =   readsbedfile.readlines()
    readsbedfile.close()
    readbottom = [] 
    readheight = 0.1
    readtract = []
    dicpoireadchromosome = {}
    readedistribution = []
    #readnamelist  = {}
    dicposition = {}
    linepointpairendx = []
    linepointpairendy = []
    for i in readsbedfileline:
        readname = i.split()[3].split("/")[0]
        #print(readname)
        i = i.strip()
        #print(i)
        chrom = i.split()[0]
        if readname in list(dicpoireadchromosome.keys()): 
            #print("da")
            if chrom !=  dicpoireadchromosome[readname]:
                pairend = 1
            else:
                pairend = 0
        else:
            pairend = 0
            #print(readname)
            dicpoireadchromosome[readname] = chrom 
        if chrom in dictracks.keys():
            readbottomtemp = dictracks[chrom][0] + 0.1
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart
            readheight = 0.05
        else:
            continue

        readedistribution,readstart,readend,readbottomtemp = sortread(readedistribution,readstart,readend,readbottomtemp)
        #print(readfordrawstart, readbottomtemp,readlength,  readheight,"sas")  

        left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  readheight) 
        readrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=colors,
                                   linewidth=2) 
        readtract.append(readrected)
        
        if pairend == 1:
            linepointpairendxpoi = [dicposition[readname][0]+readlength,readfordrawstart]
            linepointpairendypoi = [dicposition[readname][1]+ readheight,readbottomtemp+ readheight]
            linepointpairendx.append(linepointpairendxpoi)
            linepointpairendy.append(linepointpairendypoi)
        dicposition[readname] = [readfordrawstart, readbottomtemp,readlength,  readheight]
    return readtract,linepointpairendx,linepointpairendy    
