import json
import pysam
def extract_node_id(filename):
    nodelist = []
    node_ids = []

    with open(filename, 'r') as file:
        for line in file.readlines():
            json_object = json.loads(line)
            mappings = json_object.get('path', {}).get('mapping', [])
            name =  json_object.get('name')
            node_ids = [name]
            for mapping in mappings:
                node_ids.append(mapping.get('position', {}).get('node_id'))
          #  print(node_ids)
            count = 2
            if len(node_ids) > 2:
                for i in node_ids[1:-1]:
                   # print()
                    if abs(int(node_ids[count]) - int(i)) > 10:
                        nodelist.append(node_ids[0])#,node_ids[count],i])
                        break 
                    count +=1
            node_ids = []
            #print()
    return nodelist


def are_numbers_in_two_intervals(number1, number2, intervals):
    interval_number1 = None
    interval_number2 = None

    # 遍历区间集，检查每个数是否在每个区间内
    for i, interval in enumerate(intervals):
        if interval[0] <= number1 < interval[1]:
            interval_number1 = i
        if interval[0] <= number2 < interval[1]:
            interval_number2 = i

    # 如果两个数都在一个区间内，且这两个区间不同，则返回 True
    return interval_number1 is not None and interval_number2 is not None and interval_number1 != interval_number2

def create_intervals(numbers):
    # 对输入的数字列表进行排序
    numbers.sort()

    # 使用相邻的数字创建区间
    intervals = [[numbers[i], numbers[i + 1]] for i in range(len(numbers) - 1)]

    return intervals

def filiterthenotpairtrack(bam,trackbed,region,numbers,dicreaddetailinf,mode,jsonfile):
    import pysam
    readsbedfile = open(trackbed,"r")
    tracklist =   readsbedfile.readlines()
    readsbedfile.close()
    print(tracklist)
    dictracklist = {}
    for i in tracklist:
        if i.find("main") == -1:
            i = i.split()
            head = "\t".join(i[:3])
            tail = i[3]
            dictracklist[head ] = tail
            
    headpoilist = []
    tailpoilist = []
    cutpointlist = []
    subtracklist = []
    supportsubtracks = []
    alltailpoilist = []
    
    
    bf = pysam.AlignmentFile(bam,"r")
    print("bamfile",bam)
    for i in bf:
        #
        #if str(i).find("Bas") != -1:
        head = str(i.reference_name)
        tail = str(i.next_reference_name)
        readname = str(i.qname)
        headpoi = int(i.pos+1)
        tailchr = str(i.next_reference_name)
        tailpoi = int(i.mpos+1)
        #alltailpoilist.append(int(i.mpos+1))
       # print(head,tail)
        if head != tail :
            if head != "None" and tail != "None":
                headpoilist.append(headpoi)
                tailpoilist.append([tailchr,tailpoi])
    #spporttrackhead = []
    #spporttrackend = []
    #print(headpoilist)
    #print(tailpoilist)
    supporttracks = []
    print("tracklist",tracklist)
    dicsplittrack = {}
    if mode == "gam":
        spiltreadlist = extract_node_id(jsonfile)
        spiltreadlistreliable = []
        for i in spiltreadlist:
            if  i in dicreaddetailinf.keys():

                alltailpoilist.append(dicreaddetailinf[i][-4])
                if dicreaddetailinf[i][2].find("_") != -1:
                    cleantrack = dicreaddetailinf[i][2].replace("_","\t")
                    
                    #print("Scleantrack",cleantrack)
                    if cleantrack not in dicsplittrack.keys():#spiltreadlistreliable:
                        dicsplittrack[cleantrack] = 1
                    else:
                        dicsplittrack[cleantrack] +=1 
         
        for i in dicsplittrack.keys():
            
            if dicsplittrack[i] > 2:
                i = i+"\t" + dictracklist[i]
                supporttracks.append(i)
                print("supporttracksadd",i)
    
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
                    print("supporttracksadd",i)
                    break
                    
        else:
            maintrack = i
            #supporttracks.append(i)
    cutpointlist.append(int(maintrack.split()[1]))
    cutpointlist.append(int(maintrack.split()[2]))
    maintrackchr =  maintrack.split()[0]
    cutpointlist.sort()
    print("cutpointlist",cutpointlist)
    for i in range(len(cutpointlist)):
        if i < len(cutpointlist)-1:
            subtracklist.append([maintrackchr,cutpointlist[i],cutpointlist[i+1]])
            print(maintrackchr,cutpointlist[i],cutpointlist[i+1],"mainsub")
            
    supportsubtracks.append(subtracklist[0])
   # print("subtracklist,alltailpoilist:",subtracklist)#,alltailpoilist)
    for i in tailpoilist:
        alltailpoilist.append(i[1])
       
    print("Second round bam")
    bf = pysam.AlignmentFile(bam,"r")
    for i in bf:
        
        #if str(i).find("Bas") != -1:
        head = str(i.reference_name)
        tail = str(i.next_reference_name)
        readname = str(i.qname)
        headpoi = int(i.pos+1)
        tailchr = str(i.next_reference_name)
        tailpoi = int(i.mpos+1)
        #print(head,tail)

        cutpointlistlist = create_intervals(cutpointlist)
        if head == tail and are_numbers_in_two_intervals(headpoi,tailpoi,cutpointlistlist):
            print("cutinterval",headpoi,tailpoi,cutpointlistlist)
           #if tail > head:
            alltailpoilist.append(tailpoi)
            alltailpoilist.append(headpoi)
        if head != tail:
            print("Diff chr",head,tail,readname)
            alltailpoilist.append(tailpoi)
            alltailpoilist.append(headpoi)
   
    print("alltailpoilist",alltailpoilist)
    for i in subtracklist[1:]:
        #print(i)
        spport = 0
        spporthead = 0
        spporttail = 0
        spportst  = 0
        spported = 0
        mainsubst = i[1]
        mainsubed = i[2]
        alltailpoilistsplist =[]
        for j in alltailpoilist:
            if  mainsubst<= j <= mainsubst+region :
                alltailpoilistsplist.append(j)
                spportst += 1
            if spportst > numbers:
                spporthead += 1  
        if  spporttail>0 or spporthead > 0:
            print("Pairadd one",i,alltailpoilistsplist)
            supportsubtracks.append(i)
            
    if mode == "gam":            
        for i in subtracklist[1:]:
            spportrst =0
            spportred =0
            spporthead = 0
            spporttail = 0
            mainsubst = i[1]
            mainsubed = i[2]
            for k in dicreaddetailinf.keys():
                if dicreaddetailinf[k][2] == i[0]:
                   # print( dicreaddetailinf[k][0],j,dicreaddetailinf[k][-1])
                    if dicreaddetailinf[k][0] < mainsubst <dicreaddetailinf[k][3]:
                        print(dicreaddetailinf[k],mainsubst)
                        spportrst += 1
                    if  dicreaddetailinf[k][0] > mainsubed > dicreaddetailinf[k][3]:
                        print(dicreaddetailinf[k],mainsubed)
                        spportred += 1

                if spportred> 16 or  spportrst > 16:
                    spporttail += 1
                    spporthead +=1
                    break

            if  spporttail>0 or spporthead > 0:
                print("linkadd one",i)
                if i not in supportsubtracks:
                    supportsubtracks.append(i)

    print("supportsubtracks",supportsubtracks) 
    print("supporttracks",supporttracks) 
    return supporttracks,supportsubtracks
