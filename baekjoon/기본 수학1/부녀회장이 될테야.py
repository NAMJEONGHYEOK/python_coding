# sol 1 리스트 sum 슬라이싱
# t = int(input())
# sol = []
# for i in range(t):
#     k = int(input())        # 층
#     n = int(input())        # 호
#     people = []    
  
#     base = [i for i in range(1,n+1)] # 0층
#     # print(base)
#     for floor in range(k) :
#         temp = []
#         for unit in range(n) :
#             temp.append(sum(base[:unit+1]))
        
#         base = temp.copy()
#         people.append(base)
        
#     sol.append(base[-1]) # 1부터 n 번째 번호 호출

# for j in sol :
#     print(j)

# sol2 이차원배열

t = int(input())
sol2 = []
#base 2차원 리스트 생성
base = [[ 0 for j in range(15) ]for i in range(15)]
for i in range(15) :
    base[i][1] = 1
    base[0][i] = i

for h in range(1, 15) :
    for k in range(2, 15) :
        base[h][k] = base[h][k-1] +base[h-1][k]

for i in range(t) :
    k = int(input())
    n = int(input())

    result = base[k][n]
    sol2.append(result)

for s in sol2 :
    print(s)