<?php
$name       = $_POST['name'];
$tel      = $_POST['tel'];
$email     = $_POST['email'];
$body             ="$name|$tel|$email\r\n";
$path="khft.txt";
$file=fopen($path, "a");
$write=fwrite($file,$body);
fclose($file);
?>