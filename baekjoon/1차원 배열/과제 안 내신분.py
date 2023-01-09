# 배열은 생성이 빠르고 삭제시에는 연결리스트가 유리하나 간단한 문제인 만큼 배열의 삭제를 사용.

students = 30
arr = list(range(1,students+1))
for i in range (28) :
    arr.remove(int(input()))

print("%d" % arr[0])
print("%d" % arr[1])
