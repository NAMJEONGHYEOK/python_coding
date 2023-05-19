a1,a0 = map(int,input().split())
c = int(input())
n = int(input())
result = 1 if (a1-c)*n +a0 <=0 and c>=a1 else 0
print(result)