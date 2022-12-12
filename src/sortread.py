import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def sortread(readedistribution,readstart,readend,readbottomtemp):   
    stopsignal = 0
    #print(readedistribution)
    mcount = 0
    while True:
        countn = 0
        mcount += 1
        for i in readedistribution:
            #print(countn)
            #print(len(readedistribution))
            haveusestart = int(i[0])
            haveuseend = int(i[1])
            haveusebottomtemp = float(i[2])
           # print( readbottomtemp,haveusebottomtemp)
            if readbottomtemp == haveusebottomtemp:
                #print("sa",countn)
                if  haveusestart <= readstart <=haveuseend or haveusestart <= readend<=haveuseend:
                    readbottomtemp += 0.075
                    break
            countn +=1
        if countn == len(readedistribution):
            #print(countn,len(readedistribution))
            readedistribution.append([readstart,readend,readbottomtemp])
            break
        if mcount > 15:
            stopsignal = 1
            break
    return readedistribution,readstart,readend,readbottomtemp,stopsignal


