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
			<h1 class="logo-w3">BÀI KIỂM TRA TRÌNH ĐỘ TIẾNG ANH</h1>
			<div class="w3layouts-main">
				<h2><span>Miễn phí 100%</span></h2>
					<h3>Bạn vui lòng nhập đầy đủ thông tin:</h3>
						<input placeholder="Tên của bạn (VD: Lan)" name="tenhocvien" type="text" class="tenhocvien">
						<input placeholder="Số điện thoại" name="sdthocvien" type="phone" class="sdthocvien">
						<input placeholder="Email" name="emailhocvien" type="email" class="emailhocvien">
						<button onclick="kiemtra()">BẮT ĐẦU LÀM BÀI</button>
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
    function validateEmail(email) {
            var re = /\S+@\S+\.\S+/;
            return re.test(email);
        }
    function kiemtra(){
                sessionStorage.tenhocvien = $("input[name='tenhocvien']").val();
                sessionStorage.sdthocvien = $("input[name='sdthocvien']").val();
    			var phoneno = /^([a-zA-Z0-9_-]){8,11}$/;
				var phoneval = $("input[name='sdthocvien']").val();
                var name = sessionStorage.tenhocvien;
                var tel = sessionStorage.sdthocvien;
                var email = $("input[name='emailhocvien']").val();
    			if($("input[name='tenhocvien']").val() == "")
            {
                alert("Vui lòng nhập Họ tên!");
            }
            else if($("input[name='emailhocvien']").val()=="" || !validateEmail($("input[name='emailhocvien']").val())){
                alert("Email phải hợp lệ !");
                return false;
            }
            else if((!phoneval.match(phoneno)) ){
                alert("Số điện thoại bạn điền không hợp lệ !");
                return false;
            }
            else
            {
                $.ajax({
                    type: "POST",
                    url: "send.php",
                    data: {name:name,tel:tel,email:email},
                    dataType: "html",
                    success: function (msg) {
                        window.location.href = "test.php";
                    },
                    error: function (msg) {
                        bootbox.alert('Có lỗi xảy ra, vui lòng liên hệ Hotline: (028) 668 338 94');
                    }
                });
            }
            }

        </script>
</body>
</html>
