import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def readpathwaybed(pathwaybedfilename,drawtrackcolor,middlethetrackandread):
    dictracks = {}
    drawmaintrackcolor = drawtrackcolor[0]
    drawpathwaytrackcolor = drawtrackcolor[1]
    readpathwaybedfile = open(pathwaybedfilename,"r")
    readpathwaybedfileline =   readpathwaybedfile.readlines()
    readpathwaybedfile.close()
    pathwaytracks  = []
    mainbottom = 4.75
    pathwaybottom = 1.75
    pathwaybottomlist = [4.75]
    linepointx = []
    linepointy = []
    dicpathwaybottom = {}
    for i in readpathwaybedfileline:
        i = i.strip()
        probe = i.split()[3]
        if probe == "main":
            maintrackname = i.split()[0]
            maintrackstart =  int(i.split()[1])
            maintrackend = int(i.split()[2])
            mainlength = maintrackend- maintrackstart
            
            sizetrackx = [[maintrackstart,maintrackend],[maintrackstart,maintrackstart]] #the page size placeholder
            sizetracky = [[0,0],[0,10]]
            left, bottom, width, height = (maintrackstart, mainbottom,mainlength, 0.5)
            mainrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=drawmaintrackcolor,
                                   linewidth=2)    
            maintrack = mainrected
            
            dictracks[maintrackname] = [mainbottom+0.5,maintrackstart,maintrackstart]
        else:
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            print(pathwaytrackname)
            pathwaystart = int(i.split()[1])
            pathwaylength = int(i.split()[2])- int(i.split()[1])
            pathwaystartinmain = int(i.split()[3].split("-")[1])
            pathwayendinmain = int(i.split()[3].split("-")[2])
            #print(pathwaystart)
            while True:
                if pathwaybottom not in pathwaybottomlist:
                    pathwaybottomlist.append(pathwaybottom)
                    break
                else:
                    pathwaybottom = pathwaybottom+3
            dicpathwaybottom[pathwaytrackname] = pathwaybottom
            if middlethetrackandread == 1:
                pathwaystartinmaintemp = pathwaystartinmain - (pathwaylength/2)
                comback = pathwaystartinmain -  pathwaystartinmaintemp
                nobackpathwayendinmain =  pathwayendinmain
                pathwayendinmain = pathwayendinmain - comback 
                pathwaystartinmain = pathwaystartinmaintemp
            else:
                comback= 0
                
            left, bottom, width, height = (pathwaystartinmain, pathwaybottom,pathwaylength, 0.5)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=drawpathwaytrackcolor,
                                   linewidth=2) 
            pathwaytracks.append(pathwayrected)
            #pathwayinsertion location
            left, bottom, width, height = (nobackpathwayendinmain, 4.65,mainlength/500, 0.5)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color="red",
                                   linewidth=2) 
            pathwaytracks.append(pathwayrected)            
            if pathwaybottom >5:
                mainwaysurface = 5.25
            else:
                mainwaysurface = 4.75
            linepointx1 = [pathwaystartinmain+comback ,pathwaystartinmain] #for the insert posistion
            if pathwaybottom <4.75:
                linepointy1 = [mainwaysurface  ,pathwaybottom+0.5]
            else:
                linepointy1 = [mainwaysurface  ,pathwaybottom]
            linepointx.append(linepointx1)
            linepointy.append(linepointy1)
            
            linepointx2 = [pathwayendinmain+comback,pathwaystartinmain+pathwaylength] 
            if pathwaybottom <4.75:
                linepointy2 = [mainwaysurface  ,pathwaybottom+0.5]
            else:
                linepointy2 = [mainwaysurface  ,pathwaybottom]            
            
            linepointx.append(linepointx2)
            linepointy.append(linepointy2)
            
            dictracks[pathwaytrackname] = [pathwaybottom+0.5,pathwaystart,pathwaystartinmain]
    print()        
    return sizetrackx, sizetracky, maintrack, pathwaytracks, linepointx, linepointy, dictracks,dicpathwaybottom,mainlength

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
    dicreaddetailinf = {}
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

        readedistribution,readstart,readend,readbottomtemp,stopsignal = sortread(readedistribution,readstart,readend,readbottomtemp)
        #print(readfordrawstart, readbottomtemp,readlength,  readheight,"sas")  
        
        if stopsignal ==0:
            left, bottom, width, height  = (readfordrawstart, readbottomtemp,readlength,  readheight) 
            readrected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=colors,
                                       linewidth=1) 
            readtract.append(readrected)
            dicreaddetailinf[readname+i.split()[5]] = [readfordrawstart, readbottomtemp]
            
        if pairend == 1:
            linepointpairendxpoi = [dicposition[readname][0]+readlength,readfordrawstart]
            linepointpairendypoi = [dicposition[readname][1]+ readheight,readbottomtemp+ readheight]
            linepointpairendx.append(linepointpairendxpoi)
            linepointpairendy.append(linepointpairendypoi)
        dicposition[readname] = [readfordrawstart, readbottomtemp,readlength,  readheight]
    return readtract,linepointpairendx,linepointpairendy,dicreaddetailinf

