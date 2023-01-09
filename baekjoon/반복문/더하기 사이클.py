
n = int(input())
# n >=0 and n < 100
cycles = 0
temp = n


while 1:
    a = (temp % 10)
    b = (temp // 10) + (temp % 10) 
    c = (a * 10) + (b % 10)
    temp = c
    cycles += 1
    if (temp == n) :
        break


print(cycles)


