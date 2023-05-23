N,M = map(int,input().split())


# N장의 카드를 입력받아 리스트저장
card = list(map(int,input().split()))
findvalue = False
# 리스트 내림차순정렬 9 8 7 6 5 4 ... 1 
card.sort(reverse=True)
sum = 0
for i in range(len(card)) :
    for j in range(i+1,len(card)) :
        for k in range(j+1,len(card)) :
            if (sum < card[i]+card[j]+card[k] and card[i]+card[j]+card[k] <= M) :
                sum = card[i]+card[j]+card[k]
               
print(sum)

