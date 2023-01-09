n = 10
arr = []
s1 =  set() # 파이썬 공집합 만들기
for i in range (n) :
    arr.append(int(input()))

for j in arr :
    s1.add(j % 42)


print(len(s1))