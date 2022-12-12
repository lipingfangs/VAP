import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
        genenamey = genebottomtemp-0.25
        genenamepoilist.append([genenamex,genenamey])
    return genetract, genenamelist, genenamepoilist
