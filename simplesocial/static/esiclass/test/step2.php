<!DOCTYPE html>
<html lang="vi">
<head>
<title>ESI ENGLISH CLASS</title>
<link rel="shortcut icon" href="images/favicon.png">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link href="assets/style.css" rel="stylesheet" type="text/css" media="all" />
<link href="https://fonts.googleapis.com/css?family=Montserrat:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i&amp;subset=latin-ext,vietnamese" rel="stylesheet">
</head>
<body>
	<!-- main -->
	<div class="main">

		<div class="main-w3l">
			<a class="logo"><img src="images/logo.png"></a>
			<h1 class="logo-w3">BƯỚC 2: KIỂM TRA KHẢ NĂNG PHÁT ÂM</h1>
			<div class="w3layouts-main">
				<h2><span>Lưu ý:</span></h2>
					<h3>BÀI KIỂM TRA PHÁT ÂM YÊU CẦU HỌC VIÊN PHẢI SỬ DỤNG MÁY TÍNH CHẠY HỆ ĐIỀU HÀNH WINDOWS</h3>

						<button onclick="kiemtra()">TIẾP TỤC</button>
			</div>

		<!-- footer -->
		<div class="footer-w3l">
			<p>&copy; 2018 ESI ENGLISH CLASS All rights reserved</p>
		</div>

		<!-- footer -->
		</div>
	</div>
    <script type="text/javascript" src="assets/jquery.js"></script>
    <script type="text/javascript">
    function kiemtra(){
                var name = sessionStorage.tenhocvien;
                var tel = sessionStorage.sdthocvien;
                var diem = sessionStorage.diemhocvien;
                $.ajax({
                    type: "POST",
                    url: "guidiem.php",
                    data: {name:name,tel:tel,diem:diem},
                    dataType: "html",
                    success: function (msg) {
                        window.location.href = "test2.php";
                    },
                    error: function (msg) {
                        bootbox.alert('Có lỗi xảy ra, vui lòng liên hệ Hotline: (028) 668 338 94');
                    }
                });
            }
    </script>
</body>
</html>
