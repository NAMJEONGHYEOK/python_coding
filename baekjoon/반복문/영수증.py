total = int(input())
items = int(input())
sum = 0
for tc in range(items) :
    price, counts = map(int, input().split())
    sum += price * counts

if (total == sum) :
    print("Yes")
else :
    print("No")