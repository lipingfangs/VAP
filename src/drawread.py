from src.sortreadnovel import *
import pysam
import json

def extract_node_id(filename):
    nodelist = []
    node_ids = []

    with open(filename, 'r') as file:
        for line in file.readlines():
            json_object = json.loads(line)
            mappings = json_object.get('path', {}).get('mapping', [])
            name =  json_object.get('name')
            node_ids = [name]
            for mapping in mappings:
                node_ids.append(mapping.get('position', {}).get('node_id'))
          #  print(node_ids)
            count = 2
            if len(node_ids) > 2:
                for i in node_ids[1:-1]:
                   # print()
                    if abs(int(node_ids[count]) - int(i)) > 10:
                        nodelist.append(node_ids[0])#,node_ids[count],i])
                        break 
                    count +=1
            node_ids = []
            #print()
    return nodelist

def readreadbed(readsbedfilename,dictracks,colors,readsdirection,mode,jsonfile,maintrackname):#,wholebam):
    print(dictracks,"dictracks enter")
    readsbedfile = open(readsbedfilename,"r")
    readsbedfileline =   readsbedfile.readlines()
    readsbedfile.close()
    readbottom = [] 
    readheight = 0.1
    readtract = []
    dicpoireadchromosome = {}
    layend = {}
    readedistribution = []
    dicposition = {}
    linepointpairendx = []
    linepointpairendy = []
    linepointsplitreadx = []
    linepointsplitready = []
    dicreaddetailinf = {}
    
    readchrtemp  = ""
    if mode == "gam":
        spiltreadlist = extract_node_id(jsonfile)
    for i in readsbedfileline:
        split_i = i.split()
        readchr =  split_i[0]
        if i.split()[3].find("/") != -1:
            readname = "/".join(i.split()[3].split("/")[:-1])
        else:
            readname = i.split()[3]
        if  readchrtemp  != readchr:
            layend = {}
            readchrtemp =  readchr 
        readdirection = split_i[5]
        i = i.strip()
        chrom = split_i[0]
   
        if chrom in dictracks.keys():
            dictracks_chrom = dictracks[chrom]
            readbottomtemp = dictracks_chrom[0] + 0.1
            readstart  =int(split_i[1]) 
            readend =int(split_i[2])
            if mode == "short":
                if   readend - readstart>5000:
                    continue
            readforpathpointlength = readstart - dictracks_chrom[1] 
            readfordrawstart= dictracks_chrom[2] + readforpathpointlength 
            

            readlength = readend - readstart
            readheight = 0.05
            readfordrawend = readfordrawstart + readlength
        else:
            continue
        step = 0.075
        layend,readfordrawend,readfordrawend,readbottomtemp,stopsignal = sortreadnovel(layend,readfordrawstart,readfordrawend,readbottomtemp,step)
        if maintrackname != chrom and readfordrawstart < dictracks_chrom[2]:
            readfordrawstart = dictracks_chrom[2] 
            print(readfordrawstart,dictracks_chrom[2] )
        
        if maintrackname != chrom:# and readfordrawend >dictracks_chrom[2]+:
            tracklength = int(chrom.split("_")[2]) - int(chrom.split("_")[1])
            dictracksend = dictracks_chrom[2]+tracklength
            if readfordrawend >dictracksend:
                print(readfordrawend,dictracksend ) 
                readfordrawend = dictracksend 
                readlength =   readfordrawend - readfordrawstart     
        if stopsignal ==0:
            left, bottom, width, height  = (readfordrawstart, readbottomtemp,readlength, readheight) 
            readrected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=colors,
                                       linewidth=1) 
            readtract.append(readrected)
            #print("stopsignal",readname+split_i[5],readfordrawstart, readbottomtemp)
            if not dicreaddetailinf.get(readname+split_i[5]):
                dicreaddetailinf[readname+split_i[5]] = [readfordrawstart, readbottomtemp,chrom,readfordrawstart+readlength]
            else:
                temp = dicreaddetailinf[readname+split_i[5]]
                dicreaddetailinf[readname+split_i[5]] = [readfordrawstart, readbottomtemp,chrom,readfordrawstart+readlength]+ temp
          #      tempcount = 1
            if not dicreaddetailinf.get(readname):
                dicreaddetailinf[readname] = [readfordrawstart, readbottomtemp,chrom,readfordrawstart+readlength]
            else:
                temp = dicreaddetailinf[readname]
                dicreaddetailinf[readname] = [readfordrawstart, readbottomtemp,chrom,readfordrawstart+readlength]+ temp
          #      tempcount = 1  #  while True:
                   # tempcountstr = str(tempcount)
              #      if not dicreaddetailinf.get(readname+split_i[5]+tempcountstr):
                       # tempcount += 1
               #     else:
                       # dicreaddetailinf[readname+split_i[5]+tempcountstr] =  [readfordrawstart, readbottomtemp,chrom,readfordrawstart+readlength]
                        #break

            
            if readsdirection ==1:
               # if readdirection == "+":
                #    directionrected=mpatches.Arrow(left+width/4,bottom+0.025,width/2, 0,
                    #                            fill=True,
                  #                              color="black",
                   #                            width=0.025,lw = 0.5)
                 #   readtract.append(directionrected)
                if readdirection == "-":
                    directionrected=mpatches.Rectangle((left,bottom),width,height,
                                                fill=True,
                                                color="#808080",
                                               linewidth=1) 
                    readtract.append(directionrected)     
                    
        if readname not in list(dicposition.keys()):
            dicposition[readname] = [[readfordrawstart, readbottomtemp,readlength,  readheight,readchr]]
            pairend = 0
        else:
            dicposition[readname].append([readfordrawstart, readbottomtemp,readlength,  readheight,readchr])
            if readbottomtemp != dicposition[readname][0][1]:
                pairend = 1
            else:
                pairend = 0
                
                
            
            
       # if readname in list(dicpoireadchromosome.keys()): 
         #   if chrom !=  dicpoireadchromosome[readname]:
             #   pairend = 1
         #   else:
              #  pairend = 0
     #   else:
           # pairend = 0
           # dicpoireadchromosome[readname] = chrom         
        #print(dicposition.keys(),readname,pairend)
       
        #dicposition[readname] = [readfordrawstart, readbottomtemp,readlength,  readheight]
        if pairend == 1:
            if dicposition[readname][0][4] != readchr:
            #dicposition_readname = dicposition[readname]
                linepointpairendxpoi = [dicposition[readname][0][0]+readlength,readfordrawstart]
                linepointpairendypoi = [dicposition[readname][0][1]+ readheight,readbottomtemp+ readheight]
                linepointpairendx.append(linepointpairendxpoi)
                linepointpairendy.append(linepointpairendypoi)
            
        
        
        if mode == "gam" and pairend == 1:
            #spiltreadlist = extract_node_id(jsonfile)
            #print(spiltreadlist)
            if readname in  spiltreadlist:
             #    print(readname,dicposition[readname])
                #readname = readpair[0]
                #dicposition_readname = dicposition[readname]
                linepointsplitreadxpoi = [dicposition[readname][0][0]+readlength,readfordrawstart]
                linepointsplitreadypoi = [dicposition[readname][0][1]+ readheight,readbottomtemp+ readheight]
                linepointsplitreadx.append(linepointsplitreadxpoi)
                linepointsplitready.append(linepointsplitreadypoi)
               
     #   dicposition[readname] = [readfordrawstart, readbottomtemp,readlength,  readheight]
                
    #print("dicreaddetailinf")    
   # print(dicreaddetailinf)
    for i in  dicreaddetailinf.keys():
        if len(dicreaddetailinf[i]) > 5:
            continue
            #print("dicreaddetailinf",i,dicreaddetailinf[i])
    return readtract,linepointpairendx,linepointpairendy,dicreaddetailinf,linepointsplitreadx,linepointsplitready
