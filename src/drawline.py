import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def drawline(point,colorselect):
    linepointx = [point[0][0],point[1][0]]
    linepointy = [point[0][1],point[1][1]]
    plt.plot(linepointx, linepointy, color=colorselect,zorder=0)
