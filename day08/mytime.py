import time
import datetime

start =time.time();
time.sleep(1);

end = time.time();

# 시분초 단위로 변환하기 - dateTime import 후 
sec = end - start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)
