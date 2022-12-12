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
