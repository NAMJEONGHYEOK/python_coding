# case 1 : 첫 번째 숫자가 두 번쨰 숫자의 약수이다. - factor
# case 2 : 첫 번째 숫자가 두 번째 숫자의 배수이다. - multiple
# case 3 : 첫 번째 숫자가 두 번쨰 숫자의 약수와 배수가 모두 아니다. - neither
# 10000을 넘지 않는 두지연수이며, 마지막 줄에는 0 이 2개 주어진다.

# 0 0 이 입력되기 전까지 a,b 두 수를 입력받는다.
# b가 a로 나눠떨어진다 = 첫 번째 숫자 a가 b의 약수이다. -factor
# a가 b로 나눠 떨어진다 = 첫 번째 숫자 a가 b의 배수이다. - multiple
# 위 두가지가 아닌경우 - neither
# 0 0 입력인 경우 종료


result = [] # 결과를 저장한후 한번에 출력한다.
while(1) : # 0 0 입력 전까지 계속 입력받아야 한다.
    # a,b = input().split()
    a,b = map(int,input().split());

    if (a == 0 and b == 0) : 
        break;

    if ( a % b == 0) :
        result.append("multiple")
        continue;

    elif (b % a == 0) :
        result.append("factor")
        continue;

    else :
        result.append("neither")
        continue;

for i in result :
    print(i)
    