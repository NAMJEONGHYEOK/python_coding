while True :
    try : 
        print(input())
    except EOFError : # 종결 규칙이 없을 때 아무것도 입력 안했을때 빠져나와야 하므로 End of File Error를 구현해준다.
        break 