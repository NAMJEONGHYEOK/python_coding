word = input()
# list_alpha = [-1] * 26
list_alpha = [-1 for i in range(26)]
index = 0

for i in word : # 입력받은 글자수 만큼 반복
    x = ord(i)-97
    list_alpha[x] = word.index(i)

for j in list_alpha :
    print(j, end=" ")