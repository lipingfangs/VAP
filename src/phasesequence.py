def phasesequence(reliablebed,panfa):
    reliablebedfile= open(reliablebed,"r")
    reliablebedfilelist =   reliablebedfile.readlines()
    reliablebedfile.close()
    dicsort = {}
    sortpoi = []
    reliablebedfilelistsort = []
    for i in reliablebedfilelist:
        if i.find("mainsubreliable"):
            dicsort[ i.split()[1]] = i 
            sortpoi.append(int(i.split()[1]))
        if i.find("trackreliable"):    
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
            dicfa[i] = ""
            temp = i
        else:
            dicfa += i
    for i in reliablebedfilelistsort:
        bedchr = i.split()[0]
        bedstart = int(i.split()[1])
        bedend =  int(i.split()[2])
        if i.find("mainsubreliable"):
            phaseseq += dicfa[bedchr][bedstart-1:bedend]
        if i.find("trackreliable"):
            pathwayseqchr =bedchr+"_"+  bedstart+"_"+bedend
            phaseseq += dicfa[pathwayseqchr]
    return phaseseq

    
