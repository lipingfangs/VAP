import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def sortreadnovel(layerend,readstart,readend,readbottomtemp,step):   
    stopsignal = 0
    #print(readedistribution)
    mcount = 0

    while True:
        #countn = 0
        mcount += 1

        if readbottomtemp in list(layerend.keys()):
            haveuseend = layerend[readbottomtemp]
        else:
            layerend[readbottomtemp] = readend
            break
            
        if  haveuseend < readstart:
            layerend[readbottomtemp] = readend
            break
        else:
            readbottomtemp += step
            
        if mcount > 20:
            stopsignal = 1
            break  
                    

    return layerend,readstart,readend,readbottomtemp,stopsignal
