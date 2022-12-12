<head>
		<meta charset="UTF-8">
		
		

	</head>

<?php 
	$home="/";
	if(isset($_REQUEST["idx"])){
		$idx = $_REQUEST["idx"];
	}
//echo "<h1>$idx</h1>"
?>

<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="bitbug_favicon.ico" type="image/x-icon" />
    <title>VSAG</title>
	<link href="bootstrap.min.css" rel="stylesheet">
    <link href="<?php echo $home ?>src/css/animate.css" rel="stylesheet">
    <link href="<?php echo $home ?>src/css/blast.css" rel="stylesheet">
	<link href="base.css" rel="stylesheet">
	<script src="<?php echo $home ?>src/js/angular.min.js"></script>

  </head>

  <body>
  <div  class="bodyContainer">
    
    <nav style="height:50px"  class="navbar navbar-inverse">
      <div style="font-size:20px" class="container nav_menubar">
       <div style="position:absolute; left:50px; top:0px; height:75px">
			<ul class="nav nav-pills">
        <div style="color:#2F4F4F">
			<li  role="presentation" <?php  if($idx==1){echo 'class="active"';} ?>><a href="sequenceextraction.php">Home</a></li>
         </div>
			<li role="presentation" <?php  if($idx==2){echo 'class="active"';} ?>><a href="instruction.php">Instruction</a></li>
         <li role="presentation" <?php  if($idx==2){echo 'class="active"';} ?>><a href="sequenceextraction.php">VSAG</a></li>
         <li role="presentation" <?php  if($idx==2){echo 'class="active"';} ?>><a href="Ricediff.php">Rice differentiation interval</a></li>
        <li role="presentation" <?php  if($idx==2){echo 'class="active"';} ?>><a href="ContactCite.php">Contact&nbsp;&&nbsp;Cite</a></li>
	
  
			</ul>
        </div>
      </div>
   </div>
	</nav>
