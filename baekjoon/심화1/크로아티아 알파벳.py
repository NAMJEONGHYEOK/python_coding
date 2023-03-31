croalpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]

count = 0
s1 = input()

for i in croalpha :
    count += s1.count(i)

for j in croalpha :
    s1.strip(j)

print(len(s1)-count) # 전체 갯수에서 크로아티아 문자 갯수 빼면 전체 알파벳의 갯수
