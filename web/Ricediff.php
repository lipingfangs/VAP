<!DOCTYPE html>
<html lang="en">
<?php include '/var/www/html/VSAG/header.php';?>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sequence acquire</title>
    <style type="text/css">
	.tit {
	background:#00FF7F;
	
    
}
			#footer{
		  position: fixed;  
           bottom: 0px;
			}
			.copyright{
		  margin: 0 auto;
			}
	</style>
    <link rel="stylesheet" href="./css/form.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap-theme.min.css" integrity="sha384-6pzBo3FDv/PJ8r2KRkGHifhEocL+1X2rVCTTkUfGk7/0pbek5mMa1upzvWbrUbOZ" crossorigin="anonymous">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" integrity="sha384-HSMxcRTRxnN+Bdg0JdbxYKrThecOKuH5zCYotlSAcp1+c8xmyTe9GYg1l9a69psu" crossorigin="anonymous">
	<link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>
	<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>      
    

<body>
<div class ="tit" style="height:120px">
<h1 class="tit" style="transform:translateY(5px); font-size:50px"> &nbsp;&nbsp;VSAG: PAV differences in rice   </h1> 
    <h3 class="tit" style="transform:translate(-10px)">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Visualization PAV differences between rice subspecies with VSAG </h3>
</div>
 <br>       
<div style='width:450px; height:600px;  transform:translate(20px)' class='panel panel-default'>
     <div class='panel-heading'> <h2 class='panel-title'>Rice</h2></div>
     <div  style='position:absolute; left:0px; top:50px; transform:translate(25px)' class = 'work'>
   <form action="<?php echo $_SERVER["PHP_SELF"] ?>" method="post" enctype="multipart/form-data">
    <!-- enctype="multipart/form-data"作用是给表单添加“添加文件”的功能 -->
          
        <div style="width:400px;" class="input-group input-group-lg">
        <span class="input-group-addon">Chromosome: </span>
        <input style="height:46px" type="text"  name="Chromosome" class="form-control" value="Chr1">
        </div>
         &nbsp;&nbsp;
        <div style="width:400px;" class="input-group input-group-lg">
        <span class="input-group-addon">Start: </span>
        <input style="height:46px" type="text"  name="Start" class="form-control" value="160000">
        </div>
         &nbsp;&nbsp;
        <div style="width:400px;" class="input-group input-group-lg">
        <span class="input-group-addon">End:</span>
        <input style="height:46px" type="text"  name="End" class="form-control" value="170000">
        </div> 
         <br>
         Length of tracks filiter: <input type="int" name="filitertracklengths" value=0> &nbsp;&nbsp;Default: 0</input>
          <br>
          <br>
      <div style="width:400px" class="panel-group" id="accordion">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" 
                       href="#collapseOne">
                        Annotation Option
                    </a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in">
                <div class="panel-body">
                Gene&nbsp;: <input type="checkbox" name="Gene" value="1"/> &nbsp;&nbsp;
                Differential interval&nbsp;:<input type="checkbox" name="Differentialinterval" value="1"/> &nbsp;&nbsp;<br><br>
                Differential colors&nbsp;: <input type="text" name="Differentialcolors" value="pink"></input>
                <br><br>DNA sequencecolors&nbsp;: <input type="checkbox" name="DNAsequence" value="1"/> &nbsp;&nbsp;
                </div>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" 
                       href="#collapseTwo">
                        Colors option
                    </a>
                </h4>
            </div>
            <div id="collapseTwo" class="panel-collapse collapse">
                <div class="panel-body">
                Branch track colors:<input type="text" name="branchcolor" value="green"></input>
                 <br>
                 <br> 
                Main track colors: <input type="text" name="maincolor" value="skyblue"></input>
                 <br>
                 <br>   
                Population colors: <input type="text" name="populationcolor" value="SpringGreen,DodgerBlue"> </input>
                </div>
            </div>
        </div>      
    </div> 
                 <input type="submit" name="submit"   value="Submit">
     </form>   
             
</div>
</div>
<div style='position:absolute; left:500px; top:210px; width:1250px; height:600px; ' class="panel panel-default">
     <div class='panel-heading'> <h2 class='panel-title'>Tracks</h2></div>
     <div  style='position:absolute; left:0px; top:50px; transform:translate(25px)' class = 'work'>
     <?php

