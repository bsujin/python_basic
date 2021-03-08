import logging

# 로거명 설정 
mylogger = logging.getLogger("my")

# 로거 레벨 설정
mylogger.setLevel(logging.DEBUG)

# 포맷 설정 변수 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 정보 출력 위치 설정 
# 1. StreamHandler : console에 출력 
stream_hander = logging.StreamHandler()

# 출력 포맷 설정 
stream_hander.setFormatter(formatter)

# 로거명에 핸들러 적용 
mylogger.addHandler(stream_hander)

# 2. 파일에 저장 : 로그 저장될 파일 설정 및 파일명 설정
file_handler = logging.FileHandler('my.log')

# 로그 저장시 포맷설정 
file_handler.setFormatter(formatter)

# 로거명에 파일 핸들러 적용 
mylogger.addHandler(file_handler)

# 단계에 따른 로거 출력 
mylogger.info("info")
mylogger.debug("i'm debug")
mylogger.warn("i'm warn")
mylogger.warning("i'm warning")
mylogger.error("i'm error")
mylogger.critical("i'm critical")

