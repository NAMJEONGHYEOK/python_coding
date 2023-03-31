
grade = {
    "A+":4.5, "A0":4.0,
    "B+":3.5, "B0":3.0,
    "C+":2.5,"C0":2.0,
    "D+":1.5,"D0":1.0,
    "F":0        } # p과목의 경우 계산에서 제외

subject = 20
p_count = 0
score = 0
credit = 0
for i in range(subject) : 

    value = list(input().split(" "))

    if value[2] == 'P' :
       
        continue
    else :
        temp = value[2]
        credit += float(value[1]) * grade.get(value[2])
        score += float(value[1])

print(credit/score)