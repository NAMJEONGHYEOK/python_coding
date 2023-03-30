N, M = map (int, input().split()) # N은 바구니의 갯수, M은 테스트 케이스 갯수

basket = [0 for a in range(N)]

for b in range(M) :
    i,j,k = map(int,input().split())
    t = [k] * (j-i+1)
    basket[i-1:j] = t
 

for i in basket :
    print(i, end=" ")