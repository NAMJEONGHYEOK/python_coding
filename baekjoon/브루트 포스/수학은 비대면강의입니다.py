# import time
# start = time.time()  # 시작 시간 저장
# #최대 공약수를 통해 최소 공배수를 구한다 - 유클리드 호제법\
# def gcd(a,b) :
#     while(b) : # b가 참이다 = 자연수이다 = a%b !=0, 0이면 break
#         a,b = b,a%b
#     return a
        
# def lcm(a,b) :
#     result = a*b//gcd(a,b)
#     return result

# #  ax + by = c
# #  dx + ey = f
# conList =list(map (int,input().split()))

# xlcm = lcm(conList[0],conList[3])

# temp_a = xlcm // conList[0]
# temp_d = -(xlcm // conList[3])

# # ## 연립 계산
# for i in range(len(conList)) :
#     if (i < 3 ) :
#         conList[i] *= temp_a
#     else :
#         conList[i] *= temp_d

# y = (conList[2]+conList[5])//(conList[1]+conList[4]) 
# x = (conList[2]-(conList[1]*y))//conList[0]
# print("{} {}".format(x,y))
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
# 해당 방법으로 실행시 실행시간 오류 초과
#가감법 사용
# import time

# start = time.time()  # 시작 시간 저장
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

a,b,c,d,e,f = map(int,(input().split()))

for x in range(-999,1000) :
    for y in range(-999,1000) :
        if (a*x+b*y) == c and d*x+e*y==f :
            print("{} {}".format(x,y))
            break
    

