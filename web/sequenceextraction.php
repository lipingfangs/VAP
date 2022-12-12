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
  
    <script type="text/javascript">
        var xhr;
        var ot;//
        var oloaded;
        //上传文件方法
        function UpladFile() {
            var fileObj = document.getElementById("file").files[0]; // js 获取文件对象
            var url = "uploadFile"; // 接收上传文件的后台地址 
            
            var form = new FormData(); // FormData 对象
            form.append("mf", fileObj); // 文件对象
            
            xhr = new XMLHttpRequest();  // XMLHttpRequest 对象
            xhr.open("post", url, true); //post方式，url为服务器请求地址，true 该参数规定请求是否异步处理。
            xhr.onload = uploadComplete; //请求完成
            xhr.onerror =  uploadFailed; //请求失败
            xhr.upload.onprogress = progressFunction;//【上传进度调用方法实现】
            xhr.upload.onloadstart = function(){//上传开始执行方法
                ot = new Date().getTime();   //设置上传开始时间
                oloaded = 0;//设置上传开始时，以上传的文件大小为0
            };
            xhr.send(form); //开始上传，发送form数据
        }
        //上传进度实现方法，上传过程中会频繁调用该方法
        function progressFunction(evt) {
            
             var progressBar = document.getElementById("progressBar");
             var percentageDiv = document.getElementById("percentage");
             // event.total是需要传输的总字节，event.loaded是已经传输的字节。如果event.lengthComputable不为真，则event.total等于0
             if (evt.lengthComputable) {//
                 progressBar.max = evt.total;
                 progressBar.value = evt.loaded;
                 percentageDiv.innerHTML = Math.round(evt.loaded / evt.total * 100) + "%";
             }
            
            var time = document.getElementById("time");
            var nt = new Date().getTime();//获取当前时间
            var pertime = (nt-ot)/1000; //计算出上次调用该方法时到现在的时间差，单位为s
            ot = new Date().getTime(); //重新赋值时间，用于下次计算
            
            var perload = evt.loaded - oloaded; //计算该分段上传的文件大小，单位b       
            oloaded = evt.loaded;//重新赋值已上传文件大小，用以下次计算
        
            //上传速度计算
            var speed = perload/pertime;//单位b/s
            var bspeed = speed;
            var units = 'b/s';//单位名称
            if(speed/1024>1){
                speed = speed/1024;
                units = 'k/s';
            }
            if(speed/1024>1){
                speed = speed/1024;
                units = 'M/s';
            }
            speed = speed.toFixed(1);
            //剩余时间
            var resttime = ((evt.total-evt.loaded)/bspeed).toFixed(1);
            time.innerHTML = '，速度：'+speed+units+'，剩余时间：'+resttime+'s';
               if(bspeed==0)
                time.innerHTML = '上传已取消';
        }
        //上传成功响应
        function uploadComplete(evt) {
         //服务断接收完文件返回的结果
         //    alert(evt.target.responseText);
             alert("上传成功！");
        }
        //上传失败
        function uploadFailed(evt) {
            alert("上传失败！");
        }
          //取消上传
        function cancleUploadFile(){
            xhr.abort();
        }
    </script>        
</head>
<body>        
<?php
function getDirContent($path){
  if(!is_dir($path)){
    return false;
 }
 $arr = array();
  $data = scandir($path);
  foreach ($data as $value){
    if($value != '.' && $value != '..'){
      $arr[] = $value;
    }
  }
  return $arr;
} 

?>        
        


<div class ="tit" style="height:120px">
<h1 class="tit" style="transform:translateY(5px); font-size:50px"> &nbsp;&nbsp;VSAG   </h1> 
    <h3 class="tit" style="transform:translate(-10px)">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Visualization your alignment with grapical pan-genome</h3>
