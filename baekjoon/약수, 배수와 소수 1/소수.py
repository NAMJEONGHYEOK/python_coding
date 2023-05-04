M, N =map(int,input().split())


def chae (n) :
    sosu = []
    a = [False,False] + [True] * (n-1)
    for i in range(2,n+1) :
        if a[i] :
            sosu.append(i)
            for j in range(2*i,n+1,i) :
                a[j] = False
    return sosu

a = chae(M-1)
b = chae(N)
c = [x for x in b if x not in a] # b-a list
# print(a)
# print(b)
# print([x for x in b if x not in a])
if c :
    print(sum(c))
    print(min(c))
else :
    print(-1)