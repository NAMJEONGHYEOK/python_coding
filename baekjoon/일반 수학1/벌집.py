n = int(input())

i = 1
stair = 1


while 1:
    maxvalue = (6*(stair-1)) + i
    if n > maxvalue :
        i = maxvalue
        stair += 1
    else :
        print(stair)
        break

