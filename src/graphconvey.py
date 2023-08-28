
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(sequence))

def graphconvey(gfafile,selectref):
    from collections import defaultdict
    with open(gfafile, 'r') as file:
        lines = file.readlines()
    selectref = selectref
    # 使用字典存储每个节点的个体
    node_individuals = defaultdict(set)
    # 存储每个个体的节点顺序
    individual_nodes = defaultdict(list)
    dicseq = {}
    diclength = {}

    for line in lines:
        if line.startswith('S'):
            line =line.strip()
            i = line.split()
            dicseq[i[1]] = i[2]
            diclength[i[1]] = len(i[2])

    dicacc = {}
    for line in lines:
        if line.startswith('P'):   
            line =line.strip()
            i = line.split()
            dicacc[i[1]] = {}
            acc = 0
            for node in i[2].split(","):
                acc += diclength[node[:-1]]
                direaction = node[-1]
                node = node[:-1]
                dicacc[i[1]][node] = [acc,acc-diclength[node],direaction]
    reflist = list(dicacc[selectref].keys())
    reflisting = list(dicacc[selectref].keys())

    runlist = [selectref]
    print(">" + selectref)
    for i in list(dicacc.keys()):

        uniqlist = []
        if i != selectref:
            runlist.append(i) 
            nowlist = list(dicacc[i].keys())
            for j in list(dicacc[i].keys()):
                if j not in reflisting:
                    uniqlist.append(j)
         #   print(i,uniqlist)            
            reflisting = reflisting+uniqlist
            wholeacc = []
            wholeaccname = []

            for j in uniqlist:
                wholeacc.append([dicacc[i][j][1],dicacc[i][j][0]]) 
                wholeaccname.append(j)
            merged_data = []
            merged_row_names = []

            while wholeacc:
                start, end = wholeacc.pop(0)
                row_name = [wholeaccname.pop(0)]
                changed = True
                while changed:
                    changed = False
                    for l, (a, b) in enumerate(wholeacc[:]):
                        if a == end:
                            end = b
                            row_name.append(wholeaccname.pop(l))
                            wholeacc.pop(l)
                            changed = True
                            break
                        if b == start:
                            start = a
                            row_name.insert(0, wholeaccname.pop(l))
                            wholeacc.pop(l)
                            changed = True
                            break
                merged_data.append([start, end])
                merged_row_names.append(row_name)
           # print(merged_data,merged_row_names)
            for j in range(len(merged_row_names)):
                nodepoi = merged_data[j]
                nodename = merged_row_names[j]

                headnodes = nodename[0]
                endnodes = nodename[-1]

                if dicacc[i][headnodes][2] == "+":
                    prevheadnodes = nowlist[nowlist.index(headnodes) -1]
                    nextendnodes =  nowlist[nowlist.index(endnodes) +1]
                else:
                    prevheadnodes = nowlist[nowlist.index(endnodes) +1]
                    nextendnodes =  nowlist[nowlist.index(headnodes) -1]
               # print(nodename,headnodes,endnodes,prevheadnodes,nextendnodes)
                if nowlist.index(headnodes) -1 < 0 or  nowlist.index(headnodes) -1 < 0:
                    continue
                print(">"+i,str(nodepoi[0]),str(nodepoi[1]),sep = "_",end = "\t")
                for k in runlist:

                    if prevheadnodes in dicacc[k].keys():
                         if  dicacc[k][prevheadnodes][2] == "+":
                             print(">"+k+":"+str(dicacc[k][prevheadnodes][0]),end = "\t")
                             break
                         if   dicacc[k][prevheadnodes][2] == "-":
                             print(">"+k+":"+str(dicacc[k][prevheadnodes][1]),end = "\t")
                             break

                for k in runlist:        
                    if   nextendnodes in dicacc[k].keys():
                         print(">"+k+":"+str(dicacc[k][nextendnodes][1]),end = "\t")
                         break
                         if   dicacc[k][nextendnodes][2] == "+":
                             print(">"+k+":"+str(dicacc[k][nextendnodes][0]),end = "\t")
                         if   dicacc[k][nextendnodes][2] == "-":       
                             print(">"+k+":"+str(dicacc[k][nextendnodes][1]),end = "\t")
                print()
