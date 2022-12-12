<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="keywords" content="html5" />
<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="demo.css">
<link rel="stylesheet" href="dropzone.css">
<style>

</style>
</head>
<body>


		<div class="col-md-12">
			<div class="row" style="margin-top:30px;">
				<div class="col-md-6 col-xs-12 col-md-offset-3">
					<!--<form id="mydropzone" action="/target" class="dropzone"></form>-->
					<div id="mydropzone" class="dropzone" style="height:300px; border-radius:10px;"></div>
				</div>
			</div>
		</div>

    
<div class="container">
    <h1>
<?php 
$path = "uploads/"; 
 
$extArr = array("jpg", "png", "gz"); 
 
if(isset($_POST) and $_SERVER['REQUEST_METHOD'] == "POST"){ 
    $name = $_FILES['file']['name']; 
    $size = $_FILES['file']['size']; 
     
    if(empty($name)){ 
        echo '请选择要上传的图片'; 
        exit; 
    } 
    $ext = extend($name); 
    if(!in_array($ext,$extArr)){ 
        echo '图片格式错误！'; 
        exit; 
    } 
    if($size>(100*1024)){ 
        echo '图片大小不能超过100KB'; 
        exit; 
    } 
    $image_name = time().rand(100,999).".".$ext; 
    $tmp = $_FILES['file']['tmp_name']; 
    if(move_uploaded_file($tmp, $path.$image_name)){ 
        echo '<h1>ok</h1>'; 
    }else{ 
        echo '上传出错了！'; 
    } 
    exit; 
} 
 
//获取文件类型后缀 
function extend($file_name){ 
    $extend = pathinfo($file_name); 
    $extend = strtolower($extend["extension"]); 
    return $extend; 
} 
 ?>
     </h1>
</div>
<script src="dropzone.min.js"></script>
<script>
   var myDropzone = new Dropzone("div#mydropzone", { 
		url: "index.php",
		paramName: "file",
		maxFilesize: 0.5, // MB
		maxFiles: 5,
		acceptedFiles: ".jpg,.png,.gz"
   });
</script>

</body>
</html>