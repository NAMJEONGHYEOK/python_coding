N,M = map(int,input().split())
base = []
count = []
for a in range(N) :
    base.append(input())

for a in range(N-7) :
    for b in range(M-7) :
        w_index = 0 # 흰색시작
        b_index = 0 # 검은색시작

        for i in range(a,a+8) : # 시작지점
            for j in range(b,b+8) : #시작지점
                if (i+j) % 2 == 0  :
                    if base[i][j] != 'W':                
                        w_index += 1
                    else :
                        b_index += 1
                else :
                    if base[i][j] != 'W' :
                      
                        b_index += 1
                    else :
                        w_index += 1
            
        count.append(b_index)
        count.append(w_index)

print(min(count))
    