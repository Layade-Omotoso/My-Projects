<?php

$conn = mysqli_connect("localhost","root","","omotoso");
$taskname = $_POST['taskname'];
$assignto = $_POST['assignto'];
$timeframe = $_POST['timeframe'];
if($conn){
    // echo "Connected successfully";
    $rand = rand(111,999);
    
    $sql = "INSERT INTO taskinfo (TaskID, TaskName, AssignTo, TimeFrame) VALUES ($rand, '$taskname', '$assignto', $timeframe)";
    if(!mysqli_query($conn,$sql)){
        echo "Could not add new record";
    }
    mysqli_close($conn);

}
header("Location:project.php");