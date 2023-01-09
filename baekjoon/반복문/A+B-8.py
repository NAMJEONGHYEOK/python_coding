import sys

n = int(input())
result = []
for i in range(n) :
    a,b = map(int, sys.stdin.readline().split())
    result.append([a,b])

for t,(a,b)in enumerate(result) :
    print("Case #{}: {} + {} = {}".format(t+1,a,b,a+b))