def sortread(readedistribution,readstart,readend,readbottomtemp):   
    stopsignal = 0
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
                    readbottomtemp += 0.075
                    break
            countn +=1
        if countn == len(readedistribution):
            #print(countn,len(readedistribution))
            readedistribution.append([readstart,readend,readbottomtemp])
            break
        if mcount > 15:
            stopsignal = 1
            break
    return readedistribution,readstart,readend,readbottomtemp,stopsignal


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
        readbottomtemp = dictracks[chrom][0] + 0.1
        readstart  =int(i.split()[1]) 
        readend =int(i.split()[2])
        coveragescores =  float(i.split()[4]) *0.02
        
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

def mutilplesamplecoveragebed(coveragebedfilename,dictracks,mutilplesamplecolor):
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    coveragerectedlist = []
    dicsamplesreadbottomtemp = {}
    samplesreadbottomtemplist =[]
    countsample = 0
    for i in coveragefileline:
        #print(i)
        samplename = i.split()[5]
        if samplename not in  samplesreadbottomtemplist:
            samplesreadbottomtemplist.append(samplename)
            dicsamplesreadbottomtemp[samplename] =  [countsample,mutilplesamplecolor[countsample]]
            countsample += 1
    for j in dicsamplesreadbottomtemp.keys():    
        for i in coveragefileline:
            #print(i)
            samplename = i.split()[5]
            i =i.strip()
            chrom = i.split()[3]
            readbottomtemp = dictracks[chrom][0] + 0.1 + dicsamplesreadbottomtemp[j][0]
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])
            coveragescores =  float(i.split()[4]) *0.005
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart

            left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
            coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=dicsamplesreadbottomtemp[j][1],
                                       linewidth=2) 
            coveragerectedlist.append(coveragerected)
    return coveragerectedlist

def cutpathwayreliablebed(pathwaybedfilename,dicpathwaybottom,anncolor,middlethetrackandread):
    dictracks = {}
    readpathwaybedfile = open(pathwaybedfilename,"r")
    readpathwaybedfileline =   readpathwaybedfile.readlines()
    readpathwaybedfile.close()
    annpathwaytracks  = []
    mainbottom = 4.75
    pathwaybottom = 1.75
    pathwaybottomlist = [4.75]
    linepointx = []
    linepointy = []
    annmaintracksublist = []
    for i in readpathwaybedfileline:
        i = i.strip()
        probe = i.split()[3]
        if probe == "mainsubreliable":
            maintrackname = i.split()[0]
            maintrackstart =  int(i.split()[1])
            maintrackend = int(i.split()[2])
            mainlength = maintrackend- maintrackstart
            
            left, bottom, width, height = (maintrackstart, mainbottom,mainlength, 0.5)
            mainrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=anncolor,
                                   linewidth=2)    
            annmaintracksublist.append(mainrected)
            
            dictracks[maintrackname] = [mainbottom+0.5,maintrackstart,maintrackstart]
        else:
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            print(pathwaytrackname)
            pathwaystart = int(i.split()[1])
            pathwaylength = int(i.split()[2])- int(i.split()[1])
            pathwaystartinmain = int(i.split()[3].split("-")[1])
            pathwayendinmain = int(i.split()[3].split("-")[2])
            #print(pathwaystart)
            pathwaybottom = dicpathwaybottom[pathwaytrackname]
            print(pathwaybottom)
            if middlethetrackandread == 1:
                pathwaystartinmain = pathwaystartinmain - (pathwaylength/2)
            left, bottom, width, height = (pathwaystartinmain, pathwaybottom,pathwaylength, 0.5)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=anncolor,
                                   linewidth=2) 
            annpathwaytracks.append(pathwayrected)
            if pathwaybottom >5:
                mainwaysurface = 5.25
            else:
                mainwaysurface = 4.75
            linepointx1 = [pathwaystartinmain ,pathwaystartinmain]
            linepointy1 = [mainwaysurface  ,pathwaybottom]
            linepointx.append(linepointx1)
            linepointy.append(linepointy1)
            
            linepointx2 = [pathwayendinmain,pathwaystartinmain+pathwaylength] 
            linepointy2 = [mainwaysurface ,pathwaybottom]
            linepointx.append(linepointx2)
            linepointy.append(linepointy2)
            dictracks[pathwaytrackname] = [pathwaybottom+0.5,pathwaystart,pathwaystartinmain]
    
    return annmaintracksublist, annpathwaytracks, linepointx, linepointy, dictracks