</div>
<div style="transform:translate(0px);">
<br>   
<a style="transform:translateY(0px);" href="http://RiceGenomicHJX.xiaomy.net" title="Rice HJX74 Genome Database">
&nbsp;&nbsp;&nbsp;&nbsp;Back to main
</a>
<br>
</div>
<br>
<div  class = "work">
    <div style="width:650px; height:650px; transform:translate(20px); " class="panel panel-default"> 
        <div class="panel-heading"> <h3 class="panel-title">Control panel</h3></div>
        <br>
    <div style="transform:translate(10px);">
    <form action="<?php echo $_SERVER["PHP_SELF"] ?>" method="post" enctype="multipart/form-data">
    <!-- enctype="multipart/form-data"作用是给表单添加“添加文件”的功能 -->
         Modes: &nbsp;&nbsp;   
        <input type="radio" name="mode" value="read" />Read &nbsp;&nbsp;
        <input type="radio" name="mode" value="Population" />Population Frequency &nbsp;&nbsp;
        <input type="radio" name="mode" value="Coverages" />Coverages &nbsp;&nbsp;
        <input type="checkbox" name="snp" value="1"/> Display SNP &nbsp;(Length < 1000bp)&nbsp;
     <br>
     <br>  
        <div style="width:400px;" class="input-group input-group-lg">
        <span class="input-group-addon">Main track colors: </span>
        <input style="height:46px" type="text"  name="maintrackcolor" class="form-control" value="Green">
        </div>
	<br>
        <div style="width:400px;" class="input-group input-group-lg">
        <span class="input-group-addon">Branch colores: </span>
        <input style="height:46px" type="text"  name="branchcolor" class="form-control" value="Skyblue">
        </div>
	<br>
        <div style="width:400px;" class="input-group input-group-lg">
        <span class="input-group-addon"> Read colors:</span>
        <input style="height:46px" type="text"  name="readcolor" class="form-control" value="Grey">
        </div>    
   <br>
	<br>
        Length of tracks filiter: <input type="int" name="filitertracklengths"> &nbsp;&nbsp;Default: 0</input>

    <br>       
    <br>
    <div style="width:600px" class="panel-group" id="accordion">
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" 
                       href="#collapseOne">
                        Pair-end and Navigation Option
                    </a>
                </h4>
            </div>
            <div id="collapseOne" class="panel-collapse collapse in">
                <div class="panel-body">
                Pair-end display <input type="checkbox" name="Navigation" value="1"/> &nbsp;&nbsp;
                Pair-end associated colors: <input type="text" name="pecolor"> &nbsp;&nbsp;Default: Yellow</input>
                 <br>
                 <br>
                Navigation <input type="checkbox" name="Navigation" value="1"/> &nbsp;&nbsp; 
                Navigation colors: &nbsp;&nbsp;<input type="text" name="Navigationcolor"> &nbsp;&nbsp;Default: red</input>
                </div>
            </div>
        </div>
        <div class="panel panel-default">
            <div class="panel-heading">
                <h4 class="panel-title">
                    <a data-toggle="collapse" data-parent="#accordion" 
                       href="#collapseTwo">
                        Population and annotation option
                    </a>
                </h4>
            </div>
            <div id="collapseTwo" class="panel-collapse collapse">
                <div class="panel-body">
                Population colors: &nbsp;&nbsp;<input type="text" name="populationcolor"> &nbsp;&nbsp;Default: red,green</input>
                <br>
                Auto annotation <input type="checkbox" name="autoannotation" value="1"/> &nbsp;&nbsp;
                Uploaded the gff file <input type="file" name="gfffile" id="gfffile" value="Select the file from local"> or
                Uploaded the specific bed file<input type="file" name="gfffile" id="gfffile" value="Select the file from local"> 
                 <label for="gfffile">Function locus file name: </label>
                </div>
            </div>
        </div>      
    </div>

    <br>
    <br>

     <br>
     <br>
         
    
    
        
    </div>
    <br>
    <br>
     <div style='position:absolute; left:675px; top:0px; width:700px; height:650px; ' class="panel panel-default"> 
    <div class="panel-heading"> <h3 class="panel-title">Upload file</h3></div>
    <div style='position:absolute; left:25px; top:450px; border-radius:100px;'>
     Select the file from local: &nbsp;&nbsp;<input type="file" name="file" id="file" value="Select the file from local">
     Uploaded:<label for="file"></label>
     <input type="submit" name="submit"  onclick="UpladFile()" value="Submit">
     <input type="button" onclick="cancleUploadFile()" value="取消" />
     <br>
     Upload progress: &nbsp;&nbsp;<progress id="progressBar" value="0" max="100" style="width: 150px;"></progress>
     <span id="percentage"></span><span id="time"></span>
    </div>    
         
    
    <div  style='position:absolute; left:25px; top:50px; border-radius:100px;' class = 'work'>
    <iframe  style= 'border-radius:25px;'  src='upload.php'  name='rightFrame' height= '350px' width='600px'  noresize='noresize'  id='leftFrame'></iframe>
     </div>
     </div>
    </form>
        

