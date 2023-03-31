N,M = map(int, input().split())

# matrix_A = [[0 for column in range(N)] for row in range(M)]
# matrix_B = [[0 for column in range(N)] for row in range(M)]
A = []
B= []
for i in range (2*N) :
    temp = list(map(int, input().split(" ")))
    if (i < N) :
        A.append(temp)
    else :
        B.append(temp)

result = []
for j in range(N) :
    temp2 = []
    for k in range(M) :
        temp2.append(A[j][k]+B[j][k])
    result.append(temp2)

for a in result :
    for b in a :
        print(b,end=" ")
    print()