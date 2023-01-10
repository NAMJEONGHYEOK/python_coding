dial = [i for i in range(1,13)] # 걸리는 초
patturn = [3,3,3,3,3,4,3,4]

s1 = input()
slist = list(s1)

slist_ord = []
solve_ord = []
for i in slist :
    slist_ord.append(ord(i)-65)
slist_ord

time = 0
count = 2 # 2부터 시작 
for j in slist_ord :
    for k in patturn :
        if (j // k > 0 ) :
              j -= k
              count += 1
        else :
            solve_ord.append(count)
            count = 2
            break

for index in solve_ord :
    time += dial[index]
print(time)