</div>

<br>
<div   style="transform:translateY(10px)" class = "work">

<?php
        echo $_POST["Navigation"];
//colormodule        
   if(empty($_POST["maintrackcolor"])){
            $maintrackcolor =  "skyblue";
        }
    else{
        $maintrackcolor = $_POST["maintrackcolor"];
    }
    if(empty($_POST["branchcolor"])){
         $branchcolor = "PaleGreen";
        }
    else{
             $branchcolor = $_POST["branchcolor"];
        }
    if(empty($_POST["readcolor"])){
        $readcolor = "grey";
        }
    else{
        $readcolor = $_POST["readcolor"];
    }
    if(empty($_POST["pecolor"])){
        $pecolor = "yellow";
        }
    else{
        $pecolor = $_POST["pecolor"];
    }
    if(empty($_POST["populationcolor"])){
        $populationcolor = "red,green";
        }
    else{
        $populationcolor = $_POST["populationcolor"];
    }    

    if($_POST["Navigation"] == NULL){
        $navigationornot = "0";
        }
    else{
        $navigationornot = "1";
        if(empty($_POST["Navigationcolor"])){
            $Navigationcolor = "red";
        }
        else{
            $Navigationcolor = $_POST["Navigationcolor"];
        }
        
    }
    if($_POST["snp"] ==  NULL){
        $snpornot = "0";
    }
    else{$snpornot = "1";
        }        
        
// 允许上传的图片后缀
header("Last-Modified: " . gmdate( "D, d M Y H:i:s" ) . "GMT" );
header("Cache-Control: no-cache, must-revalidate" );
header("Pragma:no-cache");
header("Cache-control:no-cache");
$allowedExts = array("zip", "docx");
$temp = explode(".", $_FILES["file"]["name"]);
$gorun = 0;
//echo "File size ".$_FILES["file"]["size"];
//echo "<br>";
//print_r($temp);
//echo "$temp[0]";
$extension = end($temp);     // 获取文件后缀名
if ((($extension == "gz")
|| ($extension == "zip")
&& ($_FILES["file"]["size"] < 2048000)   // 小于 200 kb
&& in_array($extension, $allowedExts)))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "<li>错误：: " . $_FILES["file"]["error"] . "<\li><br>";
        echo "<div  style='position:absolute; left:600px; top:-650px;' class = 'work'>
