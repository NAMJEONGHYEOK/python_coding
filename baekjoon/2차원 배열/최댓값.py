M = 10
N = 10
col = 0
row = 0
maxvalue = 0
A = [[ 0 for i in range (1,N) ]for j in range(1,M)]
for a in range(1,N) :
    A[a-1] = list(map(int, input().split()))
   

for j in A :
    if maxvalue < max(j) :
        maxvalue = max(j)
        col = A.index(j)
        row = j.index(max(j))
    else :
        continue

print(maxvalue)
print(col+1,row+1)
