import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from src.sortread import *

def readpathwaybed(pathwaybedfilename,drawtrackcolor,middlethetrackandread,trackdireactionornot):
    dictracks = {}
    drawmaintrackcolor = drawtrackcolor[0]
    drawpathwaytrackcolor = drawtrackcolor[1]
    readpathwaybedfile = open(pathwaybedfilename,"r")
    readpathwaybedfileline =   readpathwaybedfile.readlines()
    readpathwaybedfile.close()
    pathwaytracks  = []
    mainbottom = 2
    pathwaybottom = 1.75
    pathwaybottomlist = [2.75]
    linepointx = []
    linepointy = []
    dicpathwaybottom = {}
    tempdirectionlist = []
    branchdistribution = []
    insertbarlength = 2
    for i in readpathwaybedfileline:
        i = i.strip()
        probe = i.split()[3]
        if probe == "main":
            maintrackname = i.split()[0]
            maintrackstart =  int(i.split()[1])
            maintrackend = int(i.split()[2])
            mainlength = maintrackend- maintrackstart
                
                
                 
            
            sizetrackx = [[maintrackstart,maintrackend],[maintrackstart,maintrackstart]] #the page size placeholder
            sizetracky = [[0,0],[0,10]]
            left, bottom, width, height = (maintrackstart, mainbottom,mainlength, 0.5)
            mainrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=drawmaintrackcolor,
                                   linewidth=2)    
            maintrack = mainrected
            maindirection = i.split()[-1]
            #direction of maintrack
            if trackdireactionornot ==1:
                if maindirection == "Forward":
                    directionrected=mpatches.Arrow(left,bottom,width,0, 
                                            fill=True,
                                            color="#8B7500"
                                           ,width=0.5,lw = 0.5) 
                    
                elif maindirection == "Reverse":
                    directionrected=mpatches.Arrow(left,bottom,-width,0, 
                                            fill=True,
                                            color="#8B658B"
                                           ,width=0.5,lw = 0.5) 
                tempdirectionlist.append( directionrected)            
            dictracks[maintrackname] = [mainbottom+0.5,maintrackstart,maintrackstart,mainlength]
        else:
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            print(pathwaytrackname)
            pathwaystart = int(i.split()[1])
            pathwaylength = int(i.split()[2])- int(i.split()[1])
            pathwaystartinmain = int(i.split()[3].split("-")[1])
            pathwayendinmain = int(i.split()[3].split("-")[2])
            pathwaystartinmainorg = pathwaystartinmain
            pathwayendinmainorg = pathwayendinmain 
            #print(pathwaystart)
            
           # while True:
               # if pathwaybottom not in pathwaybottomlist:
                    #pathwaybottomlist.append(pathwaybottom)
                    #break
                #else:
                    #pathwaybottom = pathwaybottom+3
            
            if middlethetrackandread == 1:
                print(pathwaystartinmain, pathwayendinmain,pathwaylength,"org")
                pathwaymainmiddle = (pathwaystartinmain +  pathwayendinmain)/2
                pathwaymiddle = (pathwaystartinmain +  pathwaystartinmain+pathwaylength)/2
                
                print(pathwaymainmiddle, pathwaymiddle,"middlepoint")
                comback =pathwaymainmiddle - pathwaymiddle 
                print(comback,"comback")
                pathwaystartinmaintemp = pathwaystartinmain + comback
                #comback = pathwaymiddle-  pathwaymainmiddle
                nobackpathwayendinmain =  pathwayendinmain
                pathwayendinmain = pathwayendinmain + comback 
                pathwaystartinmain = pathwaystartinmaintemp
                print(pathwaystartinmain,"finishchange")

            else:
                comback= 0
            pathwaysmainend = pathwaystartinmain+pathwaylength
            pathwaybottomtemp =  mainbottom + 3
            branchdistribution,pathwaystartinmain,pathwaysmainend,pathwaybottom,stopsignal = sortread(branchdistribution,pathwaystartinmain,pathwaysmainend,pathwaybottomtemp,3)    
            #print(pathwaytrackname,branchdistribution)
            #print(pathwaystartinmain,"enter")
            left, bottom, width, height = (pathwaystartinmain, pathwaybottom,pathwaylength, 0.5)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=drawpathwaytrackcolor,
                                   linewidth=2) 
            pathwaytracks.append(pathwayrected)
            dicpathwaybottom[pathwaytrackname] = pathwaybottom
            # direction of branch
            trackdirection = i.split()[-1]
            
            if trackdireactionornot ==1:
                if trackdirection  == "Forward":
                    directionrected=mpatches.Arrow(left,bottom+0.25,width, 0,
                                            fill=True,
                                            color="#8B7500"#,
                                           ,width=0.5,lw = 0.5)
                elif trackdirection  == "Reverse":
                    directionrected=mpatches.Arrow(left+width,bottom+0.25,-width, 0,
                                            fill=True,
                                            color="#8B658B"#,
                                           ,width=0.5,lw = 0.5)                    
                tempdirectionlist.append( directionrected) 
                
            dictracks[pathwaytrackname] = [pathwaybottom+0.5,pathwaystart,pathwaystartinmain,pathwaylength]    
            
    #pathway insertion location    
   
    for i in readpathwaybedfileline[1:]:      
        if  len(i.split()) < 6:
            mainbottomtop = dictracks[readpathwaybedfileline[0].split()[0]][0]
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            pathwaybottomtop =  dictracks[pathwaytrackname][0]
            pathwaystartinmainorg = int(i.split()[3].split("-")[1])
            pathwayendinmainorg = int(i.split()[3].split("-")[2])
            pathwaystartinmain = dictracks[pathwaytrackname][2]
            pathwaylength = dictracks[pathwaytrackname][3]

                    
            linepointx1 = [pathwaystartinmainorg ,pathwaystartinmain] #for the insert posistion
            linepointy1 = [mainbottomtop  ,pathwaybottomtop-0.25]              
            linepointx.append(linepointx1)
            linepointy.append(linepointy1)
            left, bottom, width, height = (pathwaystartinmainorg, mainbottomtop-0.55,insertbarlength, 0.7)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color="red",
                                       linewidth=2) 
            pathwaytracks.append(pathwayrected) 
                
               
            linepointx2 = [pathwayendinmainorg,pathwaystartinmain+pathwaylength] 
            linepointy2 = [mainbottomtop  ,pathwaybottomtop-0.25]         
            linepointx.append(linepointx2)
            linepointy.append(linepointy2)
            left, bottom, width, height = (pathwayendinmainorg, 1.95,insertbarlength, 0.7)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color="red",
                                       linewidth=2) 
            pathwaytracks.append(pathwayrected) 
                
        else:
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            pathwaybottomtop =  dictracks[pathwaytrackname][0]
            pathwaystartinmain = dictracks[pathwaytrackname][2]
            pathwaylength = dictracks[pathwaytrackname][3]
            if i.split()[5].find(":")==-1:
                lastbranchstartname = i.split()[5]
            else:
                lastbranchstartname= i.split()[5].split(":")[0]# +"_"+str(maintrackstart)            
            #lastbranchstartname = i.split()[5]
            lastbranchstartbottomtop = dictracks[lastbranchstartname][0]
            lastbranchstartinmain = dictracks[lastbranchstartname][2]
            if i.split()[5].find(":")==-1:
                lastbranchstartlengthtoadd = int(i.split()[6])-int(lastbranchstartname.split("_")[1])
            else:
                lastbranchstartlengthtoadd = int(i.split()[6])-int(maintrackstart)
            lastbranchstartinmainorg = lastbranchstartinmain + lastbranchstartlengthtoadd
            
            if i.split()[7].find(":")==-1:
                lastbranchendname = i.split()[7]
            else:
                lastbranchendname = i.split()[7].split(":")[0]#+"_"+str(maintrackstart)
                
            lastbranchendbottomtop = dictracks[lastbranchendname][0]
            lastbranchendinmain = dictracks[lastbranchendname][2]
            if i.split()[7].find(":")==-1:
                lastbranchendlengthtoadd = int(i.split()[8])-int(lastbranchendname.split("_")[1])
            else:
                lastbranchendlengthtoadd = int(i.split()[8])-int(maintrackstart)
            lastbranchendinmainorg = lastbranchendinmain + lastbranchendlengthtoadd
             
            
            linepointx1 = [lastbranchstartinmainorg ,pathwaystartinmain] #for the insert posistion
            linepointy1 = [lastbranchstartbottomtop  ,pathwaybottomtop-0.25]    
            linepointx.append(linepointx1)
            linepointy.append(linepointy1)
            
            left, bottom, width, height = (lastbranchstartinmainorg, lastbranchstartbottomtop-0.55,insertbarlength, 0.7)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color="red",
                                       linewidth=2) 
            pathwaytracks.append(pathwayrected) 
                
               
            linepointx2 = [lastbranchendinmainorg,pathwaystartinmain+pathwaylength] 
            linepointy2 = [lastbranchendbottomtop  ,pathwaybottomtop-0.25]         
            linepointx.append(linepointx2)
            linepointy.append(linepointy2)
            
            left, bottom, width, height = (lastbranchendinmainorg, lastbranchstartbottomtop-0.55,insertbarlength, 0.7)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color="red",
                                       linewidth=2) 
            pathwaytracks.append(pathwayrected)             
       
    print(len(tempdirectionlist))   
    pathwaytracks = pathwaytracks+tempdirectionlist
    return sizetrackx, sizetracky, maintrack, pathwaytracks, linepointx, linepointy, dictracks,dicpathwaybottom,mainlength
