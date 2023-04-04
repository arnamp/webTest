<?php
$con  = mysqli_connect("localhost","root","240901","vibra_db");
 if (!$con) {
     # code...
    echo "Problem in database connection! Contact administrator!" . mysqli_error();
 }else{
    $sql1 ="select * from tempgrp";
    $sql2 ="select * from tempgrp2";
    $sql3 = "select * from lightgrp";
    $result1 = mysqli_query($con,$sql1);
    $result2 = mysqli_query($con,$sql2);
    $result3 = mysqli_query($con,$sql3);
    while ($row = mysqli_fetch_array($result1)) { 
        $productname1=$row['DeviceType'];
        $datetime1[]  = date_format(date_create( $row['Uptime']),"Y-M-d H:i:s") ;
        $info1[] = $row['Info'];
    }
    while ($row = mysqli_fetch_array($result2)) { 
        $productname2=$row['DeviceType'];
        $datetime2[]  = date_format(date_create( $row['Uptime']),"Y-M-d H:i:s") ;
        $info2[] = $row['Info'];
    }
    while ($row = mysqli_fetch_array($result3)) { 
      $productname3=$row['DeviceType'];
      $datetime3[]  = date_format(date_create( $row['Uptime']),"Y-M-d H:i:s") ;
      $info3[] = $row['Info'];
    }
 }
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>APA-Vibrate</title>

  <link rel="stylesheet" href="web.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.3.0/css/all.min.css" 
</head>

