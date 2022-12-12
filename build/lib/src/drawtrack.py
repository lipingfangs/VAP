import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def readpathwaybed(pathwaybedfilename,drawtrackcolor,middlethetrackandread,trackdireactionornot):
    dictracks = {}
    drawmaintrackcolor = drawtrackcolor[0]
    drawpathwaytrackcolor = drawtrackcolor[1]
    readpathwaybedfile = open(pathwaybedfilename,"r")
    readpathwaybedfileline =   readpathwaybedfile.readlines()
    readpathwaybedfile.close()
    pathwaytracks  = []
    mainbottom = 4.75
    pathwaybottom = 1.75
    pathwaybottomlist = [4.75]
    linepointx = []
    linepointy = []
    dicpathwaybottom = {}
    tempdirectionlist = []
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
            #direction
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
            dictracks[maintrackname] = [mainbottom+0.5,maintrackstart,maintrackstart]
        else:
            pathwaytrackname =  i.split()[0]+"_"+i.split()[1]+"_"+i.split()[2]
            print(pathwaytrackname)
            pathwaystart = int(i.split()[1])
            pathwaylength = int(i.split()[2])- int(i.split()[1])
            pathwaystartinmain = int(i.split()[3].split("-")[1])
            pathwayendinmain = int(i.split()[3].split("-")[2])
            #print(pathwaystart)
            while True:
                if pathwaybottom not in pathwaybottomlist:
                    pathwaybottomlist.append(pathwaybottom)
                    break
                else:
                    pathwaybottom = pathwaybottom+3
            dicpathwaybottom[pathwaytrackname] = pathwaybottom
            if middlethetrackandread == 1:
                pathwaystartinmaintemp = pathwaystartinmain - (pathwaylength/2)
                comback = pathwaystartinmain -  pathwaystartinmaintemp
                nobackpathwayendinmain =  pathwayendinmain
                pathwayendinmain = pathwayendinmain - comback 
                pathwaystartinmain = pathwaystartinmaintemp
            else:
                comback= 0
                
            left, bottom, width, height = (pathwaystartinmain, pathwaybottom,pathwaylength, 0.5)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color=drawpathwaytrackcolor,
                                   linewidth=2) 
            pathwaytracks.append(pathwayrected)
            
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
                
     
            #pathway insertion location
            if pathwaybottom >5:
                mainwaysurface = 5.25
            else:
                mainwaysurface = 4.75
            linepointx1 = [pathwaystartinmain+comback ,pathwaystartinmain] #for the insert posistion
            if pathwaybottom <4.75:
                linepointy1 = [mainwaysurface  ,pathwaybottom+0.5]
            else:
                linepointy1 = [mainwaysurface  ,pathwaybottom]
            linepointx.append(linepointx1)
            linepointy.append(linepointy1)
            left, bottom, width, height = (pathwaystartinmain+comback, 4.65,mainlength/500, 0.7)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color="red",
                                   linewidth=2) 
            pathwaytracks.append(pathwayrected) 
            
            linepointx2 = [pathwayendinmain+comback,pathwaystartinmain+pathwaylength] 
            if pathwaybottom <4.75:
                linepointy2 = [mainwaysurface  ,pathwaybottom+0.5]
            else:
                linepointy2 = [mainwaysurface  ,pathwaybottom]            
            
            linepointx.append(linepointx2)
            linepointy.append(linepointy2)
            left, bottom, width, height = (pathwayendinmain+comback, 4.65,mainlength/500, 0.7)
            pathwayrected=mpatches.Rectangle((left,bottom),width,height, 
                                    fill=True,
                                    color="red",
                                   linewidth=2) 
            pathwaytracks.append(pathwayrected) 
            
            dictracks[pathwaytrackname] = [pathwaybottom+0.5,pathwaystart,pathwaystartinmain]
    print(len(tempdirectionlist))   
    pathwaytracks = pathwaytracks+tempdirectionlist
    return sizetrackx, sizetracky, maintrack, pathwaytracks, linepointx, linepointy, dictracks,dicpathwaybottom,mainlength


        
