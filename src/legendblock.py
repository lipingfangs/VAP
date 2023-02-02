import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
def legendblock(colors,text,xpoi,ypoi,legendheight,coefficient,laynum):
    laynumcof = laynum/30
    left, bottom, width, height = (xpoi, ypoi,coefficient,  legendheight) 
    legendblock=mpatches.Rectangle((left,bottom),width,height, 
                                        fill=True,
                                        color=colors,
                                       linewidth=2) 
    plt.text(xpoi,ypoi-0.5,text,fontsize=10)
    return legendblock

