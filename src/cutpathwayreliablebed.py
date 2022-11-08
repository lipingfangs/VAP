import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def cutpathwayreliablebed(pathwaybedfilename,dicpathwaybottom,anncolor,middlethetrackandread):
    dictracks = {}
    readpathwaybedfile = open(pathwaybedfilename,"r")
    readpathwaybedfileline =   readpathwaybedfile.readlines()
    readpathwaybedfile.close()
    annpathwaytracks  = []
    mainbottom = 4.75
    pathwaybottom = 1.75
    pathwaybottomlist = [4.75]
    linepointx = []
    linepointy = []
    annmaintracksublist = []
    for i in readpathwaybedfileline:
        i = i.strip()
        probe = i.split()[3]
        if probe == "mainsubreliable":
            maintrackname = i.split()[0]
            maintrackstart =  int(i.split()[1])
            maintrackend = int(i.split()[2])
            mainlength = maintrackend- maintrackstart
            
            left, bottom, width, height = (maintrackstart, mainbottom,mainlength, 0.5)
            mainrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=anncolor,
                                   linewidth=2)    
            annmaintracksublist.append(mainrected)
            
            dictracks[maintrackname] = [mainbottom+0.5,maintrackstart,maintrackstart]
        else:
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            print(pathwaytrackname)
            pathwaystart = int(i.split()[1])
            pathwaylength = int(i.split()[2])- int(i.split()[1])
            pathwaystartinmain = int(i.split()[3].split("-")[1])
            pathwayendinmain = int(i.split()[3].split("-")[2])
            #print(pathwaystart)
            pathwaybottom = dicpathwaybottom[pathwaytrackname]
            print(pathwaybottom)
            if middlethetrackandread == 1:
                pathwaystartinmain = pathwaystartinmain - (pathwaylength/2)
            left, bottom, width, height = (pathwaystartinmain, pathwaybottom,pathwaylength, 0.5)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=anncolor,
                                   linewidth=2) 
            annpathwaytracks.append(pathwayrected)
            if pathwaybottom >5:
                mainwaysurface = 5.25
            else:
                mainwaysurface = 4.75
            linepointx1 = [pathwaystartinmain ,pathwaystartinmain]
            linepointy1 = [mainwaysurface  ,pathwaybottom]
            linepointx.append(linepointx1)
            linepointy.append(linepointy1)
            
            linepointx2 = [pathwayendinmain,pathwaystartinmain+pathwaylength] 
            linepointy2 = [mainwaysurface ,pathwaybottom]
            linepointx.append(linepointx2)
            linepointy.append(linepointy2)
            dictracks[pathwaytrackname] = [pathwaybottom+0.5,pathwaystart,pathwaystartinmain]
    
    return annmaintracksublist, annpathwaytracks, linepointx, linepointy, dictracks
