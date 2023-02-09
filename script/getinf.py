#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @name   : freqacq.py
# @author : cat
# @date   : 2023/2/8.
def locatetomsuornot(a,runlist, refchrlist):
    
    if a.split(":")[0] in refchrlist:
        #print(a,end = ",")
        #print("done")
        vrdlist.append(a)
        vrdlist.append(a)
        return a

    else:
        achr= a.split(":")[0]
        aloc = int(a.split(":")[1])
        for i in runlist:
            i = i.split()
            inschr  = i[0].split("_")[0]
            insst = int(i[0].split("_")[1])
            insed = int(i[0].split("_")[2])
            poshead =  i[1]
            postail=  i[2]
            posheadchr = poshead.split(":")[0]
            postailchr = postail.split(":")[0]
            if inschr ==  achr  and aloc>insst and aloc<insed:
                vrdlist.append(i[0])
                if posheadchr in refchrlist and  postailchr  in refchrlist:
                    vrdlist.append(poshead)#,postail,end = ",")
                    vrdlist.append(postail) #print("done")
                    return a             
                else:
                    if posheadchr not in refchrlist and postailchr  in refchrlist:
                        #print("tail",postail,end = ",")
                        vrdlist.append(postail)
                        a = locatetomsuornot(poshead,runlist, refchrlist)
                    if postailchr not in refchrlist and posheadchr in refchrlist:
                        vrdlist.append(poshead)
                        #print("tail",poshead,end = ",")
                        a = locatetomsuornot(postail,runlist, refchrlist)
                    if postailchr not in refchrlist and posheadchr not in refchrlist:
                        a = locatetomsuornot(poshead,runlist, refchrlist)
                        a = locatetomsuornot(postail,runlist, refchrlist)

                    

def sortlocus(vrdlist,headerortail,refchrlist):  
    sortpoi = []
    #print(vrdlist)
    for i in vrdlist[1:]:
        if i.split(":")[0] in refchrlist:
            sortpoi.append(i.split(":")[1])
            chrn = i.split(":")[0]
    if headerortail  == "head":       
        return min(sortpoi), chrn
    else:
        return max(sortpoi), chrn
    

import sys
goin = sys.argv[1]
#reflistfilename  = sys.argv[2]

#goout = sys.argv[2]
#gooutfile=  open(goout,"w")
genelist = open(goin,"r")
genelistlorg = genelist.readlines()
genelist.close()



genelistl = []
dicstin = {} 
dicstined ={}
dicdirection = {}
reflist= []
genelistlnotonelevel = []
genecleanlist =[]
for i in genelistlorg:
    i = i.strip()
    if i.find(">") != -1:
        genelistl.append(i)
        if len(i.split()) <2:
            reflist.append(i[1:])
            
    

for i in genelistl:
    i = i.strip()
    if len(i.split()) >2:
       # templine = ""
        #templine = "_".join(temp[0].split("_")[:-2])
        temp = i.strip().split()
        templine = ""
        templine = "_".join(temp[0].split("_")[:-2])        
        temp[0] = templine+","+temp[0].split("_")[-2]+","+temp[0].split("_")[-1]
        if i.find("<") !=-1:
            dicdirection[temp[0][1:]] = "Reverse"
        else:
            dicdirection[temp[0][1:]] = "Forward"
        i = i.replace(">","").replace("<","")
        genecleanlist.append(i)
       # print(i)
        temp = i.strip().split()
        if temp[1].split(":")[0] in reflist and temp[2].split(":")[0] in reflist:
            chrMSU = temp[1].split(":")[0]
            #print(chrMSU)
            rangeMSU =  temp[1].split(":")[1] +","+ temp[2].split(":")[1]
            #print(rangeMSU)
            templine = ""
            templine = "_".join(temp[0].split("_")[:-2])
                
            temp[0] = templine+","+temp[0].split("_")[-2]+","+temp[0].split("_")[-1]
            dicstin[temp[0]] = [rangeMSU,chrMSU]
        else:
            genelistlnotonelevel.append(i)

print("#MSUdone")
#print(dicstin)


for i in dicstin.keys():
    print(i,end = ",")
    print(dicstin[i][0],end = ",")
    print(dicstin[i][1],end = ",")
    print(dicdirection[i])
          
#print("#onlyonelevel done")  
          

#print("Chr10Basmati1genomefa:130859",end=",")


for i in genelistlnotonelevel:
    c = 0
    fourlist = ["","","","","",""]
    #print(i)
    for j in i.split()[1:]:
        
        #print(j)
        c +=1
        vrdlist = []
        locatetomsuornot(j,genecleanlist,reflist)
        if vrdlist == []:
            donout ="yes"
            break
        else:
            donout ="no"
            
        if c ==1:
            poi,chrn = sortlocus(vrdlist,"head",reflist)
            directpro = vrdlist[0]
            fourlist[0] = poi
            fourlist[2] = chrn
            fourlist[3] = "Forward"
            fourlist[4] = directpro +","+j.split(":")[1]
            
        else:
            poi,chrn = sortlocus(vrdlist,"tail",reflist)
            directpro = vrdlist[0]
            fourlist[1] = poi 
            fourlist[5] = directpro +","+j.split(":")[1]
            
    clist = i.split()[0].split("_")
    cl = 0
    printlist = clist+fourlist
    if donout != "yes":
        for i in printlist:
            cl +=1
            if cl == len(printlist):
                print(i)
            else:
                print(i,end = ",")
