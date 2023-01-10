numbers = list(range(1,10_001))
remove_list=[]    #생성자 리스트
for num in numbers:
    for n in str(num):
        num += int(n)
    
    if num <= 10_000:
        remove_list.append(num)
for remove_num in set(remove_list):
    numbers.remove(remove_num) 
    # del 은 인덱스를 알때 지정 인덱스의 원소를 지움.
    # remove 는 원소를 알때 해당 원소를 제거함.
for self_num in numbers:
    print(self_num)