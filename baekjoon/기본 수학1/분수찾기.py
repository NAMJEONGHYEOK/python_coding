x = int(input())

#머리찾기 
size = x**(1/2)
size_int = int(x**(1/2))
maxsize = 0
if (size > size_int) :
    maxsize = size_int+1
else :
    maxsize = size_int

# # 

d = 1
a = 1
head = []
while 1 :
    head.append(a)
    if (x < a) :
        break 
    a += d  
    d += 1
    
# true = 왼쪽에서 오른쪽 / false = 오른쪽에서 왼쪽
sol = head.index(a) # 몇번재 대각줄인가
 # 줄 내에서 몇번째 순서인가
order = x -(head[sol-1]) +1 
# print(sol)
# print(order)
sum = sol + 1
if (sol % 2 ==0 ) :
    print("{}/{}".format(order,sum-order))
else :
    print("{}/{}".format(sum-order,order))
