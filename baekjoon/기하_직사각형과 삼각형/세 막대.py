a,b,c = map(int,input().split())

# 가장 긴 변의 길이가, 나머지 두 변의 길이의 합보다 커야한다

temp = [a,b,c]
maxvalue = int(max(temp))
temp.remove(maxvalue)
sum_temp= sum(temp)

if maxvalue >= sum_temp :
    maxvalue =  sum_temp - 1
    print(maxvalue+sum_temp)
else :
    if (a==b and b==c and a==c) : # 정삼각형
        print(3*a) 
    elif (a==b or b==c or a==c  ) : #이등변 삼각형
        print(a+b+c)
    else :
        print(maxvalue+sum_temp)

