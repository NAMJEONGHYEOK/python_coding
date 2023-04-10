B, N = input().split()

S1 = list(B)

N = int(N)
ex= 0 
sum = 0
for i in S1[::-1] :
     target = int(i) if i.isdigit() else ord(i)-55
     sum += target * (N ** ex)
     ex += 1

print(sum)
        