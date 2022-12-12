# VSAG
a programme for visualization of short sequence alignment and path navigation in graphical pan-genome
![1670828199388](https://user-images.githubusercontent.com/46209789/206981536-67cf7832-e288-4e54-be32-74f2d368e5a9.png)

***Install***
**Dependency*

Pysam, matplotlib, mpld3, Samtools, Bamtools
php environment (for web), apache (for web)
**Command tools*
```
python setup.py install
```

**web-server*
All pages are packaged in the webserver index. You can directly copy the page to the login index of the server to complete the deployment and make it accessible. If you have any difficulty, Please feel free to contact the author (lpf_bio@foxmail.com)

***Usage***

**Generated the info.file contained graph tracks information*

```
gfatools gfa2fa -s <graph>.GFA > <graph>.fa
python script/getinf.py <graph>.fa > <info.file>

```

**Extraction of related main and branch paths based on a certain reference genome interval*

```
 graphsamtools <info.file> <chromosome> <start posistion> <end posistion> <bam file> <out dir>
```
**Population mode*

```
graphsamtools <info.file> <chromosome> <start posistion> <end posistion> population <population 1>,<population 1 name> <population 2>,<population 2 name> <out dir>

```
**For upload and visualized in Web-sever*

```
tar zcvf <out dir>.tar.gz <out dir>
```
Upload the <out dir>.tar.gz.

**For drawing and graph navigation with command lines*

```

optional arguments:
  -h, --help            show this help message and exit

Input and output:
  --inindex ININDEX     the index of your data after process of graphsamtools
  --out OUT             The output file name of the image
  --geneinfo GENEINFO   bed file contained gene info
  --gff GFF             Annotation file of the graph genome
  --fa FA               Phase the sequence of reliable tracks
  
Function option:
  --drawtype DRAWTYPE   Types of your data you want to visualization (onlytrack/read/coverage/mutiplesamples/Popultaion)
  --anntracks ANNTRACKS
                        High light the pair-end supported tracks(pathways), default not (0)
  --pairend PAIREND     Display the pair end information or not, default not (0)
  --pairendrange PAIRENDRANGE
                        The search range in the main track, default: 200
  --pairendtheraold PAIRENDTHERAOLD
                        The selected theraold in the main track, default: 1
  --gaingene GAINGENE   gain the gene from the gff file, default: 0
  --fl FL               The filter the track lengths below
  --td TD               draw the track direction or not
  --rd RD               draw the read direction or not
  --rn RN               draw the read name or not
  --legend LEGEND       draw the legend or not
  --legendheight LEGENDHEIGHT
                        The height of legend
  --snp SNP             draw the snp information or not (interval<2000bp)
  
Apperance option:
  --middle MIDDLE       Middle the track and read, default yes (1)
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
  --dw DW               web (.html output or not)


```
