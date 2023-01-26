def gaincoverage(bedonefile,bedonefileout,coveragesteplength ):
    bedonefile = open(bedonefile,"r")
    bedonelist =   bedonefile.readlines()
    bedonefile.close()
    bedonefileout  = open(bedonefileout,"w")
    for i in bedonelist:
        countstep = 0

        chrname = i.split()[0]
        cst = int(i.split()[1])
        ced =  int(i.split()[2])
        if i.find("main") == -1:
            chrnow =  chrname+"_"+str(cst)+"_"+str(ced)
        else:
            chrnow =  chrname
        for j in range(cst,ced,coveragesteplength):

            countstep += 1
            print(chrname,j,j+coveragesteplength,chrnow,sep = "\t",file = bedonefileout)
    bedonefileout.close()
