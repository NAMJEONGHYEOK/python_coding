while(1) :
    a,b,c =map(int,input().split())
    temp = [a,b,c]
    maxvalue = max(temp)
    temp.remove(max(temp))
    if (a == b and b == c and a == 0) :
        break
    if(maxvalue >= sum(temp)) :
        print("Invalid")
    elif( a== b and b==c and a==c) :
        print("Equilateral")
    elif( a==b  or a ==c or b==c)  :
        print("Isosceles")
    else :
        print("Scalene")
    
