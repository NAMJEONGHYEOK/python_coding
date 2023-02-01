tc = int(input())

result = []

for i in range(tc) :
    a,b,c = map(int,input().split())
   
    if (c % a == 0) :
        floor = a * 100
        unit = c // a
    else :
        floor = (c % a) * 100
        unit = 1 + ( c // a)
    sol = floor + unit
    result.append(sol)

for j in result :
    print(j)

# 호수 처리를 * 100 으로한다.