N = int(input())
value = N # 나눈 값을 저장하기 위한 변수
result = []
i=2
while (value >= i) :

    if (value % i == 0) : # i로 나눠 떨어지는 것만 i를 추가.
        result.append(i)
        value //= i # 정수 몫을 저장
     
    else :
        i += 1
        
for i in result :
    print(i)