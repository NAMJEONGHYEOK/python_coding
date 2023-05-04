import sys
N, B = sys.stdin.readline().split()
### sol 1
# B = int(B)
# print(int(N,B)) # 자동변환기능 이용하는 방법

### sol 2

B = int(B)

ex = 0
sum = 0
for i in N[::-1] :
    target = int(i) if i.isdigit() else ord(i)-55
    sum +=  target * (B ** ex)
    ex += 1


print(sum)


