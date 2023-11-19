# 연속해서 k번째 작은 값 찾기/ O(nlogn)의 시간복잡도를 가지는 알고리즘
import heapq

A = list(map(int, input().split()))
list_max = []
list_controll = []
m = []

for i in range(len(A)):
    k = i//3 + 1 
    if( not list_max or A[i] < -list_max[0]):
        heapq.heappush(list_max,-A[i]) 
    else: 
        heapq.heappush(list_controll,A[i])
    if len(list_max) < k: 
        heapq.heappush(list_max, -heapq.heappop(list_controll))
    elif len(list_max) > k:
        heapq.heappush(list_controll, -heapq.heappop(list_max))
    m.append(-list_max[0])
print(sum(m))
