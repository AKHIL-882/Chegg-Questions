<?php

if(isset($_POST['submit']))
{
	$fname = $_POST['fname'];
	$lname = $_POST['lname'];
	$email = $_POST['email'];
	$dob = $_POST['dob'];
	$address = $_POST['address'];
	echo "First Name : ".$fname."<br>";
	echo "Last Name : ".$lname."<br>";
	echo "Email : ".$email."<br>";
	echo "Date of Birth : ".$dob."<br>";
	echo "Address : ".$address."<br>";
}

?>