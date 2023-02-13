import matplotlib.pyplot as plt
#import pandas as pd
import matplotlib.patches as mpatches
from mpld3 import *
import mpld3
import os
import sys
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

#input of file and dir
def mainVAG(args):
    #input of file and dir
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
    displayonline  = args.dw #1
    legend = args.legend
    legendheight = args.legendheight
    writethereadnameornot = args.rn
    trackdireactionornot = args.td
    readsdirection = args.rd
    coveragesteplength = args.coveragesteplength
    drawpopultionwithline = args.popline
    
    #color
    drawtrackcolorlist = args.trackcolor.split(",")
    drawtrackcolor = [drawtrackcolorlist[0],drawtrackcolorlist[1]]
    drawreadcolor = args.readcolor
    pairendlinecolor = args.pairendcolor
    coveragecolor =  args.coveragecolor #anncolor"#FF7F50"
    anncolor =args.anncolor #"#D02090"
    genecolor = args.genecolor #"black"
    mutilplesamplecolorlist = args.mutilplesamplecolor.split(",")
    mutilplesamplecolor = [mutilplesamplecolorlist[0],mutilplesamplecolorlist[1]]

    #size of pic
    sizex = args.sx #20
    sizey =  args.sy #8
    xlabelname = args.xlabel #"Position"
    ylabelname = args.ylabel #"Pathway"
    dpisize = args.ppi
    
    fig=plt.figure(figsize=(sizex,sizey))#dpi=dpisize,figsize=(sizex,sizey))
    ax=plt.gca()
    ax.get_yaxis().set_visible(False)
    #plt.axis('off')
    plt.xlabel(xlabelname,fontweight ='bold', size=10)
    plt.ylabel(ylabelname, fontweight ='bold',size=21)

    if filitertracklength > 0:
        print("cat "+inindex+"/pathwaybed.bed |awk '{if($3-$2>"+str(filitertracklength)+"){print $0}}' > "+inindex+"/pathwaybeddraw.bed")
        os.system("cat "+inindex+"/pathwaybed.bed |awk '{if($3-$2>"+str(filitertracklength)+"){print $0}}' > "+inindex+"/pathwaybeddraw.bed")
    else:
        print("cp "+inindex+"/pathwaybed.bed "+inindex+"/pathwaybeddraw.bed")
        os.system("cp "+inindex+"/pathwaybed.bed "+inindex+"/pathwaybeddraw.bed")

    sizetrackx, sizetracky, maintrack, pathwaytracks,linepointx,linepointy,dictracks,dicpathwaybottom,mainlength  = readpathwaybed(inindex+"/pathwaybeddraw.bed",drawtrackcolor,middlethetrackandread,trackdireactionornot)
    print(dictracks)

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
    #line of track varition    
    for i in range(len(linepointx)):
        plt.plot(linepointx[i], linepointy[i], color='pink',zorder=0)

    if  drawtype == "read":
        readtracks,linepointpairendx,linepointpairendy,dicreaddetailinf = readreadbed(inindex+"/reads.bed",dictracks,drawreadcolor,readsdirection)

        for i in readtracks:   
            plt.gca().add_patch(i)
        if   legend  ==1:
            legendblockmain = legendblock(drawreadcolor,"Read",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
            sizexzero +=  sizexcoff
            plt.gca().add_patch(legendblockmain)
        #print(readtracks)
        if pairend == 1:
            for i in range(len(linepointpairendx)):
                plt.plot(linepointpairendx[i], linepointpairendy[i], color=pairendlinecolor,alpha=0.2)
            if   legend  ==1:
                legendblockmain = legendblock(pairendlinecolor,"PE-inf",sizexzero,sizeyzero,legendheight/6,sizexcoff/2,laynum)
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
            supporttracks, supportsubtracks= filiterthenotpairtrack(inindex+"/"+ annmainbam, inindex+"/pathwaybeddraw.bed",pairendsearchranges,pairendtheraolds)
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

    if drawtype == "mutiplesamples":
        mutiplesamplescoveragerectedlist =  mutilplesamplecoveragebed(inindex+"/mutiltestdepth.regions.bed",dictracks,mutilplesamplecolor)
        for i in   mutiplesamplescoveragerectedlist:
            plt.gca().add_patch(i)

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
            plt.text(genenamepoilist[i][0], genenamepoilist[i][1], " "+genenamelist[i], fontsize=6, color=genecolor)

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
        varitionblocklist =  readonlylargedeletion(dicseqtrack,inindex,dicreaddetailinf,writethereadnameornot)

        for i in  varitionblocklist:
            plt.gca().add_patch(i)



    plt.savefig(outimage+"."+imagatype ,dpi = dpisize )

    if displayonline == 1:
        save_html(fig,outimage+"."+"html")

#mpld3.enable_notebook()  #jupyter notebook draw html
