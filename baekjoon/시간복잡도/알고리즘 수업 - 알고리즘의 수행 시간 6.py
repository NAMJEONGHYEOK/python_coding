n =int(input())
"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
"""
# count = 0 
# for i in range(1,n-1) :
#     for j in range(i+1,n) :
#         for k in range (j+1,n+1) :
#             count += 1
#             print("count : {}, i : {}, j: {}, k: {}".format(count,i,j,k))


print((n*(n-1)*(n-2))//6)
print(3)