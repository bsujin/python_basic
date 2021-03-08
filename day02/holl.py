import random

mine = input("홀/짝을 선택하시오...")
com =""
rnd = random.random()
if rnd > 0.5 :
    com = "홀"
else:
    com = "짝"
    
result = ""
if mine == com :
    result = "이겼습니다." 
else :
    result = "졌습니다." 
  
print("mine:",mine)    
print("com:",com)         
print("result:",result)    
    