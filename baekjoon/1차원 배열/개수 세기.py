n = int(input())
arr = list(map(int,input().split()))
v = int(input())

count = 0 
def find(num) :
    if(num == v ) :
        return True
    else :
        return False

for i in arr :
    if (find(i)) :
        count += 1
    else :
        continue
print(count)