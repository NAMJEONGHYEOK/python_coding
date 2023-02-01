N = int(input()) # N <= 100
inList = list(map(int,input().split()))

n = 1000   
#에라 토스 테네스의 체
sosu = []
a = [False,False] + [True]*(n-1) # 0~1000까지 1001개

for i in range(2,n+1) : # 2~1000까지 1은 소수x,합성수x
    if a[i] :
        sosu.append(i)
        for j in range(2*i,n+1,i): # !! 중요
            a[j] = False

    
# print(sosu) # 에라토스테네스의 체
count = 0
for k in inList :
    if k in sosu :
        count += 1
        
print(count)

