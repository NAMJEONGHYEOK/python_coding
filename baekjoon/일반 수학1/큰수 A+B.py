# alist = list(map(list,input().split()))

# repeat = 0
# alist[0].reverse()
# alist[1].reverse()
# a= alist[0]
# b =alist[1]

# if int(len(a)) > len(b) :
#     repeat =len(a)
#     b.append(0*(repeat-len(b)))
# elif(len(a)<len(b)) :
#     repeat=len(b)
#     a.append(0*(repeat-len(a)))
# else :
#     repeat = len(a)


# d = 0 # 올림수 
# value = []
# for i in range(repeat) :
      
#     if (int(a[i])+int(b[i]) +d >= 10) :
#         value.append(int(a[i])+int(b[i]) +d -10) 
#         d = 1
#         if(i == repeat -1) :
#             value.append(1)
#     else :
#         value.append(int(a[i])+int(b[i]) +d)
#         d = 0

    
# value.reverse()
# for sol in value :
#     print(sol,end="")

a,b =map(int,input().split())
print(a+b)