<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<%-- <script src="<%=request.getContextPath()%>/js/kakao.js"></script> --%>
<script src="//developers.kakao.com/sdk/js/kakao.min.js"></script>
<script
	src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>



	<a id="navi" href="#" onclick="navi();"> <img
		src="https://developers.kakao.com/assets/img/about/buttons/navi/kakaonavi_btn_medium.png" />
	</a>
	<script type="text/javascript">
	
    // 사용할 앱의 JavaScript 키를 설정
    Kakao.init('4c01c20d65544d5128336ce2a956d578');
    
    // 카카오 내비 버튼을 생성합니다.
  function navi() {
    Kakao.Navi.start({
      name: '유성온천역',
      x: 127.341432252612,
      y: 36.35451222722343,
      coordType: 'wgs84',
    })
  }
</script>
</body>
</html>