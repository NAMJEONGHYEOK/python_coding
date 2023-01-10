word = input().upper()

# list_alpha = [-1] * 26
list_alpha = [0 for i in range(26)]
# upper or lower 함수통해 입력함수 대문자 or 소문자로 구분 처리
# 대문자 출력이므로 65 = A , 97 = a로 사용

for i in word :
    list_alpha[ord(i)-65] += 1

maxindex = 0
maxvalue = 0
doubleCheck = False
for i in list_alpha :
    if (i > maxvalue) :
        doubleCheck = False
        maxvalue = i
        maxindex = list_alpha.index(i)
    elif ( i == maxvalue) :
        doubleCheck = True
        
if (doubleCheck) :
    print("?")
else :
    print(chr(maxindex+65))
