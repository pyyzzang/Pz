class HtmlUtil:
    @staticmethod
    def getBodyHead():
        retHttp = '<div class="limiter">                                                           ';
        retHttp += '	<div class="container-table100">                                            ';
        retHttp += '		<div class="wrap-table100">                                             ';
        retHttp += '			<div class="table100">                                              ';
        return retHttp;

    @staticmethod
    def getBodyTail():
        retHttp  = '			</div class="table100">                                              ';
        retHttp += '		</div class="wrap-table100">                                             ';
        retHttp += '	</div class="container-table100">                                            ';
        retHttp += '</div class="limiter">                                                           ';
        return retHttp;
    @staticmethod
    def getHeader():
        retHttp = "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no\" />";
        retHttp += "<script src=\"http://code.jquery.com/jquery-1.11.2.min.js\"></script>"
        retHttp += ' <head>																												';
        retHttp += ' 	<meta charset="UTF-8">                                                                                          ';
        retHttp += ' 	<meta name="viewport" content="width=device-width, initial-scale=1">                                            ';
        retHttp += ' <!--===============================================================================================-->	            ';
        retHttp += ' 	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>                                             ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">                           ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">                ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">                                       ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">                                   ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">                   ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="/static/app/css/util.css">                                                     ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="/static/app/css/main.css?version=1.2">                                                     ';
        retHttp += ' 	<link rel="stylesheet" type="text/css" href="/static/app/css/style.css">                                                     ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += '                                                                                                                     ';
        retHttp += ' <!--===============================================================================================-->	            ';
        retHttp += ' 	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>                                                       ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<script src="vendor/bootstrap/js/popper.js"></script>                                                           ';
        retHttp += ' 	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>                                                    ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<script src="vendor/select2/select2.min.js"></script>                                                           ';
        retHttp += ' <!--===============================================================================================-->              ';
        retHttp += ' 	<script src="js/main.js"></script>                                                                              ';
        retHttp += '                                                                                                                     ';
        retHttp += ' </head>                                                                                                             ';
        return retHttp;