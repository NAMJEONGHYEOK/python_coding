
docs = { "Quarter" : 25, "Dime" : 10,
         "Nickel" : 5, "Penny" : 1} # c의 단위는 센트이기 때문이다.

result = [0,0,0,0]
sum = []
T  = int(input())

for i in range(T) :
    c = int(input())
    
    while c != 0 :
        result[0] = c // docs["Quarter"]
        c %= docs["Quarter"]
        result[1] = c // docs["Dime"]
        c %= docs["Dime"]
        result[2] = c // docs["Nickel"]
        c %= docs["Nickel"]
        result[3] = c // docs["Penny"]
        c %= docs["Penny"]
    sum +=result 

for a in range(0,len(sum),4) :
    for b in sum[a:a+4] :
        print(b,end=" ")
    print("")