def geneannbed(genebedfilename,dictracks,genecolors):
    genebedfile = open(genebedfilename,"r")
    genebedfileline =  genebedfile.readlines()
    genebedfile.close()
   # print(dictracks.keys())

    genebottom = [] 
    geneheight = 0.1
    genetract = []
    genenamelist = []
    genenamepoilist = []
    dicpoigenechromosome = {}    
    for i in genebedfileline:  
        i = i.strip()
        #print(i)
        genename =  i.split()[3]
        genenamelist.append(genename)
        i = i.strip()
        chrom = i.split()[0]
        if chrom in dictracks.keys():
            genebottomtemp = dictracks[chrom][0] - 1
            genestart  =int(i.split()[1]) 
            geneend =int(i.split()[2])
            geneforpathpointlength = genestart - dictracks[chrom][1] 
            genefordrawstart= dictracks[chrom][2] + geneforpathpointlength 
            genelength = geneend - genestart
        else:
            continue
        if  i.split()[4] == "-":
            left, bottom, width, height = (genefordrawstart, genebottomtemp+0.1,-genelength,  geneheight) 
        else:
            left, bottom, width, height = (genefordrawstart, genebottomtemp+0.1,genelength,  geneheight) 
        generected=mpatches.Arrow(left,bottom,width,0, 
                                    #fill=True,
                                    color=genecolors#,
                                   ,width=0.5,lw = 0.5) 
        genetract.append(generected)
        genenamex = genefordrawstart#+genelength
        genenamey = genebottomtemp+0.25
        genenamepoilist.append([genenamex,genenamey])
    return genetract, genenamelist, genenamepoilist

