def snptrack(pathwaybedfilename,dictracks,middlethetrackandread,panfadic,tracksnpornot):
    #read sequence
    #panfafile =  open(panfa,"r")
   # panfafilelist =   panfafile.readlines()
    #panfafile.close()
    dicfa = panfadic
    phaseseq = ""
    branchdistribution = []
   # for i in  panfafilelist:
       # i = i.strip()
        #if i.startswith(">"):
           #dicfa[i[1:].split()[0]] = ""
          #  temp = i[1:].split()[0]
       # else:
           # dicfa[temp] += i
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
            
            maintrackstartsnp = maintrackstart-1
            if tracksnpornot ==0 :
                dicseqtrack[maintrackname] = [int(i.split()[1]),"none",mainbottom]
                continue
            refseq = dicfa[maintrackname][maintrackstart-1: maintrackend]
            for j in  refseq:
                plt.text(maintrackstartsnp,dictracks[maintrackname][0]-0.05,j,fontsize=0.01,color="white")
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
            
            #print(pathwayseq)
     
            #dicpathwaybottom[pathwaytrackname] = pathwaybottom
            if middlethetrackandread == 1:
                print(pathwaystartinmain, pathwayendinmain,pathwaylength,"org")
                pathwaymainmiddle = (pathwaystartinmain +  pathwayendinmain)/2
                pathwaymiddle = (pathwaystartinmain +  pathwaystartinmain+pathwaylength)/2
                
                print(pathwaymainmiddle, pathwaymiddle,"middlepoint")
                comback =pathwaymainmiddle - pathwaymiddle 
                print(comback,"comback")
                pathwaystartinmaintemp = pathwaystartinmain + comback
                #comback = pathwaymiddle-  pathwaymainmiddle
                nobackpathwayendinmain =  pathwayendinmain
                pathwayendinmain = pathwayendinmain + comback 
                pathwaystartinmain = pathwaystartinmaintemp
                print(pathwaystartinmain,"finishchange")
            
                
            #if middlethetrackandread == 1:
               # pathwaystartinmaintemp = pathwaystartinmain - (pathwaylength/2)
               # comback = pathwaystartinmain -  pathwaystartinmaintemp
                #nobackpathwayendinmain =  pathwayendinmain
                #pathwayendinmain = pathwayendinmain - comback 
                #pathwaystartinmain = pathwaystartinmaintemp
            else:
                comback= 0
            pathwaysmainend = pathwaystartinmain+pathwaylength
            #plt.text(pathwaystartinmain, pathwaybottom, pathwayseq,fontsize=1)
            if tracksnpornot ==0 :
                dicseqtrack[pathwaytrackname] = [int(i.split()[1]),"none",pathwaybottom]
                continue
            pathwayseq =  dicfa[pathwaytrackname]
            #branchdistribution,pathwaystartinmain,pathwaysmainend,pathwaybottom,stopsignal = sortread(branchdistribution,pathwaystartinmain,pathwaysmainend,pathwaybottomtemp,3)    
            pathwaystartinmainsnp = pathwaystartinmain
            for j in pathwayseq:
                plt.text( pathwaystartinmainsnp,dictracks[pathwaytrackname][0]-0.05,j,fontsize=0.05,color="black")
                pathwaystartinmainsnp +=1
            dicseqtrack[pathwaytrackname] = [int(i.split()[1]),"none", pathwaybottom]
    return dicseqtrack
