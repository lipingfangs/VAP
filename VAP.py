import matplotlib.pyplot as plt
#import pandas as pd
import matplotlib.patches as mpatches
from mpld3 import *
import mpld3
#import plotly.tools as tls
#import plotly.offline
import os
import sys
import math
import json
#sys.path.append("/share/lfp/Graphdraw/VSAG/src")
from src.coverage import *
from src.cutpathwayreliablebed import *
from src.drawread import *
from src.drawtrack import *
from src.filiterthenotpairtrack import *
from src.gaingene import *
from src.geneannotation import *
from src.legendblock import *
from src.mutilplesamplecoverage import *
from src.phasesequence import *
from src.populationfreq import *
from src.readsnptrack import *
from src.snptrack import *
from src.sortread import *
from src.sortreadnovel import *
from src.readonlylargedeletion import *
from src.goonefasta import *
from src.gaincoverag import *
from src.populationfrequencybedwithline import *
from src.drawline import *
from src.mutilplesamplecoveragewithline import *
from src.graphindex import *
from src.graphconvey import *
#input of file and dir
def mainVAG(args):
    #input of file and dir
    mode = args.mode
    if mode == "index":
        graphindex(args.rfa)
        print("#Running index mode")
        quit()
    if mode == "convey":
        print("#Running graph convey mode")
        graphconvey(args.gfa,args.ref)
        quit()
    outimage = args.out
    graphgff = args.gff
    inindex = args.inindex
    phasefastafile = args.fa
    genespecificbed = args.geneinfo
    

    #basic control
    filitertracklength = args.fl #filiter the track short than 500
    #filitertrackornot = 0
    drawtype = args.drawtype #read" #"#"read","coverage","mutiplesamples""populationfreq" ,"track"
    imagatype = args.imtype  #png,jpg
    anntrack =args.anntracks #0
    phasefastaornot = 0
    gaingeneornot = args.gaingene
    if genespecificbed  != "none" or  gaingeneornot!=0:
        if graphgff == "none" and gaingeneornot!=0:
             drawgene = 0
        else:
             drawgene = 1
    else:
        drawgene = 0
        
    #mutiplesamples = 0
    middlethetrackandread = args.middle
    drawsnp = args.snp#snp in short scale
    drawreadsnp = args.snp #snp in short reads
    drawonlylargesvinread = args.onlysv
    drawonlylargesvinreadthersold = args.onlysvthersold
    pairend =args.pairend 
    pairendsearchranges = args.pairendrange #200
    pairendtheraolds = args.pairendtheraold #1
    readspilt = args.readspilt
    displayonline  = args.dw #1
    legend = args.legend
    legendheight = args.legendheight
    writethereadnameornot = args.rn
    trackdireactionornot = args.td
    readsdirection = args.rd
    coveragesteplength = args.coveragesteplength
    drawpopultionwithline = args.popline
    drawmutiplesampleswithline = args.samplesline
    #color
    drawtrackcolorlist = args.trackcolor.split(",")
    drawtrackcolor = [drawtrackcolorlist[0],drawtrackcolorlist[1]]
    drawreadcolor = args.readcolor
    pairendlinecolor = args.pairendcolor
    readsplitcolor = args.readsplitcolor #FFB266
    coveragecolor =  args.coveragecolor #anncolor"#FF7F50"
    anncolor =args.anncolor #"#D02090"
    genecolor = args.genecolor #"black"
    mutilplesamplecolorlist = args.mutilplesamplecolor.split(",")
    mutilplesamplecolor = [mutilplesamplecolorlist[0],mutilplesamplecolorlist[1]]

    #size of pic
    sizex = args.sx #20
    selfajust = args.selfajust 
    sizey =  args.sy #8
    xlabelname = args.xlabel #"Position"
    ylabelname = args.ylabel #"Pathway"
    dpisize = args.ppi
    
