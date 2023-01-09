
## input() 보다 sys.stdin.readline() 사용이 빠르다.

import sys
tc = int(sys.stdin.readline())
result =[]
for i in range(tc) :
    a, b =map(int, sys.stdin.readline().split())
    result.append(a+b)
for j in result :
    print(j)