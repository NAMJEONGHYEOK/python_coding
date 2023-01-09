c = int(input())
case = list()
persent = list()


for i in range(c) :
    case.append(map(int,input().split()))


def avg_rate(list) :
    del list[0]
    avg_score = (sum(list))/(len(list))
    count = 0 
    for j in list :
        if (avg_score < j) :
            count+=1
    return (count*100)/(len(list))

for k in case :
    print("{:5.3f}%".format(avg_rate(list(k))))
