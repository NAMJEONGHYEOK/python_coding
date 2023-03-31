
# L = 5
# result = ""

# matrix_a = [[-1 for i in range(15)] for i in range(5)]

# Max_len = 0
# temp =[] 
# for i in range(L) :
#     temp = list(input())
#     matrix_a[i][:len(temp)] = temp

#     if len(matrix_a) > Max_len :
#         Max_len = len(temp)
#     else :
#         continue

# for j in range(Max_len) :
#     for k in range(L) :
#         if matrix_a[k][j] != -1 :
#             result += str(matrix_a[k][j])
#         else :
#             continue
# print(result.strip())
        


l = []
result = ''

for i in range(5) :
    l.append(input())

for j in range(max(len(e) for e in l)) :
    for k in range(5) :
        if j <len(l[k]) :
            print(l[k][j], end="")