def populationfrequencybed(coveragebedfilename,dictracks,mutilplesamplecolor,maintracklength,anntrack,anncolor):
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    populationfrequencybedrectedlist = []
    dicsamplesreadbottomtemp = {}
    samplesreadbottomtemplist =[]
    countsample = 0
    donerunsample = []
    readbottomtemplist = []
    trackstartlist = []
    textwithdraw = maintracklength/100 
    dicfrequencyscores = {}
    for i in coveragefileline:
        #print(i)
        samplename = i.split()[5]
        if samplename not in  samplesreadbottomtemplist:
            samplesreadbottomtemplist.append(samplename)
            dicsamplesreadbottomtemp[samplename] =  [countsample,mutilplesamplecolor[countsample]]
            countsample += 1
   # print(samplesreadbottomtemplist)
    #print(dicsamplesreadbottomtemp)
    for i in coveragefileline:
             
        samplename = i.split()[5]
        i =i.strip()
        chrom = i.split()[3]
        if chrom in dictracks.keys():
            readbottomtemp = dictracks[chrom][0] + 0.1 + dicsamplesreadbottomtemp[samplename][0]
            if readbottomtemp not in readbottomtemplist:
                readbottomtemplist.append(readbottomtemp)
            if dictracks[chrom][2] not in trackstartlist:
                trackstartlist.append(dictracks[chrom][2])
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])

        #drawcoverage       
            coveragescores =  float(i.split()[4]) * 0.8 #*0.005
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart
            try:
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)].append(float(i.split()[4]))
            except:
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)] = [readbottomtemp]
                dicfrequencyscores[str(readfordrawstart)+"_"+str(readlength)].append(float(i.split()[4]))
            left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
            coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                            fill=True,
                                            color=dicsamplesreadbottomtemp[samplename][1],
                                           linewidth=0.5) 
            populationfrequencybedrectedlist.append(coveragerected)
        
    print(readbottomtemplist, trackstartlist)
    rulerlength = 5
    rulerheight = 0.8
    trackstartlist = int(len(readbottomtemplist)/len(trackstartlist)) * trackstartlist
    
    #ruler of frequencey
    for i in range(len(readbottomtemplist)): 
        left, bottom, width, height = (trackstartlist[i]-50 , readbottomtemplist[i],rulerlength,   rulerheight)
        coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        coveragerected=mpatches.Rectangle((left-5,bottom),width,height-0.75, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        plt.text(left-textwithdraw,bottom-0.05,"0",fontsize=8)
        coveragerected=mpatches.Rectangle((left-5,bottom+0.75),width,height-0.75, 
                                        fill=True,
                                        color="black",
                                       linewidth=2)
        populationfrequencybedrectedlist.append(coveragerected)
        plt.text(left-textwithdraw,bottom+0.65,"1",fontsize=8)
        #plt.text("shahahs")
   # print(dicfrequencyscores)
    #difference annotation
    if anntrack ==1:
        for i in dicfrequencyscores.keys():
            if len(dicfrequencyscores[i])>1:
                if abs(dicfrequencyscores[i][1]-dicfrequencyscores[i][2])>0.2:
                    left, bottom, width, height = (float(i.split("_")[0]), dicfrequencyscores[i][0]-0.6,float(i.split("_")[1]), 0.5) 
                    coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                                    fill=True,
                                                    color=anncolor,
                                                   linewidth=0.5) 
                    populationfrequencybedrectedlist.append(coveragerected)                

    return populationfrequencybedrectedlist,samplesreadbottomtemplist

def mutilplesamplecoveragebed(coveragebedfilename,dictracks,mutilplesamplecolor):
    coveragefile = open(coveragebedfilename,"r")
    coveragefileline =   coveragefile.readlines()
    coveragefile.close()
    readbottom = [] 
    coveragerectedlist = []
    dicsamplesreadbottomtemp = {}
    samplesreadbottomtemplist =[]
    countsample = 0
    donerunsample = []
    for i in coveragefileline:
        #print(i)
        samplename = i.split()[5]
        if samplename not in  samplesreadbottomtemplist:
            samplesreadbottomtemplist.append(samplename)
            dicsamplesreadbottomtemp[samplename] =  [countsample,mutilplesamplecolor[countsample]]
            countsample += 1
            
    for j in dicsamplesreadbottomtemp.keys():    
        print(j)
        for i in coveragefileline:
            #print(i)
            samplename = i.split()[5]
            if samplename in donerunsample:
                continue
            i =i.strip()
            chrom = i.split()[3]
            readbottomtemp = dictracks[chrom][0] + 0.1 + dicsamplesreadbottomtemp[j][0]
            readstart  =int(i.split()[1]) 
            readend =int(i.split()[2])
            coveragescores =  float(i.split()[4]) 
            readforpathpointlength = readstart - dictracks[chrom][1] 
            readfordrawstart= dictracks[chrom][2] + readforpathpointlength 
            readlength = readend - readstart

            left, bottom, width, height = (readfordrawstart, readbottomtemp,readlength,  coveragescores) 
            coveragerected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=dicsamplesreadbottomtemp[j][1],
                                       linewidth=2) 
            coveragerectedlist.append(coveragerected)
        donerunsample.append(samplename)
    return coveragerectedlist

