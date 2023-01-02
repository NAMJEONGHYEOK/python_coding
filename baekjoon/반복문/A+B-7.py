import sys

n = int(input())
casenum = 0
result = []
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    result.append(a+b)

for j in result :
    casenum += 1
    print("Case #%d: %d" % (casenum,j))