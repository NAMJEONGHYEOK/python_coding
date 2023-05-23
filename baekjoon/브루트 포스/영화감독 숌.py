n = int(input())

count = 0
six_n = 666
while(1) :
    if '666' in str(six_n) :
        count += 1
    if (count == n) : # 입력된 값의 몇번째 수인지 확인하고 브레이크,
        print(six_n)
        break
    six_n +=1

