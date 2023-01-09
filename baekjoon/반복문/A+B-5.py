
list = []
while (1) :
    a,b =map(int,input().split())
    if (a == 0 and b ==0) :
        for a,b in list :
            print(a+b)
        break 
    else :
        list.append([a,b])  
