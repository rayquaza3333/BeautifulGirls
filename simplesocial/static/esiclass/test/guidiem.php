<?php
date_default_timezone_set('Asia/Bangkok');
require_once('php/class.phpmailer.php');




    //include("class.smtp.php"); // optional, gets called from within class.phpmailer.php if not already loaded
    $mail             = new PHPMailer();
    $mail -> CharSet = "UTF-8";
    $name       = $_POST['name'];
	$tel      = $_POST['tel'];
	$diem     = $_POST['diem'];
    $body     ="Khach lam bai kiem tra: $name|$tel|Total-Score:$diem\r\n";
    $path="khft.txt";
	$file=fopen($path, "a");
	$write=fwrite($file,$body);
	fclose($file);

    $mail->IsSMTP(); // telling the class to use SMTP
    $mail->Host       = "localhost"; // SMTP server
    $mail->SMTPAuth   = true;                  // enable SMTP authentication
    $mail->SMTPSecure = "ssl";                 // sets the prefix to the servier
    $mail->Host       = "smtp.gmail.com";      // sets GMAIL as the SMTP server
    $mail->Port       = 465;                   // set the SMTP port for the GMAIL server
    $mail->Username   = "gochoruby@gmail.com";
    $mail->Password   = "qryalksqppqrwtqq";           // GMAIL password

    $mail->SetFrom('gochoruby@gmail.com', 'GoChoruby');

    $mail->AddReplyTo("gochoruby@gmail.com","GoChoruby");

    $mail->Subject    = "KHACH LAM BAI KIEM TRA";

    $mail->AltBody    = "KHACH LAM BAI KIEM TRA";

    $mail->MsgHTML($body);

    $address = "sarah.nguyen149@gmail.com";
    $mail->AddAddress($address, "KHACH LAM BAI KIEM TRA");
    $mail->Send();
?>