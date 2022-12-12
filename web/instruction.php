<!DOCTYPE html>
<html lang="en">
<?php include 'header.php';?>

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
<div style='width:1400px; height:1000px;  transform:translate(20px)' class='panel panel-default'>
     <div class='panel-heading'> <h2 class='panel-title'>Userage</h2></div>
     <div  style='position:absolute; left:0px; top:50px; transform:translate(25px)' class = 'work'>
        <div>
        <h4>
        <div  style="font-weight:bold"> Introduction</div><br>
        <li> VSAG is a set of multifunctional modules combined with command line and web-sever. It can extract a specific comparison region depending on the reference genome interval to display the comparison between reads and graphical genome path.</li><br>
        <li> VSAG also has population analysis modules and path navigation to realize the identification of the population difference interval.  </li><br>             
        <li>We also developed and integrated a navigation module in VSAG that relies on pair-end information to provide a reference for users.  </li><br>    
       
        <br>
         <div  style="font-weight:bold"> Tutorial </div><br>
         <div style="width:1300px" class="panel-group" id="accordion">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" 
                       href="#collapseOne">
                        Base operation
                    </a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in">
                <div class="panel-body">
                <div style="font-style:italic">*Extraction of related main and branch paths based on a certain reference genome interval</div>
                   <br>
                 <code>graphsamtools info.file chromosome start-posistion end-posistion bam-file outfile </code>
                   <br>
                   <br>
                 <div style="font-style:italic">*Packaging</div>
                   <br>
                  <code>tar zcvf outfile.tar.gz outfile </code>
                   <br>
                   <br>
                 <div style="font-style:italic">*Upload the outfile.tar.gz</div>
  
                </div>
            </div>
        </div>
            
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" 
                       href="#collapseThree">
                       Population and annotation option 
                    </a>
                </h4>
            </div>
            <div id="collapseThree" class="panel-collapse collapse">
                <div class="panel-body">
  
                </div>
            </div>
        </div> 
            
         <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" 
                       href="#collapseTwo">
                        Visualization option
                    </a>
                </h4>
            </div>
            <div id="collapseTwo" class="panel-collapse collapse">
                <div class="panel-body">
  
                </div>
            </div>
        </div> 
         <br>
         <br>
        <div  style="font-weight:bold">Download VSAG</div><br> 
          <a  href="software/VSAG.vt0.75.tar.gz"> VSAG.vt0.75.tar.gz</a>
    </div>
        </h4>
        </div>
     </div>
     </div>       
</body>         
        