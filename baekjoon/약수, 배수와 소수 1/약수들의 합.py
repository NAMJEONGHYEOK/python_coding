while(1) : # -1 입력을 할 경우 멈춘다.
    divisor = []

    n = int(input()) # 정수 n을 입력 받는다.
    if (n == -1) :
        break;

    for i in range(1,n+1) :
        if ( n % i == 0) :
            divisor.append(i) # n의 약수를 추가한다.
    
    if (sum(divisor)-n == n) :# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면 완전수이다.
        sized = len(divisor)
        print("%d =" % divisor[sized-1],end=" ")
        for i in range(sized-1) :
            print("%d" % divisor[i],end="")
            if (i != sized-2) :
                print(" + ",end="")
            else :
                print("")
                break;
    else :
        print("{} is NOT perfect.".format(n))
        # 
        # print("%d is NOT perfect." % n)
            