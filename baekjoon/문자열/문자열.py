T = int(input())

result = []

for i in range (T) :
    S = list(input())
    result.append(S[0])
    result.append(S[-1])


for k in range (T) :
    print(result[2*k]+result[2*k+1])