def filiterthenotpairtrack(bam,trackbed,region,numbers):
    import pysam
    readsbedfile = open(trackbed,"r")
    tracklist =   readsbedfile.readlines()
    readsbedfile.close()
    print(tracklist)
    headpoilist = []
    tailpoilist = []
    cutpointlist = []
    subtracklist = []
    supportsubtracks = []
    alltailpoilist = []
    bf = pysam.AlignmentFile(bam,"r")
    for i in bf:
        #
        #if str(i).find("Bas") != -1:
        head = str(i.reference_name)
        tail = str(i.next_reference_name)
        readname = str(i.qname)
        headpoi = int(i.pos+1)
        tailchr = str(i.next_reference_name)
        tailpoi = int(i.mpos+1)
        alltailpoilist.append(int(i.mpos+1))
        
        if head != tail :
            if head != "None" and tail != "None":
                headpoilist.append(headpoi)
                tailpoilist.append([tailchr,tailpoi])
    #spporttrackhead = []
    #spporttrackend = []
    #print(headpoilist)
    #print(tailpoilist)
    supporttracks = []
    for i in tracklist:
        i = i.strip()
        if i.find("main") == -1: 
            mainst = int(i.split()[3].split("-")[1])
            mained = int(i.split()[3].split("-")[2])
            if mainst not in cutpointlist:
                cutpointlist.append(mainst)
            if mained not in cutpointlist:
                cutpointlist.append(mained)
            spport = 0
            spporthead = 0
            spporttail = 0
            spportst  = 0
            spported = 0
            trackchr = i.split()[0]#i.split()[3].split("-")[0]
            trackst = int(i.split()[1])#int(i.split()[3].split("-")[1]) 
            tracked =  int(i.split()[2])#int(i.split()[3].split("-")[2])

            for j in tailpoilist:
                if trackchr == j[0] and trackst- region<j[1]<trackst+region :
                    spportst += 1
                if spportst > numbers:
                    spporthead += 1   
                if  trackchr == j[0] and tracked- region<j[1]<tracked+region :
                    spported += 1
                if spported > numbers:
                    spporttail += 1
                if  spporttail>0 or spporthead > 0:
                    supporttracks.append(i)
                    break
        else:
            maintrack = i
            #supporttracks.append(i)
    cutpointlist.append(int(maintrack.split()[1]))
    cutpointlist.append(int(maintrack.split()[2]))
    maintrackchr =  maintrack.split()[0]
    cutpointlist.sort()
    for i in range(len(cutpointlist)):
        if i < len(cutpointlist)-1:
            subtracklist.append([maintrackchr,cutpointlist[i],cutpointlist[i+1]])
            print(maintrackchr,cutpointlist[i],cutpointlist[i+1],"mainsub")
    supportsubtracks.append(subtracklist[0])
    for i in subtracklist[1:]:
        #print(i)
        spport = 0
        spporthead = 0
        spporttail = 0
        spportst  = 0
        spported = 0
        mainsubst = i[1]
        mainsubed = i[2]
        
        for j in alltailpoilist:
            if  mainsubst<j< mainsubst+region :
                spportst += 1
            if spportst > numbers:
                spporthead += 1   
           # if   mainsubed- region<j<mainsubed+region :
                #spported += 1
            #if spported > numbers:
                #spporttail += 1
            if  spporttail>0 or spporthead > 0:
                supportsubtracks.append(i)
                break
        
    return supporttracks,supportsubtracks

def phasesequence(reliablebed,panfa):
    reliablebedfile= open(reliablebed,"r")
    reliablebedfilelist =   reliablebedfile.readlines()
    reliablebedfile.close()
    dicsort = {}
    sortpoi = []
    reliablebedfilelistsort = []
    for i in reliablebedfilelist:
        if i.find("mainsubreliable") !=-1:
            dicsort[ i.split()[1]] = i 
            sortpoi.append(int(i.split()[1]))
        if i.find("trackreliable") !=-1:    
            dicsort[i.split()[3].split("-")[1]] = i 
            sortpoi.append(int(i.split()[3].split("-")[1]))
    sortpoi.sort()
    for i in sortpoi:
        reliablebedfilelistsort.append(dicsort[str(i)])
        
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
    for i in reliablebedfilelistsort:
        bedchr = i.split()[0]
        bedstart = int(i.split()[1])
        bedend =  int(i.split()[2])
        if i.find("mainsubreliable") !=-1:
            phaseseq += dicfa[bedchr][bedstart-1:bedend]
        if i.find("trackreliable") !=-1:
            pathwayseqchr =bedchr+"_"+  str(bedstart)+"_"+ str(bedend)
            phaseseq += dicfa[pathwayseqchr]
    return phaseseq

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
                plt.text(maintrackstartsnp,mainbottom,j,fontsize=1,color="brown")
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
                plt.text(pathwaystartinmainsnp,pathwaybottom,j,fontsize=1,color="brown")
                pathwaystartinmainsnp +=1
            dicseqtrack[pathwaytrackname] = [int(i.split()[1]),pathwayseq, pathwaybottom]
    return dicseqtrack

