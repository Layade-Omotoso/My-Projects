<?php

$conn = mysqli_connect("localhost","root","","omotoso");
$taskname = mysqli_real_escape_string($conn, $_POST['taskname']);
$assignto = mysqli_real_escape_string($conn, $_POST['assignto']);
$timeframe = mysqli_real_escape_string($conn, $_POST['timeframe']);


$currentdate = date("Y-m-d");
$tframe = "$timeframe DAY";
$date = date_create(date("Y-m-d"));
$start =  date("Y-m-d");
date_add($date, date_interval_create_from_date_string($tframe));
$end = date_format($date, "Y-m-d");

if($conn){
    $rand = rand(1000000,9999999);
    
    $sql = "INSERT INTO taskinfo (`TaskID`, `TaskName`, `AssignTo`, `Start`, `End`) VALUES ($rand, '$taskname', '$assignto', now(), DATE_ADD(now(), INTERVAL $timeframe DAY))";
    if(!mysqli_query($conn,$sql)){
        echo "Could not add new record";
    }
    mysqli_close($conn);

}
header("Location:project.php");