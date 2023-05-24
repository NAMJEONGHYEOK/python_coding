num = [1,4,8,9,7,1,4,5,3,47,14,85]
# # 특정 노드를 기준으로 위로 올라가는 방법
# def heap_sort(unsorted):
#     n = len(unsorted)
#     #최대 힙 만들기
#     #최소힙은 부등호만 반대로 바꿔주면 됨
#     for i in range(1, n):
#         child = i
#         while child != 0:
#             parent = (child-1)//2
#             if unsorted[parent] > unsorted[child]:
#                 unsorted[parent], unsorted[child] = unsorted[child], unsorted[parent]
#             child = parent #최대값이 루트까지 도달 할 수 있도록

#     #힙 만들기
#     for node in range(n-1, -1, -1): # 
#         #루트 노드와 마지막 노드를 교환
#         #값이 큰 순서대로 힙의 끝에 저장됨
#         unsorted[0], unsorted[node] = unsorted[node], unsorted[0]
#         parent = 0
#         child = 1

#         # 정렬이 미완료 된 노드들 사이에서
#         # 마지막 노드 자리리 보내준 루트 노드를 제외한 가장 큰 값을 찾고
#         # 루트 노드 자리로 온 마지막 노드의 자리 찾기
#         while child < node:
#             child = parent*2 + 1
#             #마지막 노드 자리로 보낸 루트 노드를 제외한 가장 큰 노드를 찾기 위해
#             if child < node-1 and unsorted[child] < unsorted[child+1]:
#                 child += 1
#             #마지막 노드 자리로 보낸 루트 노드를 제외한 가장 큰 노드를 루트 자리로 보내기 위한 과정
#             if child < node and unsorted[parent] < unsorted[child]:
#                 unsorted[parent], unsorted[child] = unsorted[child], unsorted[parent]

#             parent = child

#     return unsorted


# 힙 상태를 검사하는 heapify 함수를 만들어서 사용하는 방법

def heapify(li, idx, n):
    # li : 힙으로 만들고자 하는 배열
    # idx : 선택된 노드
    # n : 힙의 범위
    
    # 자식의 왼쪽 노드를 의미
    left = idx * 2
    # 자식의 오른쪽 노드를 의미
    right = idx * 2 + 1
    s_idx = idx

    # 선택 노드, 선택 노드의 양 자식 중 가장 작은 값을 찾는 과정
    if left <= n and li[s_idx] > li[left]:
        s_idx = left
    if right <= n and li[s_idx] > li[right]:
        s_idx = right
        
    # 선택 노드와 자식 노드의 위치가 바뀌어야 한다면
    if s_idx != idx:
        # 부모 자식 위치 변경
        li[idx], li[s_idx] = li[s_idx], li[idx]
        # 부모가 자식으로 내려간 이후에도, 그 자식과 바뀔 여지가 있는지 재귀로 체크
        return heapify(li, s_idx, n)

def heap_sort(array):
    n = len(array)
    
    # 루트노드는 index 1부터 시작하므로, 앞에 0 원소를 추가한 채로 시작.
    array = [0] + array
    
    # 최종 정렬된 원소들이 저장될 배열
    ans = []

    # Min Heap을 만드는 과정
    for i in range(n//2, 0, -1):
        heapify(array, i, n)

    # 루트 노드 원소를 정렬 배열에 저장, heapify 반복
    for i in range(n, 0, -1):
        ans.append(array[1])
        array[i], array[1] = array[1], array[i]
        heapify(array, 1, i-1)
    
    # array[1:]를 얻으면 오름차순 정렬 배열을 얻을 수 있음
    return ans
print(heap_sort(num))