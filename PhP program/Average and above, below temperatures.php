
<?php
// initializing the array 
$array = array(78,60,62,68,71,68,73,85,66);
// declaring local variables
$sum=0;
// getting the length of array
$length = count($array);
// finding the sum of all values in array
foreach($array as $ele){
    $sum = $sum + $ele;
}
// calculating the average
$average = round(floatval($sum/$length),2);
// displaying the Average
echo "Average Temperature:".$average."\n";
// displaying the Above and Below Average values
foreach($array as $ele){
    if($ele>$average){
        echo "Above Average ".$ele."\n";
    }else{
        echo "Below Average ".$ele."\n";
    }
}

?>