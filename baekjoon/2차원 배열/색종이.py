paper_length = 10

Count = int(input())

drawing_paper = [[0 for i in range(101)] for i in range(101)]
# 넓이 공식이 아닌 색칠하기 개념으로 접근하자~.

over_lap_count = 0
for i in range(Count) :
    x,y = map(int, input().split())
    
    for j in range(x,x+10) :
        for k in range(y,y+10) :
            drawing_paper[j][k] = 1

for a in drawing_paper :
    over_lap_count += a.count(1)


print(over_lap_count)


