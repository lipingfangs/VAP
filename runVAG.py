import sys
import os
import argparse
#import VSAG.py

from VAG import *

def parse_args():
    description = "VSAG is a software for the visualization of short read alignment of  graphical pan-genome"
    parser = argparse.ArgumentParser(description=description)
    
    #for the file operation
    parser.add_argument('--inindex', type=str, default="graphsamtoolstempdir", help="the index of your data after process of graphsamtools")
    parser.add_argument('--out', type=str, default="out", help='The output file name of the image')
    parser.add_argument('--geneinfo', type=str,default="none", help="bed file contained gene info")
    parser.add_argument('--gff', type=str,default="none", help="Annotation file of the graph genome")
    parser.add_argument('--fa', type=str,default="none", help="Phase the sequence of reliable tracks")
    
    #for function
    parser.add_argument('--drawtype', type=str,default="read", help="Types of your data you want to visualization (onlytrack/read/coverage/mutiplesamples/Popultaion)")
    parser.add_argument('--anntracks', type=int,default=0, help="High light the pair-end supported tracks(pathways), default not (0)")
    parser.add_argument('--pairend', type=int,default=0, help="Display the pair end information or not, default not (0) ")
    parser.add_argument('--pairendrange', type=int,default=300, help="The search range in the main track, default: 200")
    parser.add_argument('--pairendtheraold', type=int,default=6, help="The selected theraold in the main track, default: 1")   
    parser.add_argument('--gaingene', type=int,default=0, help="gain the gene from the gff file, default: 0")
    parser.add_argument('--fl', type=int,default=0, help="The filter the track lengths below")
    parser.add_argument('--td', type=int,default=0, help="draw the track direction or not")
    parser.add_argument('--rd', type=int,default=0, help="draw the read direction or not")
    parser.add_argument('--rn', type=int,default=0, help="draw the read name or not")
    parser.add_argument('--legend', type=int,default=1, help="draw the legend or not") 
    parser.add_argument('--legendheight', type=int,default=0.3, help="The height of legend") 
    parser.add_argument('--snp', type=int,default=1, help="draw the snp information or not (interval<2000bp)") 
    parser.add_argument('--onlysv', type=int,default=1, help="Only display the SV large than thersold (default for >5bp) or not") 
    parser.add_argument('--onlysvthersold', type=int,default=5, help="Thersold of length only display the SV large than thersold  or not")
    parser.add_argument('--coveragesteplength', type=int,default=100, help="Length of step with coverage (default for 100bp)") 
    #for color and displayed
    parser.add_argument('--middle', type=int,default=1, help="Middle the track and read, default yes (1) ")
    parser.add_argument('--trackcolor', type=str,default="#CDCD00,#00BFFF", help="Track colors including main track and  the branches default:#CDCD00,#00BFFF ")
    parser.add_argument('--readcolor', type=str,default="#FFC1C1", help="Read colors default:#FFC1C1")
    parser.add_argument('--pairendcolor', type=str,default="yellow", help="Colors of pair end link default:yellow")
    parser.add_argument('--coveragecolor', type=str,default="#FF7F50", help="coverage colors default:#FF7F50")
    parser.add_argument('--anncolor', type=str,default="#D02090", help="Read colors default:#D02090")
    parser.add_argument('--genecolor', type=str,default="black", help="Gene colors default:black") 
    parser.add_argument('--mutilplesamplecolor', type=str,default="#FFDEAD,#FFA54F", help="Mutilple sample colors  default:#FFDEAD,#FFA54F")
    parser.add_argument('--popline', type=int,default=0, help="draw the population distribution with line plot")
    
    #for the size, type and label of picture
    parser.add_argument('--sx', type=int,default=14, help="Size of X")
    parser.add_argument('--sy', type=int,default=4, help="Size of Y")
    parser.add_argument('--xlabel', type=str,default="Position", help="Label of your Y axi")
    parser.add_argument('--ylabel', type=str,default="Pathway", help="Label of your X axi")
    parser.add_argument('--ppi', type=int,default=150, help="The dpi of your image")
    parser.add_argument('--imtype', type=str,default="png", help="The image type of output;default:png; Support:pdf,svg,jpg")
    parser.add_argument('--dw', type=int,default=1, help="web (.html output or not)")
    
    args = parser.parse_args() 
    return args

if __name__ == '__main__':
    args = parse_args()
    #print(args.ppi)
    #run the main function of VSAG
    mainVAG(args)
   # test(args)  
