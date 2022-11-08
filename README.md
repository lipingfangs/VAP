# VSAG
a programme for visualization of short sequence alignment and path navigation in graphical pan-genome
![out](https://user-images.githubusercontent.com/46209789/200499386-cb1277d2-f323-4829-bdb3-cc9c34a87f35.png)
***Usage***

**Extraction of related main and branch paths based on a certain reference genome interval*
```
 graphsamtools <info.file> <chromosome> <start posistion> <end posistion> <bam file>
```
**For drawing and graph navigation**
```
optional arguments:
  -h, --help            show this help message and exit
  --inindex ININDEX     the index of your data after process of graphsamtools
  --out OUT             The output file name of the image
  --drawtype DRAWTYPE   Types of your data you want to visualization (onlytrack/read/coverage/mutiplesamples)
  --anntracks ANNTRACKS
                        High light the pair-end supported tracks(pathways), default not (0)
  --pairend PAIREND     Display the pair end information or not, default not (0)
  --pairendrange PAIRENDRANGE
                        The search range in the main track, default: 200
  --pairendtheraold PAIRENDTHERAOLD
                        The selected theraold in the main track, default: 1
  --middle MIDDLE       Middle the track and read, default yes (1)
  --geneinfo GENEINFO   bed file contained gene info
  --trackcolor TRACKCOLOR
                        Track colors including main track and the branches default:#CDCD00,#00BFFF
  --readcolor READCOLOR
                        Read colors default:#FFC1C1
  --pairendcolor PAIRENDCOLOR
                        Colors of pair end link default:yellow
  --coveragecolor COVERAGECOLOR
                        coverage colors default:#FF7F50
  --anncolor ANNCOLOR   Read colors default:#D02090
  --genecolor GENECOLOR
                        Gene colors default:black
  --mutilplesamplecolor MUTILPLESAMPLECOLOR
                        Mutilple sample colors default:#FFDEAD,#FFA54F
  --sx SX               Size of X
  --sy SY               Size of Y
  --xlabel XLABEL       Label of your Y axi
  --ylabel YLABEL       Label of your X axi
  --ppi PPI             The dpi of your image
  --imtype IMTYPE       The image type of output;default:png; Support:pdf,svg,jpg

```