//colormodule        
   if(empty($_POST["Chromosome"])){
            $Chromosome =  "Chr1";
            $defaulthead = 1;
        }
    else{
        $Chromosome = $_POST["Chromosome"];
    }
    if(empty($_POST["Start"])){
         $Start = 160000;
        }
    else{
         $Start = $_POST["Start"];
        }
    if(empty($_POST["End"])){
         $End = 170000;
        }
    else{
         $End = $_POST["End"];
        } 
    if($_POST["Differentialinterval"]== NULL){
         $Differentialinterval = 0;
        }
    else{
         $Differentialinterval = 1;
        } 
    if(empty($_POST["Differentialcolors"])){
         $Differentialintervalanncolor = "red";
        }
    else{
         $Differentialintervalanncolor = $_POST["Differentialcolors"];
        }
    if($_POST["DNAsequence"] == NULL){
            $DNAsequence =  0;
        }
    else{
        $DNAsequence =  1;
    }
    if(empty($_POST["branchcolor"])){
         $branchcolor = "PaleGreen";
        }
    else{
         $branchcolor = $_POST["branchcolor"];
        }
    if(empty($_POST["branchcolor"])){
         $maintrackcolor = "skyblue";
        }
    else{
         $maintrackcolor = $_POST["maincolor"];
        }
    if(empty($_POST["populationcolor"])){
         $populationcolor = "SpringGreen,DodgerBlue";
        }
    else{
         $populationcolor = $_POST["populationcolor"];
        }

    if($defaulthead==1){
    echo "<div  style='position:absolute; left:-20px; top:40px; transform:translate(25px)' class = 'work'>
<iframe  style= 'border-radius:25px;'  src='ricedisplay/grapChr1160000170000.html'  name='rightFrame' height= '500px' width='1200px'  noresize='noresize'  id='leftFrame'></iframe>
    </div>";
    }
    
    else
    {
    echo "Processing... may need to wait one to two minutes  ";
    header("Last-Modified: " . gmdate( "D, d M Y H:i:s" ) . "GMT" );
    header("Cache-Control: no-cache, must-revalidate" );
    header("Pragma:no-cache");
    header("Cache-control:no-cache");
    //echo "ricedisplay/graphsamtools ricedisplay/MSUandGFA.onlyothertoMSU.withchrname.clean.chr.inf ".$Chromosome." ".$Start." ".$End."  population ricedisplay/Final_511_PAV.ind.frq,ind ricedisplay/Final_511_PAV.jap.frq,jap ricedisplay/grap".$Chromosome.$Start.$End."<br>";
    system("ricedisplay/graphsamtools ricedisplay/MSUandGFA.onlyothertoMSU.withchrname.clean.chr.inf ".$Chromosome." ".$Start." ".$End."  population ricedisplay/Final_511_PAV.ind.frq,ind ricedisplay/Final_511_PAV.jap.frq,jap ricedisplay/grap".$Chromosome.$Start.$End);
    $filenamewithoutend = "ricedisplay/grap".$Chromosome.$Start.$End;
    $colorconf = "'".$maintrackcolor.",". $branchcolor.",white,white,".$populationcolor."'";
    $Differentialinterval = $Differentialinterval.",".$Differentialintervalanncolor;
    //echo "/home/lfp/miniconda3/envs/py10/bin/python VSAGdr.py /var/www/html/VSAG/".$filenamewithoutend." ".$colorconf." ".$mode." ".$Differentialinterval." ".$DNAsequence;
    system("/home/lfp/miniconda3/envs/py10/bin/python VSAGdr.py /var/www/html/VSAG/".$filenamewithoutend." ".$colorconf." populationfreq ".$Differentialinterval." ".$DNAsequence); 
    echo "";
    echo "<div  style='position:absolute; left:-40px; top:40px; transform:translate(25px)' class = 'work'>
<iframe  style= 'border-radius:25px;'  src='".$filenamewithoutend.".html'  name='rightFrame' height= '500px' width='1200px'  noresize='noresize'  id='leftFrame'></iframe>
    </div>";
        
    }
     


?>          
</div>
</div>
<br>
<br>
<div id="footer" class="copyright" align="center">
     <br>
     <br>
		<p>&copy; 2020-2025 PMBL;South China Agricultural University. All rights reserved.
		&nbsp;<a href= "./introduction.html">Terms of Service</a>
		</p>
</div>             
             
</body>         
        