<body>

    <div class="page"> 
      <div class="sidebar">
        <font size ="5"><center><h1>Graph Status</h1></font></center>
        <div class="sidebar-img">
          <img src="https://cdn.dribbble.com/users/2014359/screenshots/6008317/2.gif" alt="">
        </div>
        
        <div class="menu">
          <b class="cg">Menu</b>
          <div class="Item">
            <div class="sidebar-icon">
              <i class="fa-solid fa-table"></i>
            </div>
            <a href="Dashboard.html"><font size ="5"><b>Dashboard</b></font></a>
          </div>
          <div class="Item" >
            <div class="sidebar-icon">
              <i class="fa-solid fa-eject"></i>
            </div>
            <a href="About.html"><font size ="5"><b>About Project</b></font></a>
          </div><div class="Item">
            <div class="sidebar-icon">
              <i class="fa-solid fa-people-group"></i>
            </div>
            <a href="Member.html"><font size ="5"><b>Members</b></font></a>
          </div>
          <div class="Item Item-active">
            <div class="sidebar-icon">
              <i class="fa-solid fa-chart-line"></i>
            </div> 
            <font size ="5"><b>Graphs</b></font>
          </div>
        </div>
        <div class="end"></div>
        <div class="clock-box">
          <p id="clock"></p>
        </div>
        <script>
          function updateTime() {
            var now = new Date();
            var hours = now.getHours();
            var minutes = now.getMinutes();
            var seconds = now.getSeconds();
    
            // Add leading zeros to minutes and seconds
            minutes = (minutes < 10 ? "0" : "") + minutes;
            seconds = (seconds < 10 ? "0" : "") + seconds;
    
            // Determine AM/PM notation
            var ampm = (hours < 12 ? "AM" : "PM");
            hours = (hours > 12 ? hours - 12 : hours);
            hours = (hours == 0 ? 12 : hours);
    
            // Format the time
            var timeString = hours + ":" + minutes + ":" + seconds + " " + ampm;
    
            // Update the clock element
            document.getElementById("clock").innerHTML = timeString;
          }
    
          // Call the updateTime function every second
          setInterval(updateTime, 1000);
        </script>
        <div class="other">
            <img src="https://s3-us-west-2.amazonaws.com/cbi-image-service-prd/original/3bcb6755-c53c-4f31-9ba0-d198e587b019.jpeg" width="100%"><br><br><br>
            <img src="https://thailandsmartcityexpo.com/wp-content/uploads/2022/11/22611022.png" width="100%"><br><br><br>
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Kmitl.jpg" width="100%"><br><br><br><br><br>
            <center><img src="https://thumbs.gfycat.com/JaggedFlusteredLark-max-1mb.gif" width="70%"></center>
        </div>
      </div>
      <div class="content">
          <div style="width:70%;hieght:10%;text-align:center">
          <div class="page-header"><h2>Graph Status</h2></div>
            <div class="word_device"><?php echo $productname1; ?><br></div>
            <canvas  id="chart1"></canvas> 
            <script src="//code.jquery.com/jquery-1.9.1.js"></script>
            <script src="//cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
                <script type="text/javascript">
                    var ctx1 = document.getElementById("chart1").getContext('2d');
                        var Chart1 = new Chart(ctx1, {
                            type: 'line',
                            data: {
                                labels:<?php echo json_encode($datetime1); ?>,
                                datasets: [{
                                    label:'Temp & Humid 1',
                                    backgroundColor:[
                                    'RGB(0, 0, 255,0.1)'],borderColor:["RGB(255, 99, 71)"],borderWidth:2,
                                    data:<?php echo json_encode($info1); ?>,
                                }]  
                              },
                            options: {
                              legend: {
                                display: false,
    
                                labels: {
                                fontColor: '#FFFFFF',
                                fontFamily: 'Circular Std Book',
                                fontSize: 14,
                                }
                              },
                            }
                          });
                  </script> 
            </div>  
            <div style="width:70%;hieght:10%;text-align:center">
            <div class="page-header"><h2>Graph Status</h2></div>
              <div class="word_device"><?php echo $productname2; ?><br></div>
              <canvas  id="chart2"></canvas>
              <script src="//code.jquery.com/jquery-1.9.1.js"></script>
              <script src="//cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
                  <script type="text/javascript">
                      var ctx2 = document.getElementById("chart2").getContext('2d');
                          var Chart2 = new Chart(ctx2, {
                              type: 'line',
                              data: {
                                  labels:<?php echo json_encode($datetime2); ?>,
                                  datasets: [{
                                      label:'Temp & Humid 2',
                                      backgroundColor:[
                                      'RGB(0, 0, 255,0.1)'],borderColor:["RGB(255, 99, 71)"],borderWidth:2,
                                      data:<?php echo json_encode($info2); ?>,
                                  }]  
                                },
                              options: {
                                legend: {
                                  display: false,
      
                                  labels: {
                                  fontColor: '#FFFFFF',
                                  fontFamily: 'Circular Std Book',
                                  fontSize: 14,
                                  }
                                },
                              }
                            });
                    </script> 
            </div> 
            <div style="width:70%;hieght:10%;text-align:center">
            <div class="page-header"><h2>Graph Status</h2></div>
              <div class="word_device"><?php echo $productname3; ?><br></div>
              <canvas  id="chart3"></canvas>
              <script src="//code.jquery.com/jquery-1.9.1.js"></script>
              <script src="//cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
                  <script type="text/javascript">
                      var ctx3 = document.getElementById("chart3").getContext('2d');
                          var Chart3 = new Chart(ctx3, {
                              type: 'line',
                              data: {
                                  labels:<?php echo json_encode($datetime3); ?>,
                                  datasets: [{
                                      label:'Light',
                                      backgroundColor:[
                                      'RGB(0, 0, 255,0.1)'],borderColor:["RGB(255, 99, 71)"],borderWidth:2,
                                      data:<?php echo json_encode($info3); ?>,
                                  }]  
                                },
                              options: {
                                legend: {
                                  display: false,
      
                                  labels: {
                                  fontColor: '#FFFFFF',
                                  fontFamily: 'Circular Std Book',
                                  fontSize: 14,
                                  }
                                },
                              }
                            });
                    </script> 
              </div> 

        </div>
      </div>
</body>
</html>

