<?php
// Muaz Khan     - www.MuazKhan.com 
// MIT License   - https://www.webrtc-experiment.com/licence/
// Documentation - https://github.com/muaz-khan/RecordRTC

header("Access-Control-Allow-Origin: *");
error_reporting(E_ALL);
ini_set('display_errors', 1);

set_error_handler("someFunction");

function someFunction($errno, $errstr) {
    echo '<h2>Upload failed.</h2><br>';
    echo '<p>'.$errstr.'</p>';
}

function selfInvoker()
{
    if (!isset($_POST['audio-filename']) && !isset($_POST['video-filename'])) {
        echo 'Empty file name.';
        return;
    }

    // do NOT allow empty file names
    if (empty($_POST['audio-filename']) && empty($_POST['video-filename'])) {
        echo 'Empty file name.';
        return;
    }

    // do NOT allow third party audio uploads
    if (false && isset($_POST['audio-filename']) && strrpos($_POST['audio-filename'], "RecordRTC-") !== 0) {
        echo 'File name must start with "RecordRTC-"';
        return;
    }

    // do NOT allow third party video uploads
    if (false && isset($_POST['video-filename']) && strrpos($_POST['video-filename'], "RecordRTC-") !== 0) {
        echo 'File name must start with "RecordRTC-"';
        return;
    }
    
    $fileName = '';
    $tempName = '';
    $file_idx = '';
    
    if (!empty($_FILES['audio-blob'])) {
        $file_idx = 'audio-blob';
        $fileName = $_POST['audio-filename'];
        $tempName = $_FILES[$file_idx]['tmp_name'];
    } else {
        $file_idx = 'video-blob';
        $fileName = $_POST['video-filename'];
        $tempName = $_FILES[$file_idx]['tmp_name'];
    }
    
    if (empty($fileName) || empty($tempName)) {
        if(empty($tempName)) {
            echo 'Invalid temp_name: '.$tempName;
            return;
        }

        echo 'Invalid file name: '.$fileName;
        return;
    }

    /*
    $upload_max_filesize = return_bytes(ini_get('upload_max_filesize'));

    if ($_FILES[$file_idx]['size'] > $upload_max_filesize)
       echo 'upload_max_filesize exceeded.';
       return;
    }

    $post_max_size = return_bytes(ini_get('post_max_size'));

    if ($_FILES[$file_idx]['size'] > $post_max_size)
       echo 'post_max_size exceeded.';
       return;
    }
    */

    $filePath = 'uploads/' . $fileName;
    
    // make sure that one can upload only allowed audio/video files
    $allowed = array(
        'webm',
        'wav',
        'mp4',
        "mkv",
        'mp3',
        'ogg'
    );
    $extension = pathinfo($filePath, PATHINFO_EXTENSION);
    if (!$extension || empty($extension) || !in_array($extension, $allowed)) {
        echo 'Invalid file extension: '.$extension;
        return;
    }
    
    if (!move_uploaded_file($tempName, $filePath)) {
        if(!empty($_FILES["file"]["error"])) {
            $listOfErrors = array(
                '1' => 'The uploaded file exceeds the upload_max_filesize directive in php.ini.',
                '2' => 'The uploaded file exceeds the MAX_FILE_SIZE directive that was specified in the HTML form.',
                '3' => 'The uploaded file was only partially uploaded.',
                '4' => 'No file was uploaded.',
                '6' => 'Missing a temporary folder. Introduced in PHP 5.0.3.',
                '7' => 'Failed to write file to disk. Introduced in PHP 5.1.0.',
                '8' => 'A PHP extension stopped the file upload. PHP does not provide a way to ascertain which extension caused the file upload to stop; examining the list of loaded extensions with phpinfo() may help.'
            );
            $error = $_FILES["file"]["error"];

            if(!empty($listOfErrors[$error])) {
                echo $listOfErrors[$error];
            }
            else {
                echo 'Not uploaded because of error #'.$_FILES["file"]["error"];
            }
        }
        else {
            echo 'Problem saving file: '.$tempName;
        }
        return;
    }
    
    echo 'success';

    date_default_timezone_set('Asia/Bangkok');
    require_once('php/class.phpmailer.php');
    //include("class.smtp.php"); // optional, gets called from within class.phpmailer.php if not already loaded
    $mail             = new PHPMailer();
    $mail -> CharSet = "UTF-8";
    $body             ="Khach lam bai kiem tra: http://esiclass.com/test/uploads/$fileName\r\n";

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
}

/*
function return_bytes($val) {
    $val = trim($val);
    $last = strtolower($val[strlen($val)-1]);
    switch($last) {
        // The 'G' modifier is available since PHP 5.1.0
        case 'g':
            $val *= 1024;
        case 'm':
            $val *= 1024;
        case 'k':
            $val *= 1024;
    }

    return $val;
}
*/

selfInvoker();
?>
