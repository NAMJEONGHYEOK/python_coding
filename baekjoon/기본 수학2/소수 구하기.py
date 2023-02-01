M, N =map(int,input().split())


def chae (n) :
    sosu = []
    a = [False,False] + [True] * (n-1)
    for i in range(2,n+1) : # 범위를 전체 or x**0.5 +1 제곱근으로 한다.
        if a[i] :
            sosu.append(i)
            for j in range(2*i,n+1,i) :
                a[j] = False
    return sosu

b = chae(N)


# print(a)
# print(b)
# print([x for x in b if x not in a])
for x in b : 
    if x >= M : 
        print(x)