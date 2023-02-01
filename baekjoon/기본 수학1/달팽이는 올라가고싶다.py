import math

a, b, v = map(int,input().split())
# day = 0
# height = 0
# while 1 :
#     height += a
#     day += 1
#     if (height >= v) :
#         break
#     else :
#         height -= b

# print(day)
# 0.15초의 시간제한이므로 반복문을 찾는 것이 아닌 식을 만들어서
# # 출력만 해야한다.

#  = (v-a)/(a-b) +1w
#  = (v-b)/(a-b)
sol = math.ceil((v-b)/(a-b))
print(sol)