<iframe  src='displayweb.html'  name='rightFrame' height= '380px' width='1050px'  noresize='noresize'  id='leftFrame'></iframe>";
        
    }
    else
    {
        echo "<li>上传文件名: " . $_FILES["file"]["name"] ."<br>";
        echo "<li>文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "<li>文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
        echo "<li>文件临时存储的位置: " . $_FILES["file"]["tmp_name"] . "<br>";
        // 判断当前目录下的 upload 目录是否存在该文件
        // 如果没有 upload 目录，你需要创建它，upload 目录权限为 777
        if (file_exists("upload/" . $_FILES["file"]["name"]))
        {
            echo $_FILES["file"]["name"] . " 文件已经存在。 ";
            echo "文件存储在: " . "/var/www/html/VSAG/upload/" . $_FILES["file"]["name"];
         
        }
        else
        {    // 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
            move_uploaded_file($_FILES["file"]["tmp_name"], "/var/www/html/VSAG/upload/" . $_FILES["file"]["name"]);
            echo "文件存储在: " . "/var/www/html/VSAG/upload/" . $_FILES["file"]["name"];
                      
        }
        
        system("tar zxvf /var/www/html/VSAG/upload/" . $_FILES["file"]["name"]);
        $dirlist = getDirContent("/var/www/html/VSAG/upload/" . $_FILES["file"]["name"]);
        
            //echo "$temp";
        $filenamewithoutend = $temp[0];
        $colorconf = "'".$maintrackcolor.",". $branchcolor.",".$readcolor.",".$pecolor.",".$populationcolor."'";
            //navigationornot
        $navigation = $navigationornot.",".$Navigationcolor; 
        
        $mode = $_POST["mode"];
        $modeone = "read";
        if(empty($_POST["mode"])){
            $mode = "read";
            $gorun = "1";
        }
        else{
            echo "<br>".$mode.$modeone;
            echo "mode:".$_POST["mode"]."hhhhhhzhzhzhzhhzhz";
            if($_POST["mode"] == "Population" ){ 
            $mode = "populationfreq";
           
            echo "$mode";
            //echo "$dirlist";
            //foreach ( $dirlist as $val ) 
           // { 
               //$tempfilename = explode(".", $val);
               //$valname =  $tempfilename[1];
               //echo "$valname";
              //if($valname == "frq"){
                   $gorun = "1";
               //}
            //}
                                   }
            if($mode=='read'){  
                $mode = "read";
                echo "<br>read hhhhhhhhhh";
                $gorun = "1";
             }
         }   
        echo "<br>".$gorun."sdadadadadadadadad";
        if ($gorun == 1){
        echo "<h3>Processing...</h3>";
        echo "<br>/home/lfp/miniconda3/envs/py10/bin/python VSAGdr.py /var/www/html/VSAG/".$filenamewithoutend." ".$colorconf." ".$mode." ".$navigation." ".$snpornot."<br>";     
        system("/home/lfp/miniconda3/envs/py10/bin/python VSAGdr.py /var/www/html/VSAG/".$filenamewithoutend." ".$colorconf." ".$mode." ".$navigation." ".$snpornot); 
        echo "<li>Track of grapical genome</li>
        <div style='width:1400px; height:500px; border-radius:25px; transform:translate(20px)' class='panel panel-default'>
        <div class='panel-heading'> <h2 class='panel-title'>Tracks</h2></div>
        <div  style='position:absolute; left:0px; top:50px; transform:translate(25px)' class = 'work'>
<iframe   src='".$filenamewithoutend.".html'  name='rightFrame' height= '380px' width='1350px'  noresize='noresize'  id='leftFrame'></iframe>
         </div>
         </div>";  
        echo "<h3>Finish!</h3> <br><br>"; }
                
         else{
         echo "";
         echo "
         <br>
         <div  style='position:absolute; left:0px; top:-170px;' class = 'work'>
         <li>Upload nothing or Invalid file format</li>
    <iframe style= 'border-radius:25px;' src='displayweb.html'  name='rightFrame' height= '600px' width='1400px'  noresize='noresize'  id='leftFrame'></iframe></div>
    <br>
    ";
             }
            }      
       
   }

else{
     echo "";
     echo "<li>Upload nothing or Invalid file format</li>
     <div style='width:1400px; height:500px; border-radius:25px; transform:translate(20px)' class='panel panel-default'>
     <div class='panel-heading'> <h2 class='panel-title'>Tracks</h2></div>
     <div  style='position:absolute; left:0px; top:50px; transform:translate(25px)' class = 'work'>
<iframe style= 'border-radius:25px;' src='displayweb.html'  name='rightFrame' height= '380px' width='1350px'  noresize='noresize'  id='leftFrame'></iframe>
     </div>
     </div>
<br>
";

}
header("Last-Modified: " . gmdate( "D, d M Y H:i:s" ) . "GMT" );
header("Cache-Control: no-cache, must-revalidate" );
header("Pragma:no-cache");
header("Cache-control:no-cache");

?>        
</div>

</div>
<br>

<div id="footer" class="copyright" align="center">
     <br>
     <br>
		<p>&copy; 2020-2025 PMBL;South China Agricultural University. All rights reserved.
		&nbsp;<a href= "./introduction.html">Terms of Service</a>
		</p>
</div>
</body>
</html>


