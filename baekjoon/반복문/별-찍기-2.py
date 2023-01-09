num = int(input())
# level=1
# for i in range(num) : 
#     for j in range(num) :
#         if (num-level > j ) :
#             print(" ", end="")

#         else :
#             print("*",end="")
#     level += 1
#     print("")

for i in range(num) :
    print(" "*(num-i-1) + "*"*(i+1))