#    if sizex == 0:
 #       sizex = math.log(sizex,1000)
  #      if sizex < 20:
   #         sizex = 20

    #fig=plt.figure(figsize=(sizex,sizey))#dpi=dpisize,figsize=(sizex,sizey))
    #ax=plt.gca()
    #ax.get_yaxis().set_visible(False)
    #plt.axis('off')
   # plt.xlabel(xlabelname,fontweight ='bold', size=10)
    #plt.ylabel(ylabelname, fontweight ='bold',size=21)
    
    if filitertracklength > 0:
        print("cat "+inindex+"/pathwaybed.bed |awk '{if($3-$2>"+str(filitertracklength)+"){print $0}}' > "+inindex+"/pathwaybeddraw.bed")
        os.system("cat "+inindex+"/pathwaybed.bed |awk '{if($3-$2>"+str(filitertracklength)+"){print $0}}' > "+inindex+"/pathwaybeddraw.bed")
    else:
        print("cp "+inindex+"/pathwaybed.bed "+inindex+"/pathwaybeddraw.bed")
        os.system("cp "+inindex+"/pathwaybed.bed "+inindex+"/pathwaybeddraw.bed")

    sizetrackx, sizetracky, maintrack, pathwaytracks,linepointx,linepointy,dictracks,dicpathwaybottom,mainlength,maintrackname  = readpathwaybed(inindex+"/pathwaybeddraw.bed",drawtrackcolor,middlethetrackandread,trackdireactionornot)
    print(dictracks)
