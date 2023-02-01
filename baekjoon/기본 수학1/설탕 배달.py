kg = int(input())
count = 0
a = kg
while 1 :
    if a % 5 ==0 :
        count += a // 5
        break
    elif (a % 3 == 0) :
        a -= 3
        count += 1
    elif (a > 5) :
        a -= 5
        count += 1
    else :
        count = -1
        break


print(count)