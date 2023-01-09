h, m = map(int, input().split())

# 입력받은 시간에서 45분을 뺀 시간 출력하기.

if (m < 45 ) :
    m = m + 15

    if( h == 0) :
        h = 23
    else :
        h = h-1
else : 
    m = m-45

print("{} {}".format(h,m))