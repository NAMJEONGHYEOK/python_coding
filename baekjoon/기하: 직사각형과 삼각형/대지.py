T = int(input()) # 점의 갯수

x_list = []
y_list = []

for i in range(T) :
    x,y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

value = (max(x_list)-min(x_list)) * (max(y_list)-min(y_list))
# print(max(x_list))
# print(min(x_list))
# print(max(y_list))
# print(min(y_list))

# print("{} {}" % xy_list[0],xy_list[1])
print("%d" % (value) )
