import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pysam
import os

def readonlylargedeletion(dicseqtrack,bamdir,dicreaddetailinf,writethereadnameornot,mode):
    print(dicseqtrack,"dicseqtrack")
    varitionblocklist = []
    dicreaddetailinf_keys = set(dicreaddetailinf.keys())
    print("dicreaddetailinf_keys",dicreaddetailinf_keys)
    for i in os.listdir(bamdir):
        if i.find("bam") !=-1 and i.find("bai") ==-1 and i.find("regions") ==-1 and i.find("mosdepth") ==-1  :
            if i.find("main") != -1 or  i.find(":") != -1 :
                print(i)
                bf = pysam.AlignmentFile(bamdir+"/"+i,"r")
                for j in bf :
                    readname = j.qname
                    if mode == "long":
                        readname = "/".join(readname.split("/")[:-1])
                    if i.find("main") !=-1:
                        readchr = j.reference_name 
                    else:
                        chrpoiadd = i.split(":")[1].split(".")[0].split("-")
                        readchr = j.reference_name +"_" +chrpoiadd[0]+"_"+chrpoiadd[1]

                    readmarker = j.cigartuples
                    readseq = j.seq
                    if j.isize >= 0:
                        readdirection = "+"
                    else:
                        readdirection = "-"
                    readname += readdirection 
                    blankrefjump = 0
                    blankmappingjump = 0
                    maplength =0
                    scanedlength = 0
                    refjumpstep = 0
                   # print(readname)

                    if  readname in dicreaddetailinf_keys and readchr in dicseqtrack:

                    #if   readchr in dicseqtrack:
                        readstartpoint = j.pos+1
                        mapstart  = 0

                        for k in readmarker:
                            #print(k)
                            if k[0] == 0:
                                orgmapstart = mapstart-1
                                mapstart =  mapstart+blankmappingjump
                                maplength = k[1]
                                mapend = mapstart+maplength

                                #print("mapstart mapend",readseq,mapstart,mapend)
                                try:
                                    mapseq = readseq[mapstart:mapend]
                                except:
                                    break
                                if i.find("main") == -1:
                                    refstart = readstartpoint+orgmapstart-dicseqtrack[readchr][0] +  blankrefjump 
                                else:
                                    refstart = readstartpoint+orgmapstart+1-dicseqtrack[readchr][0] +  blankrefjump 
                                refend =  refstart+maplength
                                mapstart = mapend
                                scanedlength += maplength
                                
                            if k[0] == 4 or k[0] == 1:

                                blankmappingjump += k[1]
                                if k[0] == 1:
                                    refjumpstep =  k[1]
                                    if refjumpstep >1:
                                        plt.text(dicreaddetailinf[readname][0]+scanedlength,dicreaddetailinf[readname][1]-0.04,"Ins"+str(refjumpstep)+"bp",fontsize=0.75,color="green")
                                        left, bottom, width, height = (dicreaddetailinf[readname][0]+scanedlength, dicreaddetailinf[readname][1], k[1],  0.05) 
                                        varitionblock=mpatches.Rectangle((left,bottom),(width+3)/3,height, 
                                            fill=True,
                                            color="yellow",
                                           linewidth=2,
                                            edgecolor='black') 
                                        varitionblocklist.append(varitionblock)
                            if  k[0] == 2:                                
                                refjumpstep =  k[1]
                                blankrefjump += k[1]
                                if refjumpstep>1:
                                    plt.text(dicreaddetailinf[readname][0]+scanedlength,dicreaddetailinf[readname][1]-0.04,"Del"+str(refjumpstep)+"bp",fontsize=0.5,color="red")
                                    left, bottom, width, height = (dicreaddetailinf[readname][0]+scanedlength, dicreaddetailinf[readname][1], k[1],  0.05)
                                    varitionblock=mpatches.Rectangle((left,bottom),width,height, 
                                            linestyle='dotted',
                                            color="white",
                                           linewidth=2,
                                            edgecolor='black') 
                                    varitionblocklist.append(varitionblock)
                                    varitionblock=mpatches.Rectangle((left,bottom+0.020),width,0.01, 
                                            fill=True,
                                            color="black",
                                           linewidth=2) 
                                    varitionblocklist.append(varitionblock)
                                scanedlength +=  refjumpstep 
                                
    return varitionblocklist
