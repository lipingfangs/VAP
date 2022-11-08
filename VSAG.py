import matplotlib.pyplot as plt
import sys
import os
#import pandas as pd
import matplotlib.patches as mpatches
sys.path.append("/share/lfp/Graphdraw/VSAG/src")

from cutpathwayreliablebed import * 
from drawcoverage import * 
from drawread  import * 
from  drawtrack import * 
from  geneannotation import * 
from filiterthenotpairtrack import *
#basic control
def mainVSAG(args):
    inindex = args.inindex
    outimage = args.out
    imagatype = args.imtype #"svg" #png,jpg
    anntrack = args.anntracks#0
    pairend =args.pairend #0
    genefile = args.geneinfo # gene info file with .bed
    pairendsearchranges = args.pairendrange #200
    pairendtheraolds = args.pairendtheraold #1
    if genefile != "none":
        drawgene = 1
    else:
        drawgene = 0
    middlethetrackandread = args.middle
    drawtype = args.drawtype #"#"#"read","coverage","mutiplesamples"
    
    #mutiplesamples = 0
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
    
    fig=plt.figure(dpi=dpisize,figsize=(sizex,sizey))
    plt.xlabel(xlabelname,fontweight ='bold', size=18)
    plt.ylabel(ylabelname, fontweight ='bold',size=18)


    sizetrackx, sizetracky, maintrack, pathwaytracks,linepointx,linepointy,dictracks,dicpathwaybottom  = readpathwaybed(inindex+"/pathwaybed.bed",drawtrackcolor,middlethetrackandread)
    readtracks,linepointpairendx,linepointpairendy = readreadbed(inindex+"/reads.bed",dictracks,drawreadcolor)

    for i in range(len(sizetrackx)): #pic size
        plt.plot(sizetrackx[i], sizetracky[i], color='white')

    rectlist = []
    rectlist.append(maintrack)
    annrectlist = []
    #base function draw the genome tracks
    for i in pathwaytracks:
        rectlist.append(i)
    for i in rectlist:   
        plt.gca().add_patch(i)
    for i in range(len(linepointx)):
        plt.plot(linepointx[i], linepointy[i], color='pink',zorder=0)

    if  drawtype == "read":
        for i in readtracks:   
            plt.gca().add_patch(i)
        #print(readtracks)
        if pairend == 1:
            for i in range(len(linepointpairendx)):
                plt.plot(linepointpairendx[i], linepointpairendy[i], color=pairendlinecolor,alpha=0.2)
        # draw the negvation annotation
        if anntrack == 1:
            bamlist = os.listdir(inindex)
            for i in bamlist:
                if i.find("main") != -1:
                    annmainbam = i
            supporttracks, supportsubtracks= filiterthenotpairtrack(inindex+"/"+ annmainbam, inindex+"/pathwaybed.bed",pairendsearchranges,pairendtheraolds)
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

    if  drawtype == "coverage":
        coveragerectedlist = readcoveragebed(inindex+"/depth.regions.bed",dictracks,coveragecolor)
        for i in  coveragerectedlist:
            plt.gca().add_patch(i)

    if drawtype == "mutiplesamples":
        mutiplesamplescoveragerectedlist =  mutilplesamplecoveragebed(inindex+"/mutildepth.regions.bed",dictracks,mutilplesamplecolor)
        for i in   mutiplesamplescoveragerectedlist:
            plt.gca().add_patch(i)

    if drawgene == 1:  
        genetractlist, genenamelist, genenamepoilist = geneannbed(inindex+"/withassembly/gene.bed",dictracks,genecolor)
        print(genenamelist)
        for i in  genetractlist:
            plt.gca().add_patch(i)
        for i in range(len(genenamelist)):
            plt.text(genenamepoilist[i][0], genenamepoilist[i][1], " "+genenamelist[i], fontsize=10, color=genecolor)

    plt.savefig(outimage+"."+imagatype ,dpi = dpisize )
