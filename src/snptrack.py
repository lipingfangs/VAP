def snptrack(pathwaybedfilename,middlethetrackandread,panfa):
    #read sequence
    panfafile =  open(panfa,"r")
    panfafilelist =   panfafile.readlines()
    panfafile.close()
    dicfa = {}
    phaseseq = ""
    for i in  panfafilelist:
        i = i.strip()
        if i.startswith(">"):
            dicfa[i[1:].split()[0]] = ""
            temp = i[1:].split()[0]
        else:
            dicfa[temp] += i
    dicseqtrack ={}
    #read track
    readpathwaybedfile = open(pathwaybedfilename,"r")
    readpathwaybedfileline =   readpathwaybedfile.readlines()
    readpathwaybedfile.close()
    pathwaytracks  = []
    mainbottom = 4.75
    pathwaybottom = 1.75
    pathwaybottomlist = [4.75]
    for i in readpathwaybedfileline:
        i = i.strip()
        probe = i.split()[3]
        if probe == "main":
            maintrackname = i.split()[0]
            maintrackstart =  int(i.split()[1])
            maintrackend = int(i.split()[2])
            refseq = dicfa[maintrackname][maintrackstart-1: maintrackend]
            maintrackstartsnp = maintrackstart-1
            for j in  refseq:
                plt.text(maintrackstartsnp,mainbottom+0.45,j,fontsize=0.2,color="white")
                maintrackstartsnp +=1
            dicseqtrack[maintrackname] = [int(i.split()[1]),refseq,mainbottom]
        else:
            #continue
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            print(pathwaytrackname)
            pathwaystart = int(i.split()[1])
            pathwaylength = int(i.split()[2])- int(i.split()[1])
            pathwaystartinmain = int(i.split()[3].split("-")[1])
            pathwayendinmain = int(i.split()[3].split("-")[2])
            pathwayseq =  dicfa[pathwaytrackname]
            #print(pathwayseq)
            while True:
                if pathwaybottom not in pathwaybottomlist:
                    pathwaybottomlist.append(pathwaybottom)
                    break
                else:
                    pathwaybottom = pathwaybottom+3
            #dicpathwaybottom[pathwaytrackname] = pathwaybottom
            if middlethetrackandread == 1:
                pathwaystartinmaintemp = pathwaystartinmain - (pathwaylength/2)
                comback = pathwaystartinmain -  pathwaystartinmaintemp
                nobackpathwayendinmain =  pathwayendinmain
                pathwayendinmain = pathwayendinmain - comback 
                pathwaystartinmain = pathwaystartinmaintemp
            else:
                comback= 0
            #plt.text(pathwaystartinmain, pathwaybottom, pathwayseq,fontsize=1)
            pathwaystartinmainsnp = pathwaystartinmain
            for j in pathwayseq:
                plt.text(pathwaystartinmainsnp,pathwaybottom+0.45,j,fontsize=0.2,color="white")
                pathwaystartinmainsnp +=1
            dicseqtrack[pathwaytrackname] = [int(i.split()[1]),pathwayseq, pathwaybottom]
    return dicseqtrack
