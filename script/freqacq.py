#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @name   : freqacq.py
# @author : cat
# @date   : 2023/2/2.

import sys
import os

frqfilename = sys.argv[1]
pathwaybedfile = sys.argv[2]
population = sys.argv[3]

frqfile= open(frqfilename,"r")
frqfilelist =   frqfile.readlines()
frqfile.close()
 
dicfreq = {}
for i in frqfilelist:
    dicfreq[i.split()[1]] = {}
    if i.split()[1] == "A":
        dicfreq[i.split()[1]]["A"] = 1-float(i.split()[4])
        dicfreq[i.split()[1]]["G"] = float(i.split()[4])
    else:
        dicfreq[i.split()[1]]["A"] = float(i.split()[4])
        dicfreq[i.split()[1]]["G"] = 1- float(i.split()[4])
    
pathwaybedfile= open(pathwaybedfilename,"r")
pathwaybedfilelist =   pathwaybedfile.readlines()
pathwaybedfile.close()

for i in pathwaybedfilelist:
    pathchr = i.split()[0]
    pathst = int(i.split()[1])
    pathed = int(i.split()[2])
    for j in dicfreq.keys():
        freqchr = j.split("_")[0]
        freqpoi  = int(j.split("_")[1])
        if freqchr==pathchr and pathst < freqpoi < pathed:
            print(freqpoi-50,freqpoi+50, dicfreq[j]["A"],populationmark)
