# 분해합은 양의정수와 각자리수의 숫자를 더한 값이다. 원본은 생성자 , 결과는 분해합 
# 생성자는 없을수도 여러개일 수 있다. 자연수 n에 대한 가장작은 생성자를 구하는 프로그램 작성하고 없는경우 0 출력

n = int(input())
sol = 0
for i in range(1,n+1) :
    a = list(map(int,str(i)))
    if (n == sum(a) + i) :
       sol = i
       break
print(sol) 