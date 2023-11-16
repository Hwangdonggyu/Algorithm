# 이진 탐색을 이용한 rotating list문제 O(logn)의 시간 복잡도를 가진다.
A = [int(x) for x in input().split()]

start, end = 0, len(A)-1
while(start < end): 
	m = (start + end)//2 
	if A[m] > A[end]: 
		start = m + 1
	else: 
		end = m

if(len(A)-start == len(A)): 
	print(0)
else: 
	print(len(A)-start)
