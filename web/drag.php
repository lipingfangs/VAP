<!doctype html>

<html>

<head>

<meta charset="utf-8">

<title>JS文件拖拽上传</title>

<style>

p{

 width: 300px;

 height: 300px;

 border:1px dashed #000;

 position:absolute;

 top: 50%;

 left: 50%;

 margin:-150px 0 0 -150px;

 text-align:center;

 font:20px/300px '微软雅黑';

 display:none;

}

</style>

<script>

 window.onload = function () {

  var oBox = document.getElementById('box');

  var oM = document.getElementById('m1');

  var timer = null;

  document.ondragover = function(){

   clearTimeout(timer);

   timer = setTimeout(function(){

    oBox.style.display = 'none';

   },200);

   oBox.style.display = 'block';

  };

  //进入子集的时候 会触发ondragover 频繁触发 不给ondrop机会

  oBox.ondragenter = function(){

   oBox.innerHTML = '请释放鼠标';

  };

  oBox.ondragover = function(){

   return false;

  };

  oBox.ondragleave = function(){

   oBox.innerHTML = '请将文件拖拽到此区域';

  };

  oBox.ondrop = function(ev){

   var oFile = ev.dataTransfer.files[0];

   var reader = new FileReader();

   //读取成功

   reader.onload = function(){

    console.log(reader);

   };

   reader.onloadstart = function(){

    alert('读取开始');

   };

   reader.onloadend = function(){

    alert('读取结束');

   };

   reader.onabort = function(){

    alert('中断');

   };

   reader.onerror = function(){

    alert('读取失败');

   };

   reader.onprogress = function(ev){

    var scale = ev.loaded/ev.total;

    if(scale>=0.5){

     alert(1);

     reader.abort();

    }

    oM.value = scale*100;

   };

   reader.readAsDataURL(oFile,'base64');

   return false;

  };

 };

</script>

</head>

<body>

<meter id="m1" value="0" min="0" max="100"></meter>

 <p id="box">请将文件拖拽到此区域</p>

</body>

</html>

