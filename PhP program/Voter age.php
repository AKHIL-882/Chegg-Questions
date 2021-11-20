
<?php
// function declaration
function check_vote() {
    // getting input from user
    $age = (int)readline('Enter an integer: ');
    // checking the eligibility
    if ($age >= 18) {
        echo "You Are Eligible For Vote";
    } else {
        echo "You are not eligible for vote. ";
    }
}
check_vote(); 

?>