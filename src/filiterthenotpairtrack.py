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


#print(filiterthenotpairtrack("c271.sort.bam.Chr10.165000.175000.bam", "withassembly/graphsamtoolstempdir/pathwaybed.bed",200,5))                                  
#supporttracks, supportsubtracks= filiterthenotpairtrack("withassembly/91.sort.bam.Chr10.100000.120000.bam", "withassembly/graphsamtoolstempdir/pathwaybed.bed",100,1)    
#for i in supportsubtracks:
    #print(i[0],i[1],i[2],"mainsubreliable")
#for i in supporttracks:
    #print(i,"trackreliable")