#self adaptation of sizex
    if sizex == 0:
        sizex = int(mainlength/2000)
        if sizex < 20 or selfajust == "none":
            sizex = 20
    print("#size draw",mainlength,sizex,sizey)
    fig=plt.figure(figsize=(sizex,sizey))#dpi=dpisize,figsize=(sizex,sizey))
    ax=plt.gca()
    #ax.get_yaxis().set_visible(False)
    #plt.axis('off')
    plt.xlabel(xlabelname,fontweight ='bold', size=10)
    plt.ylabel(ylabelname, fontweight ='bold',size=21)


    for i in range(len(sizetrackx)): #pic size
        plt.plot(sizetrackx[i], sizetracky[i], color='white')

    #page start and legend x,y position
    sizexzero = sizetrackx[0][0]
    sizeyzero =  sizetracky[0][0]
    sizexcoff = (sizetrackx[0][1]- sizetrackx[0][0])/8
    print(sizexzero,sizeyzero)
    #base function draw the genome tracks
    rectlist = []
    rectlist.append(maintrack)
    annrectlist = []
    laynum = 0
    for i in pathwaytracks:
        rectlist.append(i)
        laynum+=1
    for i in rectlist:   
        plt.gca().add_patch(i)

    if   legend  ==1:
        legendblockmain = legendblock(drawtrackcolor[0],"Main Pathway",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
        sizexzero = sizexzero + sizexcoff
        plt.gca().add_patch(legendblockmain)
        legendblockpathway = legendblock(drawtrackcolor[1],"Branch Pathway",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
        sizexzero = sizexzero + sizexcoff
        plt.gca().add_patch(legendblockpathway)
        if trackdireactionornot ==1:
            legendtrackdireaction = legendblock("#000099","Reverve Branch",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
            sizexzero = sizexzero + sizexcoff
            plt.gca().add_patch(legendtrackdireaction)
            
    #line of track varition    
    for i in range(len(linepointx)):
        plt.plot(linepointx[i], linepointy[i], color='pink',zorder=0)

    if  drawtype == "read":
        if mode == "gam":
            for gam in os.listdir(inindex):
                if gam.find("json") !=-1:
                    gamfilejson = gam
                    break
            jsonfile = inindex+"/"+gamfilejson
            print("jsonfile is",jsonfile)
        else:
            jsonfile = "none"
        readsbedfilename = inindex+"/reads.bed"
        readtracks,linepointpairendx,linepointpairendy,dicreaddetailinf,linepointsplitreadx,linepointsplitready = readreadbed(readsbedfilename,dictracks,drawreadcolor,readsdirection,mode,jsonfile,maintrackname)
        
        for i in readtracks:   
            plt.gca().add_patch(i)
        if   legend  ==1:
            legendblockmain = legendblock(drawreadcolor,"Read",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
            sizexzero +=  sizexcoff
            plt.gca().add_patch(legendblockmain)
            if readsdirection ==1:
                legendreadsdirection = legendblock("#808080","Reverve Read",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
                sizexzero +=  sizexcoff
                plt.gca().add_patch(legendreadsdirection)
        #print(readtracks)
        if pairend == 1:
            for i in range(len(linepointpairendx)):
                plt.plot(linepointpairendx[i], linepointpairendy[i], color=pairendlinecolor,alpha=0.2)
            if   legend  ==1:
                legendblockmain = legendblock(pairendlinecolor,"PE-inf",sizexzero,sizeyzero,legendheight/6,sizexcoff/2,laynum)
                sizexzero = sizexzero + sizexcoff
                plt.gca().add_patch(legendblockmain)
                
        if readspilt ==1:
            for i in range(len(linepointsplitreadx)):
                
                plt.plot(linepointsplitreadx[i], linepointsplitready[i], color=readsplitcolor,alpha=0.2)
            if   legend  ==1:
                legendblockmain = legendblock(readsplitcolor,"Read Split",sizexzero,sizeyzero,legendheight/6,sizexcoff/2,laynum)
                sizexzero = sizexzero + sizexcoff
                plt.gca().add_patch(legendblockmain)

        if anntrack == 1:
            if   legend  ==1:
                legendblockmain = legendblock(anncolor,"Reliable Track",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
                sizexzero = sizexzero + sizexcoff
                plt.gca().add_patch(legendblockmain)
            bamlist = os.listdir(inindex)
            for i in bamlist:
                if i.find("main") != -1 and i.find("bai") == -1 and i.find("region") == -1 and i.find("mosdepth") == -1:
                    annmainbam = i
            supporttracks, supportsubtracks= filiterthenotpairtrack(inindex+"/"+ annmainbam, inindex+"/pathwaybeddraw.bed",pairendsearchranges,pairendtheraolds,dicreaddetailinf,mode,jsonfile)
            supporttracksfile = open(inindex+"/pathways.reliable.bed","w")
            for i in supportsubtracks:
                print(i[0],i[1],i[2],"mainsubreliable",file =  supporttracksfile)
            for i in supporttracks:
                print(i,"trackreliable",file =supporttracksfile )
            supporttracksfile.close()
            annmaintracksublist, annpathwaytracks, annlinepointx, annlinepointy, anndictracks  = cutpathwayreliablebed(inindex+"/pathways.reliable.bed",dicpathwaybottom,anncolor,middlethetrackandread)
            for i in annmaintracksublist:
                annrectlist.append(i)
            for i in annpathwaytracks:
                annrectlist.append(i)
            for i in annrectlist:   
                plt.gca().add_patch(i)
            if phasefastaornot ==1:
                phasefasteseq = phasesequence(inindex+"/pathways.reliable.bed",phasefastafile)
                phasefasteseqfile = open(inindex+"/"+outimage+".fa","w")
                print(">phasequence",file =  phasefasteseqfile)
                print( phasefasteseq ,file =  phasefasteseqfile)
                phasefasteseqfile.close()


    if  drawtype == "coverage":
        gaincoverage(inindex+"/pathwaybeddraw.bed",inindex+"/pathwaybeddraw.window.bed",coveragesteplength )
        os.system("for i in $(ls "+inindex+" | grep 'bam'|grep -v 'bai' | grep -v 'mosdepth' | grep -v 'region'); do mosdepth -b "+inindex+"/pathwaybeddraw.window.bed -n -t 12 -i 194 -Q 20 "+inindex+"/pathway.depth.$i "+inindex+"/$i; done" )
        print("for i in "+inindex+"/*bam; do mosdepth -b ./pathwaybeddraw.window.bed -n -t 12 -i 194 -Q 20 pathway.depth.$i $i; done")
        os.system("cat "+inindex+"/*gz > "+inindex+"/pathway.regions.bed.gz" )
        print("cat "+inindex+"/*gz > "+inindex+"/pathway.regions.bed.gz" )
        os.system("gzip -d "+inindex+"/pathway.regions.bed.gz" )
        print("gzip -d "+inindex+"/pathway.regions.bed.gz" )
        coveragerectedlist = readcoveragebed(inindex+"/pathway.regions.bed",dictracks,coveragecolor)
        for i in  coveragerectedlist:
            plt.gca().add_patch(i)
        if   legend  ==1:
            legendblockmain = legendblock(coveragecolor,"Read Coverage",sizexzero,sizeyzero,legendheight*3,sizexcoff/8,laynum)
            sizexzero +=  sizexcoff
            plt.gca().add_patch(legendblockmain)
            
    if drawtype == "mutiplesamples":
        gaincoverage(inindex+"/pathwaybeddraw.bed",inindex+"/pathwaybeddraw.window.bed",coveragesteplength )
        os.system("for i in $(ls "+inindex+" | grep 'bam'|grep -v 'bai' | grep -v 'mosdepth' | grep -v 'region'); do mosdepth -b "+inindex+"/pathwaybeddraw.window.bed -n -t 12 -i 194 -Q 20 "+inindex+"/pathway.depth.$i "+inindex+"/$i; done" )
        listdirbam = os.listdir(inindex)
        listbam = []
       
        for i in listdirbam:
            if i.find("bam") != -1 and i.find("pathway") == -1:
                tempbamname = i.split(".bam")[0]
                if tempbamname not in listbam:
                    listbam.append(tempbamname)
        for i in listbam:
            os.system("cat "+inindex+"/pathway.depth."+i+"*gz > "+inindex+"/"+i+"pathway.regions.bed.gz" )
            os.system("gzip -d "+inindex+"/"+i+"pathway.regions.bed.gz" )
            
        for i in listbam:
            print("cat "+inindex+"/"+i+"pathway.regions.bed | awk '{print $0,"+i+"}' >>"+inindex+ "/pathway.regions.bed")
            os.system("cat "+inindex+"/"+i+"pathway.regions.bed | awk '{print $0,"+i+"}' >>"+inindex+ "/pathway.regions.bed" )
        if len(listbam)>2 or drawmutiplesampleswithline ==1:
            mutiplesamplescoveragerectedlist,samplesreadbottomtemplist =  mutilplesamplecoveragewithline(inindex+"/pathway.regions.bed",dictracks,mutilplesamplecolor,mainlength,anncolor)
        else:
            mutiplesamplescoveragerectedlist =  mutilplesamplecoveragebed(inindex+"/pathway.regions.bed",dictracks,mutilplesamplecolor)
        
        for i in   mutiplesamplescoveragerectedlist:
            plt.gca().add_patch(i)
        countcolor = 0    
        
        
        for i in listbam:
            
            #os.system("cat "+inindex+"/"+i+"pathway.regions.bed | awk '{print $0,"+i+"}' >> pathway.regions.bed" )
            legendblockmain = legendblock(mutilplesamplecolor[countcolor],i,sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
            sizexzero = sizexzero + sizexcoff
            countcolor  +=1
            plt.gca().add_patch(legendblockmain)
 

    if drawtype == "populationfreq":
        if drawpopultionwithline == 1:
            populationfrequencybedrectedlist,samplesreadbottomtemplist =  populationfrequencybedwithline(inindex+"/population.frq.bed",dictracks,mutilplesamplecolor,mainlength,anncolor)
            for i in   populationfrequencybedrectedlist:
                plt.gca().add_patch(i) 
        else:
            populationfrequencybedrectedlist,samplesreadbottomtemplist =  populationfrequencybed(inindex+"/population.frq.bed",dictracks,mutilplesamplecolor,mainlength,anncolor)
            for i in   populationfrequencybedrectedlist:
                plt.gca().add_patch(i)  
            
        if   legend  ==1:
            for i in range(len(samplesreadbottomtemplist)):    
               # print(mutilplesamplecolor)
                legendblockmain = legendblock(mutilplesamplecolor[i],samplesreadbottomtemplist[i],sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
                sizexzero = sizexzero + sizexcoff
                plt.gca().add_patch(legendblockmain)
            legendblockmain = legendblock(anncolor,"Different interval",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
            plt.gca().add_patch(legendblockmain)   

    if gaingeneornot == 1:  
        gaingene(inindex,graphgff,inindex+"/pathwaybeddraw.bed")
        genetractlist, genenamelist, genenamepoilist = geneannbed(inindex+"/pathwaygaingene.bed",dictracks,genecolor)
        print(genenamelist)
        for i in  genetractlist:
            plt.gca().add_patch(i)
        for i in range(len(genenamelist)):
            plt.text(genenamepoilist[i][0], genenamepoilist[i][1], " "+genenamelist[i], fontsize=8, color=genecolor)

    if  gaingeneornot == 0 and drawgene == 1:  
        genetractlist, genenamelist, genenamepoilist = geneannbed(genespecificbed,dictracks,genecolor)
        print(genenamelist)
        for i in  genetractlist:
            plt.gca().add_patch(i)
        for i in range(len(genenamelist)):
            plt.text(genenamepoilist[i][0], genenamepoilist[i][1], " "+genenamelist[i], fontsize=6, color=genecolor)

            
    if drawsnp == 1 and drawtype == "read":
        drawonlylargesvinread = 0
        sizerange = int(sizetrackx[0][1]- sizetrackx[0][0])
        print("Snp display sizerange:",sizerange,end = ":")
        if sizerange < 2100:
            if phasefastafile !="none":
                phasefastafiledic = goonefasta(phasefastafile)
                aeqornot = 1
            else:
                phasefastafile = inindex+"/snpreference.fa"
                phasefastafiledic = goonefasta(phasefastafile)
                aeqornot = 0
            dicseqtrack = snptrack(inindex+"/pathwaybeddraw.bed",dictracks,middlethetrackandread,phasefastafiledic,1,aeqornot) #tracksnpornot
           # print(dicseqtrack,"sas")
            if drawreadsnp == 1:
                 varitionblocklist = readsnptrack(dicseqtrack,inindex,dicreaddetailinf,writethereadnameornot)
                 for i in  varitionblocklist:
                    plt.gca().add_patch(i)  
        else:
            print("too large interval, not display")
            drawonlylargesvinread = args.onlysv
            
    if drawonlylargesvinread ==1 and drawtype == "read":
        print("Only show the large insertion and deletion")
        phasefastafiledic = ""
        dicseqtrack = snptrack(inindex+"/pathwaybeddraw.bed",dictracks,middlethetrackandread,phasefastafiledic,0,0)
        varitionblocklist =  readonlylargedeletion(dicseqtrack,inindex,dicreaddetailinf,writethereadnameornot,mode)

        for i in  varitionblocklist:
            plt.gca().add_patch(i)


    print("dictracks",dictracks)
    listy = []
    for i in dictracks.keys():
        laynum = dictracks[i][0]
        if laynum not in listy:
            listy.append(laynum)
    print("listy",listy)
    listyname = ["Main (Reference)"]
    clayer = 0
    for i in listy[1:]:
        clayer +=1
        listyname.append("Branch Layer "+str(clayer))
        
    ax.set_yticklabels(listyname)
    ax.set_yticks(listy)
    plt.savefig(outimage+"."+imagatype ,dpi = dpisize )

    if displayonline == 1:
        #plotly_fig = tls.mpl_to_plotly(fig)
        #plotly.offline.plot(plotly_fig, filename=outimage+"."+"html")
        save_html(fig,outimage+"."+"html")