def readsnptrack(dicseqtrack,bamdir,dicreaddetailinf):
    import pysam
    import os
    
    for i in list(os.listdir(bamdir)):
        if i.find("bam") !=-1:
            if i.find("bai") ==-1:
                bf = pysam.AlignmentFile(bamdir+"/"+i,"r")
                for j in bf :
                    readname = j.qname
                    if i.find("main") !=-1:
                        readchr = j.reference_name
                    else:
                        chrpoiadd = i.split(":")[1].split(".")[0].split("-")
                        readchr = j.reference_name +"_" +chrpoiadd[0]+"_"+chrpoiadd[1]
                    readmarker = j.cigartuples
                    readseq = j.seq
                    if j.isize > 0:
                        readdirection = "+"
                    else:
                        readdirection = "-"
                    readname += readdirection 
                    if  readname in list(dicreaddetailinf.keys()):
                        readstartpoint = j.pos+1
                        #print(readseq,readstartpoint)
                        #dicseqone = {}
                        mapstart  = 0
                        blankjump = 0
                        for k in readmarker:
                            if k[0] == 0:
                                mapstart =  mapstart+blankjump
                                maplength = k[1]

                                mapend = mapstart+maplength
                               # print(mapstart,mapend)
                                mapseq = readseq[mapstart:mapend] 

                                refstart = readstartpoint+mapstart-dicseqtrack[readchr][0]

                                refend = readstartpoint+mapstart-dicseqtrack[readchr][0]+maplength
                                refseq = dicseqtrack[readchr][1][refstart:refend] 
                                mapstart = mapstart +  maplength 
                                #print('saasasa',refstart,refend)
                                if  len(mapseq) ==  len(refseq):
                                    #print(mapseq,refseq,"seqtwo")
                                    for l in range(len(mapseq)):
                                        if mapseq[l] != refseq[l]:
                                            plt.text(dicreaddetailinf[readname][0]+l,dicreaddetailinf[readname][1],mapseq[l],fontsize=2.5,color="black")
                                            #print(mapseq[l],"here")
                                    blankjump = 0
                            else:
                                blankjump += k[1]
                                
      
                
                
def gaingene(inindex,gfffilename,pathwaybedfilename):
    readpathwaybedfile = open(pathwaybedfilename,"r")
    readpathwaybedfileline =   readpathwaybedfile.readlines()
    readpathwaybedfile.close()
    gfffile = open(gfffilename,"r")
    gfffileline =   gfffile.readlines()
    gfffile.close()
    gaingenefile = open(inindex+"/pathwaygaingene.bed","w")
    for i in  readpathwaybedfileline:
        chrn = i.split()[0]
        st = int(i.split()[1])
        ed = int(i.split()[2])
        if i.find("main") == -1:
            chrn = i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            print(chrn,"geneann")
        for j in gfffileline:
            if j.find("#") == -1:
                temp = j.split()
                if temp[2] == "gene":
                    gchrn = temp[0]
                    gst = int(temp[3])
                    ged = int(temp[4])
                    if  gchrn.find("_") != -1:
                       # print(gchrn)
                        gst += int(gchrn.split("_")[1])
                        ged += int(gchrn.split("_")[1])
                    direction = temp[6]
                    geneid  = temp[8].split("ID=")[1].split(";")[0]
                    if st < gst and  ged<ed and gchrn ==chrn:
                        print(gchrn,gst,ged,geneid,geneid,file = gaingenefile)
    gaingenefile.close()
    
    
def legendblock(colors,text,xpoi,ypoi,legendheight,coefficient,laynum):
    laynumcof = laynum/10
    left, bottom, width, height = (xpoi, ypoi-0.2,coefficient,  legendheight) 
    legendblock=mpatches.Rectangle((left,bottom+laynumcof),width,height, 
                                        fill=True,
                                        color=colors,
                                       linewidth=2) 
    plt.text(xpoi,ypoi-0.2,text,fontsize=6.5)
    return legendblock
        



