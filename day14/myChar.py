# 컴퓨터에 내장된 언어 

for i in range(100000):
#     print(i,end="")

    # chr 을 사용하면 다양한 문자들이 나온다
    print(chr(i),end="")
    
    if i % 100 == 0:
        print()
    
# 숫자를 문자로 바꿀 수 있다 - 아스키코드값으로 
# 전각, 반각(작)