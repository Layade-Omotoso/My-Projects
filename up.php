<?php

$conn = mysqli_connect("localhost","root","","omotoso");
    
$val = $_POST['start'];
$sel = "UPDATE `taskinfo` SET `status` = `status`+1 WHERE `TaskID` = $val";
if(!mysqli_query($conn,$sel)){
    echo "Error occured";
};
mysqli_close($conn);

header("Location:project.php");
