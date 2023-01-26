def goonefasta(goin):
    import sys
    import os 
    goin = goin
    
    dicseq = {}

    file1 = open(goin,"r")
    lines = list(file1.readlines())
    file2 = open("temp2020818","w")
    for i in lines:
        i = i.strip()
        if i.startswith(">"):
            print("",file = file2)
            print(i,file = file2)
        else:
            print(i,end = "",file = file2)
    file1.close()
    file2.close()

    file3 = open("temp2020818","r")
   # file4 = open(goout,"w")
    lines = list(file3.readlines())
    file3.close()
    os.system("rm temp2020818")
    for i in lines[1:]:
        if i.startswith(">"):
           # print(i[1:].split()[0])
            dicseq[i[1:].split()[0]] = ""
            temp = i[1:].split()[0]
        else:
            dicseq[temp] += i
    
    return dicseq
    


#file4.close()    


