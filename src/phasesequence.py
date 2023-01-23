def phasesequence(reliablebed,panfa):
    reliablebedfile= open(reliablebed,"r")
    reliablebedfilelist =   reliablebedfile.readlines()
    reliablebedfile.close()
    dicsortsortpoi = []
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
