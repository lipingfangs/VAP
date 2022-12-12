import matplotlib.pyplot as plt
#import pandas as pd
import matplotlib.patches as mpatches
from mpld3 import *
import mpld3
import os
import sys
from VSAGwebsp import *
#input of file and dir
outimage = "chr10.2260000.2280000"
graphgff = "pantengraph.liner.gff"
inindex = sys.argv[1]
phasefastafile = "./genome/TenRice.one.fa"
genespecificbed = "geneOs01g0851600.bed"

#basic control
filitertracklength = 0 #filiter the track short than 100
filitertrackornot = 1
drawtype = sys.argv[3]#read" #"#"read","coverage","mutiplesamples""populationfreq"
imagatype = "png" #png,jpg
anntrack = int(sys.argv[4].split(",")[0])
pairend =1
phasefastaornot = 0
gaingeneornot = 0
drawgene = 0
mutiplesamples = 0
middlethetrackandread = 1
drawsnp = int(sys.argv[5])#snp in short scale
drawreadsnp = int(sys.argv[5]) #snp in short reads
pairendsearchranges = 300 #200
pairendtheraolds = 1 #1
displayonline  = 1 #1
legend = 1
legendheight = 0.3

colorstr = sys.argv[2]
colorlist =colorstr.split(",") 
#color
drawtrackcolor = [colorlist[0],colorlist[1]]
drawreadcolor = colorlist[2]
pairendlinecolor = colorlist[3]
coveragecolor = "#FF7F50"
anncolor = sys.argv[4].split(",")[1]
genecolor = "black"
mutilplesamplecolor = [colorlist[4],colorlist[5]]

#size of pic
sizex = 12
sizey = 4
xlabelname = "Position (bp)"
ylabelname = "Pathway"
dpisize = 150
fig=plt.figure(figsize=(sizex,sizey))#dpi=dpisize,figsize=(sizex,sizey))
ax=plt.gca()
ax.get_yaxis().set_visible(False)
#plt.axis('off')
plt.xlabel(xlabelname,fontweight ='bold', size=10)
plt.ylabel(ylabelname, fontweight ='bold',size=18)

if filitertrackornot ==1:
    #print("cat "+inindex+"/pathwaybed.bed |awk '{if($3-$2>"+str(filitertracklength)+"){print $0}}' > "+inindex+"/pathwaybeddraw.bed")
    os.system("cat "+inindex+"/pathwaybed.bed |awk '{if($3-$2>"+str(filitertracklength)+"){print $0}}' > "+inindex+"/pathwaybeddraw.bed")
else:
    #print("cp "+inindex+"/pathwaybed.bed "+inindex+"/pathwaybeddraw.bed")
    os.system("cp "+inindex+"/pathwaybed.bed "+inindex+"/pathwaybeddraw.bed")
    
sizetrackx, sizetracky, maintrack, pathwaytracks,linepointx,linepointy,dictracks,dicpathwaybottom,mainlength  = readpathwaybed(inindex+"/pathwaybeddraw.bed",drawtrackcolor,middlethetrackandread)


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
    readtracks,linepointpairendx,linepointpairendy,dicreaddetailinf = readreadbed(inindex+"/reads.bed",dictracks,drawreadcolor)

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
            if i.find("main") != -1:
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
    coveragerectedlist = readcoveragebed("./withassembly/graphsamtoolstempdir/91.sort.bam.depth.regions.bed",dictracks,coveragecolor)
    for i in  coveragerectedlist:
        plt.gca().add_patch(i)

if drawtype == "mutiplesamples":
    mutiplesamplescoveragerectedlist =  mutilplesamplecoveragebed("./withassembly/graphsamtoolstempdir/mutiltestdepth.regions.bed",dictracks,mutilplesamplecolor)
    for i in   mutiplesamplescoveragerectedlist:
        plt.gca().add_patch(i)

if drawtype == "populationfreq":
    populationfrequencybedrectedlist,samplesreadbottomtemplist =  populationfrequencybed(inindex+"/population.frq.bed",dictracks,mutilplesamplecolor,mainlength,anntrack,anncolor)
    for i in   populationfrequencybedrectedlist:
        plt.gca().add_patch(i)  
    if   legend  ==1:
        for i in range(len(samplesreadbottomtemplist)):    
           # print(mutilplesamplecolor)
            legendblockmain = legendblock(mutilplesamplecolor[i],samplesreadbottomtemplist[i],sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
            sizexzero = sizexzero + sizexcoff
            plt.gca().add_patch(legendblockmain)
        if anntrack == 1:
            legendblockmain = legendblock(anncolor,"Different interval",sizexzero,sizeyzero,legendheight,sizexcoff/2,laynum)
            plt.gca().add_patch(legendblockmain)   
        
if gaingeneornot == 1:  
    gaingene(inindex,graphgff,inindex+"/pathwaybeddraw.bed")
    genetractlist, genenamelist, genenamepoilist = geneannbed(inindex+"/pathwaygaingene.bed",dictracks,genecolor)
    print(genenamelist)
    for i in  genetractlist:
        plt.gca().add_patch(i)
    for i in range(len(genenamelist)):
        plt.text(genenamepoilist[i][0], genenamepoilist[i][1], " "+genenamelist[i], fontsize=4, color=genecolor)
        
if  gaingeneornot == 0 and drawgene == 1:  
    genetractlist, genenamelist, genenamepoilist = geneannbed(genespecificbed,dictracks,genecolor)
    print(genenamelist)
    for i in  genetractlist:
        plt.gca().add_patch(i)
    for i in range(len(genenamelist)):
        plt.text(genenamepoilist[i][0], genenamepoilist[i][1], " "+genenamelist[i], fontsize=6, color=genecolor)
        
        
if drawsnp == 1:
    sizerange = int(sizetrackx[0][1]- sizetrackx[0][0])
    print("Snp display sizerange:",sizerange)
    if sizerange < 1200:
        dicseqtrack = snptrack(inindex+"/pathwaybed.bed",middlethetrackandread,phasefastafile)
       # print(dicseqtrack,"sas")
        if drawreadsnp == 1:
            readsnptrack(dicseqtrack,inindex,dicreaddetailinf)
         
        
plt.savefig(outimage+"."+imagatype ,dpi = dpisize )

if displayonline == 1:
    save_html(fig,inindex+"."+"html")

#mpld3.enable_notebook()  #jupyter notebook中渲染图形
