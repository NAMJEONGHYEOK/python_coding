N,K = map(int,input().split())

divisor = [] # 약수 리스트 생성

for i in range(1,N+1) :
    if ( N % i == 0 ) : # N을 i로 나눠 떨어지면 i는 N의 약수이다.
            divisor.append(i)
            continue;

if (len(divisor) < K ) :
      print(0)
else :
      print(divisor[K-1])
