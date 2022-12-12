<form action="<?php echo $_SERVER["PHP_SELF"] ?>" method="post" enctype="multipart/form-data">
    <!-- enctype="multipart/form-data"作用是给表单添加“添加文件”的功能 -->
        Main track colors: <input type="text" name="maintrackcolor">&nbsp;&nbsp;Default: Green</input>
	<br>
	<br>
        Branch colores: <input type="text" name="branchcolor">&nbsp;&nbsp;Default: Skyblue</input>
	<br>
	<br>
        Pair end associated colors: <input type="text" name="pecolor"> &nbsp;&nbsp;Default: Yellow</input>
    <br>
	<br>
        Read colors: <input type="text" name="readcolor"> &nbsp;&nbsp;Default: Yellow</input>
    <br>
    <br>
        Navigation <input type="checkbox" name="Navigation" value="1"/> &nbsp;&nbsp; 
        Navigation colors: &nbsp;&nbsp;<input type="text" name="Navigationcolor"> &nbsp;&nbsp;Default: red</input>
    <br>
    <br>
     <label for="file">File name: </label>
    <input type="file" name="file" id="file" value="Select the file from local">
     <br>
     <br>
     Modes:    
    <input type="radio" name="mode" value="read" />Read &nbsp;&nbsp;
    <input type="radio" name="mode" value="Population" />Population Frequency &nbsp;&nbsp;
     Population Numbers: 
     <select name="coveragenum">
         <option value="1">1</option>
         <option value="2">2</option>
     </select>&nbsp;&nbsp;
     <br>
     <br>      
     Population colors: &nbsp;&nbsp;<input type="text" name="populationcolor"> &nbsp;&nbsp;Default: red,green</input>
     <br>
     <br>
         
    <label for="file">Coverage File name: </label>
    <input type="file" name="covfile" id="file" value="Select the file from local"><br>
    <br>
    <input type="submit" name="submit" value="Submit">
    </form>
        
        
 <?php   
        echo $_POST["Navigation"];
        echo "sasasasasa";
        if($_POST["Navigation"] == "1"){
        $navigationornot = "1";
        if(empty($_POST["Navigationcolor"])){
            $Navigationcolor = "red";
        }
        else{
            $Navigationcolor = $_POST["Navigationcolor"];
        }
        
    }
    else{$navigationornot = "0";
        }  


if($_POST["mode"]=='read'){
    //
    echo 'readisme';}
    
 

?>