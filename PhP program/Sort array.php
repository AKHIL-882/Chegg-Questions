<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <?php
        $sortArray = array("Name"=>"Khaled", "Lastname"=>"Ali", "Course"=>"Internet");

        // Get keys from cities array
    
        print_r(array_values($sortArray));

        // Displaying the content in ascending order of values
        echo "<br>";
        echo "<br>";
        arsort($sortArray);
        foreach($sortArray as $x => $x_value) {
            echo "Key=" . $x . ", Value=" . $x_value;
            echo "<br>";
        }

        // Displaying the content in ascending order of values
        echo "<br>";
        echo "<br>";
        asort($sortArray);
        foreach($sortArray as $x => $x_value) {
        echo "Key=" . $x . ", Value=" . $x_value;
        echo "<br>";
        }
    ?>
    </script>
</head>
<body>
</body>
</html> 