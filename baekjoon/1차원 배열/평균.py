n = int(input())
score = list(map(int,input().split()))
M = max(score)
S = sum(score)

avg = ( 100 * S ) / (M * n) 

print(avg)
