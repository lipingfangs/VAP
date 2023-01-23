from src.sortread import *
from src.sortreadnovel import *
def readreadbed(readsbedfilename,dictracks,colors,readsdirection):
    
    readsbedfile = open(readsbedfilename,"r")
    readsbedfileline =   readsbedfile.readlines()
    readsbedfile.close()
    readbottom = [] 
    readheight = 0.1
    readtract = []
    dicpoireadchromosome = {}
    layend = {}
    readedistribution = []
    #readnamelist  = {}
    dicposition = {}
    linepointpairendx = []
    linepointpairendy = []
    dicreaddetailinf = {}
    for i in readsbedfileline:
        readname = i.split()[3].split("/")[0]
        readdirection = i.split()[5]
        #print(readname)
        i = i.strip()
        #print(i)
        chrom = i.split()[0]

        if chrom in dictracks.keys():
            
            readbottomtemp = dictracks[chrom][0] + 0.1
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])
            if   readend - readstart>5000:
                continue
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart
            readheight = 0.05
        else:
            continue
        step = 0.075
        #readedistribution,readstart,readend,readbottomtemp,stopsignal = sortread(readedistribution,readstart,readend,readbottomtemp,step)
        layend,readstart,readend,readbottomtemp,stopsignal = sortreadnovel(layend,readstart,readend,readbottomtemp,step)

        #print(readfordrawstart, readbottomtemp,readlength,  readheight,"sas")  
       # print(readedistribution,readstart,readend,readbottomtemp,"sas")
        if stopsignal ==0:
            left, bottom, width, height  = (readfordrawstart, readbottomtemp,readlength,  readheight) 
            readrected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=colors,
                                       linewidth=1) 
            readtract.append(readrected)
            dicreaddetailinf[readname+i.split()[5]] = [readfordrawstart, readbottomtemp]
            #read direction
            if readsdirection ==1:
                if readdirection == "+":
                    directionrected=mpatches.Arrow(left+width/4,bottom+0.025,width/2, 0,
                                                fill=True,
                                                color="black"#,
                                               ,width=0.025,lw = 0.5)
                    readtract.append(directionrected)
                if readdirection == "-":
                    directionrected=mpatches.Arrow(left+width*3/4,bottom+0.025,-width/2, 0,
                                                fill=True,
                                                color="black"#,
                                               ,width=0.025,lw = 0.5)
                    readtract.append(directionrected)                
            
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
            
        if pairend == 1:
            linepointpairendxpoi = [dicposition[readname][0]+readlength,readfordrawstart]
            linepointpairendypoi = [dicposition[readname][1]+ readheight,readbottomtemp+ readheight]
            linepointpairendx.append(linepointpairendxpoi)
            linepointpairendy.append(linepointpairendypoi)
        dicposition[readname] = [readfordrawstart, readbottomtemp,readlength,  readheight]
    return readtract,linepointpairendx,linepointpairendy,dicreaddetailinf
