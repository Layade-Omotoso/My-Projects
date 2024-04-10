
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta author="Omotoso Layade">
    <title>Omotoso - Project Management</title>
    <style>
        .mainDiv{
            background: #eee;
            border-radius: 10px 10px 10px 0px;
            margin:5px 10px;
            padding: 10px 5px; 
            box-shadow:2px 2px 2px 2px;
            
        }

        #task{
            color:green;
            padding: 10px 2px;
            margin-bottom: 5px;
            
        }

        #ass{
            padding: 2px 10px;
            border:1px solid black;
            align:left;
            border-radius: 5px 5px 5px 0px;
        }

        .ass1{
            padding: 2px 10px;
            border:1px solid black;
            align:left;
            margin-right: 5px;
            border-radius: 5px;
            background: black;
            color:white;
        }

        .tn{
            display: inline;
            padding: 2px 20px;
            align:left;
            margin-right: 5px;
            border-radius: 5px;
            background: blue;
            color:white;
        }


        .action{
            padding: 5px 0px;
            float:right;
            margin-bottom: 5px;
            display:inline-block;
           
        }

        .timef{
            padding: 2px 5px;
            align: right;
            font-size:9pt;
            margin-left: 10px;
        }

        #taskform{
            background: #aaf;
            padding:10px 5px;
            margin:-5px;
        }
        input{
            padding:5px;
            border-radius:5px;

        }
        #tn{
            width:40%;
        }
        #tt{            
            width:20%;
        }
        #tf{            
            width:5%;
        }
        #btn{            
            background:red;
            color:white;
            padding:5px 10px;
        }

        .norecord{
            text-align:center;
            padding:20px;
        }
        .formlabel{
            margin-left:10px;
            border-left: 2px dotted;
            padding-left:5px;
        }
    </style>
    
</head>
<body>
   <div id='taskform'> 

       <form action="insert.php" method="POST">
       <span class='formlabel'>Task Details  </span><input id='tn' type="text" name="taskname"  placeholder='Task Description '>
       <span class='formlabel'>Assign to </span> <input id='tt' type="text" name="assignto"  placeholder='Team Name '>
       <span class='formlabel'>Timeframe </span> <input id='tf' type="number" name="timeframe" placeholder='in days'>
       <input type="submit" value="Add Task" id='btn'>
   </div> 
    
</form>
<hr style='margin-bottom:20px; border:1px dotted'>    


<?php

$conn = mysqli_connect("localhost","root","","omotoso");
echo "<TABLE width='100%' ><tr> <th> NEW TASK </th> <th> RUNNING TASK </th><th> COMPLETED TASK </th>  </tr> <tr>";
// New Task Column
$sel = "SELECT * FROM `taskinfo` WHERE `status` = 0 ORDER BY `SN` ASC";
$result = mysqli_query($conn,$sel);
echo "<td width='33%' valign='top'>";
if(mysqli_num_rows($result)>0){
    // echo "<td width='33%' valign='top'>";
    while($row = mysqli_fetch_assoc($result)){
        echo "<div class='mainDiv'>";
        echo "<DIV id='task'>".$row["TaskName"]." </DIV>";
        echo "<DIV class='to'>";
        echo "<span id='ass'>To: ".$row["AssignTo"]." </span> ";
        echo "<span class='timef'>Start: ".$row["Start"]." </span>";
        echo "<span class='timef'> End: ".$row["End"]." </span>";
        echo "</DIV>";
        echo "<DIV class='to'>";
        echo "<form class='action'action='down.php' method='post'><input type='submit' class='tn' name='del' value='Delete'>";
        echo "<input type='hidden' value=".$row["TaskID"]." name='del'> </form>";
        echo "<form class='action' action='up.php' method='post'><input type='submit' class='tn' name='start' value='Start'>";
        echo "<input type='hidden' value=".$row["TaskID"]." name='start'> </form>";  
        echo "</DIV>" ;
        echo "</div><br>";
        
    }
}
else{
    echo "<DIV class='norecord'> No new task is available</DIV>";
}     
echo "</td>";   


// Running Task Column
$sel = "SELECT * FROM `taskinfo` WHERE `status` = 1 ORDER BY `SN` ASC";
$result = mysqli_query($conn,$sel);
echo "<td width='33%' valign='top'>";

if(mysqli_num_rows($result)>0){
    while($row = mysqli_fetch_assoc($result)){
        echo "<div class='mainDiv'>";
        echo "<DIV id='task'>".$row["TaskName"]." </DIV>";
        echo "<DIV class='to'>";
        echo "<span id='ass'>To: ".$row["AssignTo"]." </span> ";
        echo "<span class='timef'>Start: ".$row["Start"]." </span>";
        echo "<span class='timef'> End: ".$row["End"]." </span>";
        echo "</DIV>";
        echo "<DIV class='to'>";
        echo "<form class='action'action='down.php' method='post'><input type='submit' class='tn' name='del' value='Undo'>";
        echo "<input type='hidden' value=".$row["TaskID"]." name='del'> </form>";
        echo "<form class='action' action='up.php' method='post'><input type='submit' class='tn' name='start' value='Done'>";
        echo "<input type='hidden' value=".$row["TaskID"]." name='start'> </form>";  
        echo "</DIV>" ;
        echo "</div><br>";
        
    }
     
    }
    else{
        echo "<DIV class='norecord'> No task is running</DIV>";
    }     
    echo "</td>"; 

// Task Completed Column
$sel = "SELECT * FROM `taskinfo` WHERE `status` = 2 ORDER BY `SN` ASC";
$result = mysqli_query($conn,$sel);
echo "<td width='33%' valign='top'>";
if(mysqli_num_rows($result)>0){
    while($row = mysqli_fetch_assoc($result)){
        echo "<div class='mainDiv'>";
        echo "<DIV id='task'>".$row["TaskName"]." </DIV>";
        echo "<DIV class='to'>";
        echo "<span id='ass'>To: ".$row["AssignTo"]." </span> ";
        echo "<span class='timef'>Start: ".$row["Start"]." </span>";
        echo "<span class='timef'> End: ".$row["End"]." </span>";
        echo "</DIV>";
        echo "<DIV class='to'>";
        echo "<form class='action' action='up.php' method='post'><input type='submit' class='tn' name='start' value='Trash'>";
        echo "<input type='hidden' value=".$row["TaskID"]." name='start'> </form>";  
        echo "</DIV>" ;
        echo "</div><br>";
        
    }
}
else{
    echo "<DIV class='norecord'>No completed task yet</DIV>";
}     
echo "</td>"; 


// else {
//     echo "Error, no record found!".mysqli_error($conn);
// }
echo "</tr></TABLE>";

mysqli_close($conn);

?>

</body>

</html>

<!-- This is working perfectly. Developed by Omotoso Layade (4/4/2024) -->