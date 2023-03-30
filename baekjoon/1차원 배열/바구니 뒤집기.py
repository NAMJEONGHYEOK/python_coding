N, M = map(int, input().split())

basket = [ i  for i in range(1,N+1)]

for a in range(M) :
    i,j= map(int,input().split())
    temp = basket[i-1:j]
    temp = temp[::-1]
    basket[i-1:j] = temp


for b in basket :
    print( b, end=" ") 