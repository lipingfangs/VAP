<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sequence acquire</title>
    <style type="text/css">
	.tit {
	background: yellowgreen;
	font-size: 30px
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
</head>
<body>
<div >
<h1 class = tit >Show the Graph alignment   </h1> 
<a href="http://RiceGenomicHJX.xiaomy.net" title="Rice HJX74 Genome Database">
Back to main
</a>
<br>
</div>
<br>
<div  class = "work">
    <form action="<?php echo $_SERVER["PHP_SELF"] ?>" method="post" enctype="multipart/form-data">
    <!-- enctype="multipart/form-data"作用是给表单添加“添加文件”的功能 -->
        Main track colors:<input type="text" name="maintrackcolor">&nbsp;&nbsp;Default: Green</input>
	<br>
	<br>
        Branch colores:<input type="text" name="branchcolor">&nbsp;&nbsp;Default: Skyblue</input>
	<br>
	<br>
        Pair end associated colors:<input type="text" name="pecolor"> &nbsp;&nbsp;Default: Yellow</input>
        <br>
	<br>
        Read colors:<input type="text" name="readcolor"> &nbsp;&nbsp;Default: Yellow</input>
        <input type="submit" value="Submit">
    </form>
    <br>
    <br>
    <span>
     <form action="sequenceextraction.php" method="post" enctype="multipart/form-data">
    <label for="file">File name: </label>
    <input type="file" name="file" id="file" value="Select the file from local"><br>
    <input type="submit" name="submit" value="Submit">
    </form>
    </span>
</div>

<br>
<div  class = "work">

<?php
// 允许上传的图片后缀
$allowedExts = array("zip", "docx");
$temp = explode(".", $_FILES["file"]["name"]);
echo "File size ".$_FILES["file"]["size"];
echo "<br>";
print_r($temp);
echo "$temp[0]";
$extension = end($temp);     // 获取文件后缀名
if ((($extension == "gz")
|| ($extension == "zip")
&& ($_FILES["file"]["size"] < 2048000)   // 小于 200 kb
&& in_array($extension, $allowedExts)))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "<li>错误：: " . $_FILES["file"]["error"] . "<\li><br>";
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
        }
        else
        {
            // 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
            move_uploaded_file($_FILES["file"]["tmp_name"], "/var/www/html/VSAG/upload/" . $_FILES["file"]["name"]."tar.gz");
            echo "文件存储在: " . "/var/www/html/VSAG/upload/" . $_FILES["file"]["name"];
        }
    }
}
else
{
    echo "<li>Upload nothing or Invalid file format</li>";

}

system("tar zxvf /var/www/html/VSAG/upload/" . $_FILES["file"]["name"]."tar.gz");
##echo "$temp";
$filenamewithend = $temp[0];
system("/root/miniconda3/bin/python VSAGdr.py /var/www/html/VSAG/".$filenamewithend." '#CDCD00' '#00BFFF' '#FFC1C1' yellow" );
#echo "/root/miniconda3/bin/python VSAGdr.py /var/www/html/VSAG/".$filenamewithend." '#CDCD00' '#00BFFF' '#FFC1C1' yellow";
#echo "$filenamewithend";
?>        
</div>
<div style="float:right;  transform:translateY(-200px)" class = "work">
<div style="float:right;  transform:translate(-100px)" class = "work">
<iframe style='transform:translateY(-280px)' src="displayweb.html"  name='rightFrame' height= '400px' width='1050px'  noresize='noresize'  id='leftFrame'></iframe>
</div>
</div>
<br>

<div id="footer" class="copyright" align="center">
		<p>&copy; 2020-2025 PMBL;South China Agricultural University. All rights reserved.
		&nbsp;<a href= "./introduction.html">Terms of Service</a>
		</p>
</div>
</body>
</html>
<?php
    function register(){
        // Array ( [username] => QQ [nickname] => QQ [age] => 123 [tel] => 123 [gender] => 男 [class] => 1 )
        // print_r($_POST);
        // 验证用户数据是否正确
        if(empty($_POST["maintrackcolor"])){
            echo 'Please select the chromosome like chr01,chr02,chr11';
            // 1.如果在php结构中直接写return,那么当运行到return代码的时候，整个php文件的执行就结束了
            // 2.如果在方法中写return,那么这个return就只能结束这个方法的执行
            return;
        }
        if(!isset($_POST["branchcolor"]) || trim($_POST["branchcolor"]) === ""){
            echo 'Please enter the startpoint like 200000';
            return;
        }
	 if(!isset($_POST["readcolor"]) || trim($_POST["readcolor"]) === ""){
            echo 'Please enter the endpoint like 200000';
            return;
        }

  

        print_r($_POST);
	print "<br>";
        // 数据的写入：明确数据写入的格式 qq|qq|123|123|男|1
        // implode:它可以将关联的数据以指定分隔符链接，转换为字符串，类似于js中的join()
        // explode:它可以将字符串以指定的分隔符分隔，生成关联数组
        $str = implode($_POST,"|");
	print "<br>";
	print($str);
	print "<br>";
    system("rm sites.txt");
        // 将数据写入到文件
	file_put_contents("sites.txt",$str."\n");
	print "<br>";
	print "<br> <p>Output:</p>";
   $seq = system('python seqsec.py');
        

        print "<br>";
	print "<br>";
    	;
}
    // 判断用户是否提交的post请求
    if($_SERVER["REQUEST_METHOD"]==="POST"){
        register();
    }

?>

