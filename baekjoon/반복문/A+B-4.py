# 코테에서 입력에 범위가 없는 경우, 종료가 없다? 예외처리 필수 
while(1) :
    try :
        a,b =map(int,input().split())
        print(a+b)
    except :
        break
