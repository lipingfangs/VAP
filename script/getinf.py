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

for i in genelistlorg:
    i = i.strip()
    if i.find(">") != -1:
        genelistl.append(i)
        if len(i.split()) <2:
            reflist.append(i[1:])
            
    

for i in genelistl:
     i = i.strip()
    if len(i.split()) >2:
        temp = i.strip().split()
        if i.find("<") !=-1:
            dicdirection[temp[0][1:]] = "Reverse"
        else:
            dicdirection[temp[0][1:]] = "Forward"
        i = i.replace(">","").replace("<","")
       # print(i)
        temp = i.strip().split()
        if temp[1].split(":")[0] in reflist and temp[2].split(":")[0] in reflist:
            chrMSU = temp[1].split(":")[0]
            #print(chrMSU)
            rangeMSU =  temp[1].split(":")[1] +"-"+ temp[2].split(":")[1]
            #print(rangeMSU)
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

for i in genelistlnotonelevel:
    temp = i.strip().split()
    posout = ""
    posoneout = ""
    postwoout = ""
    #if temp[1].find("MSU") == -1 or temp[2].find("MSU") == -1:
        #print(temp)
    if temp[1].split(":")[0] not in reflist:
        poshead = temp[1].split(":")[0]
        posone = int(temp[1].split(":")[1])
        for j in dicstin.keys():
            jchr  = j.split("_")[0]
            jst = int(j.split("_")[1])
            jed = int(j.split("_")[2])
            if jchr == poshead  and posone>jst and posone<jed:
                if temp[2].split(":")[0] in reflist:
                    posoneout += dicstin[j][0]  +","+  temp[2].split(":")[1]+","+dicstin[j][1]
                else:
                    posoneout += dicstin[j][0]  +","+dicstin[j][1]
                    
            
    if temp[2].split(":")[0] not in reflist:
        poshead = temp[2].split(":")[0]
        postwo = int(temp[2].split(":")[1])
        for j in dicstin.keys():
            jchr  = j.split("_")[0]
            jst = int(j.split("_")[1])
            jed = int(j.split("_")[2])
            if jchr == poshead and postwo>jst and postwo<jed:
                if temp[1].split(":")[0] in reflist:
                    postwoout += temp[1].split(":")[1] + "," + dicstin[j][0]+","+dicstin[j][1]
                else:
                    postwoout += dicstin[j][0]+","+dicstin[j][1]

    if postwoout == "" and    posoneout != "":
        dicstined[temp[0]] = posoneout
    elif postwoout != "" and    posoneout == "":
        dicstined[temp[0]] = postwoout
    elif postwoout != "" and    posoneout != "":
        dicstined[temp[0]] = posoneout+","+postwoout
        #break
        #print(dicstined)
#for i in dicstin.keys():
    #print(i,end = ",")
    #print(dicstin[i][0],end = ",")
    #print(dicstin[i][1])               
for i in    dicstined.keys():
    print(i,end = ",")
    print(dicstined[i],end = ",")
    print(dicdirection[i])
