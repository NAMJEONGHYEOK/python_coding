a, b = map(int, input().split())
c = int(input())

# c의 범위는 0에서 1000 까지이므로 c의 시간을 먼저 계산해서 합산

c1 = c//60 
c2 = c % 60 

# 분단위 부터 처리. 합산할 경우 시간에 영향을 미치기 때문

if (b+c2 > 59) :
    a = a +1
    b = (b+c2) - 60
else :
    b = b+c2

if (a+c1 > 23) :
    a = (a+c1) - 24
else :
    a = a+c1

print("%d %d" % (a,b))

