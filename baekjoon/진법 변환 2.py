N, B = map(int,input().split())

a_list = []
while N !=0 :
    a = (N % B)
    if a >= 10  :
        a_list += chr(a+55)
    else :
        a_list += str(a)
    N //= B
for i in a_list[::-1] :
    print(i, end="")
    


    