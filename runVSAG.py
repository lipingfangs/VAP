import sys
import os
import argparse
#import VSAG.py
from testv import *
from VSAG import *

def parse_args():
    description = "VSAG is a software for the visualization of short read alignment of  graphical pan-genome"
    parser = argparse.ArgumentParser(description=description)
    #for function
    parser.add_argument('--inindex', type=str, default="graphsamtoolstempdir", help="the index of your data after process of graphsamtools")
    parser.add_argument('--out', type=str, default="out", help='The output file name of the image')
    parser.add_argument('--drawtype', type=str,default="read", help="Types of your data you want to visualization (onlytrack/read/coverage/mutiplesamples)")
    parser.add_argument('--anntracks', type=int,default=0, help="High light the pair-end supported tracks(pathways), default not (0)")
    parser.add_argument('--pairend', type=int,default=0, help="Display the pair end information or not, default not (0) ")
    parser.add_argument('--pairendrange', type=int,default=200, help="The search range in the main track, default: 200")
    parser.add_argument('--pairendtheraold', type=int,default=1, help="The selected theraold in the main track, default: 1")
    parser.add_argument('--middle', type=int,default=1, help="Middle the track and read, default yes (1) ")
    parser.add_argument('--geneinfo', type=str,default="none", help="bed file contained gene info")
    #for color of displayed
    parser.add_argument('--trackcolor', type=str,default="#CDCD00,#00BFFF", help="Track colors including main track and  the branches default:#CDCD00,#00BFFF ")
    parser.add_argument('--readcolor', type=str,default="#FFC1C1", help="Read colors default:#FFC1C1")
    parser.add_argument('--pairendcolor', type=str,default="yellow", help="Colors of pair end link default:yellow")
    parser.add_argument('--coveragecolor', type=str,default="#FF7F50", help="coverage colors default:#FF7F50")
    parser.add_argument('--anncolor', type=str,default="#D02090", help="Read colors default:#D02090")
    parser.add_argument('--genecolor', type=str,default="black", help="Gene colors default:black") 
    parser.add_argument('--mutilplesamplecolor', type=str,default="#FFDEAD,#FFA54F", help="Mutilple sample colors  default:#FFDEAD,#FFA54F")
    
    #for the size and label of picture
    parser.add_argument('--sx', type=int,default=20, help="Size of X")
    parser.add_argument('--sy', type=int,default=8, help="Size of Y")
    parser.add_argument('--xlabel', type=str,default="Position", help="Label of your Y axi")
    parser.add_argument('--ylabel', type=str,default="Pathway", help="Label of your X axi")
    parser.add_argument('--ppi', type=int,default=150, help="The dpi of your image")
    parser.add_argument('--imtype', type=str,default="png", help="The image type of output;default:png; Support:pdf,svg,jpg")
    args = parser.parse_args() 
    return args

if __name__ == '__main__':
    args = parse_args()
    #print(args.ppi)
    #run the main function of VSAG
    mainVSAG(args)
   # test(args)  
