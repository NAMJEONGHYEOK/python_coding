N,M = map(int,input().split()) # 바구니 수와 회전 수

# i,j,k 범위 i부터 j까지 바꾸되 기준은 k바구니.
basket = [i for i in range (1,N+1)]
result = []

for i in range(M) :
    i,j,k = map(int, input().split())
    
    temp = basket[k-1:j]+basket[i-1:k-1]
    basket[i-1:j] = temp

for i in basket :
    print(i, end=" ")


