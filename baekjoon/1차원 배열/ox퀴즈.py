n = int(input())
arr =[]
sol = []
for i in range(n) :
    arr.append(input())

def scoring (str) :
    count = 0
    score = 0
    for j in list(str) :
        if ( j == 'o' or j =='O') :
            score += count + 1
            count += 1
        else :
            count = 0;
    return score


for k in arr :
    print(scoring(k))