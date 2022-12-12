import sys
goin = sys.argv[1]
#goout = sys.argv[2]
#gooutfile=  open(goout,"w")
genelist = open(goin,"r")
genelistl = genelist.readlines()
genelist.close()
dicstin = {} 
dicstined ={}
for i in genelistl:
    i = i.strip().split()
    if i[1].find("MSU") != -1 and i[2].find("MSU") != -1:
        chrMSU = i[1].split(":")[0]
        #print(chrMSU)
        rangeMSU =  i[1].split(":")[1] +"-"+ i[2].split(":")[1]
        #print(rangeMSU)
        dicstin[i[0]] = [rangeMSU,chrMSU]

print("#MSUdone")
#print(dicstin)

for i in dicstin.keys():
    print(i,end = ",")
    print(dicstin[i][0],end = ",")
    print(dicstin[i][1])

for i in genelistl:
    temp = i.strip().split()
    posout = ""
    posoneout = ""
    postwoout = ""
    #if temp[1].find("MSU") == -1 or temp[2].find("MSU") == -1:
        #print(temp)
    if temp[1].find("MSU") == -1:
        poshead = temp[1].split(":")[0]
        posone = int(temp[1].split(":")[1])
        for j in dicstin.keys():
            jchr  = j.split("_")[0]
            jst = int(j.split("_")[1])
            jed = int(j.split("_")[2])
            if jchr == poshead  and posone>jst and posone<jed:
                if temp[2].find("MSU") != -1:
                    posoneout += dicstin[j][0]  +","+  temp[2].split(":")[1]+","+dicstin[j][1]
                else:
                    posoneout += dicstin[j][0]  +","+dicstin[j][1]
                    
            
    if temp[2].find("MSU") == -1:
        poshead = temp[2].split(":")[0]
        postwo = int(temp[2].split(":")[1])
        for j in dicstin.keys():
            jchr  = j.split("_")[0]
            jst = int(j.split("_")[1])
            jed = int(j.split("_")[2])
            if jchr == poshead and postwo>jst and postwo<jed:
                if temp[1].find("MSU") != -1:
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
    print(dicstined[i])

