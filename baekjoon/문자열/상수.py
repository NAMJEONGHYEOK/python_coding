A, B =map(int, input().split())

C = list(str(A))
D = list(str(B))

C.reverse()
D.reverse()

C = int(''.join(C))
D = int(''.join(D))

if (C > D) :
    print(C)
else :
    print(D)