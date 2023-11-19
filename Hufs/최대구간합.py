# Prefix_sum 구하기 O(nlogn)의 시간복잡도를 가짐
def max_sum(A, left, right):
	if(left == right): return A[left]
	m = (left+right)//2 
	L = max_sum(A,left,m)
	R = max_sum(A,m+1,right)

	left_sum = 0
	left_max_sum = A[left]
	for i in range(m,left-1,-1):
		left_sum += A[i]
		left_max_sum = max(left_max_sum, left_sum)
			
	# A의 오른쪽 반 최대 구간 합 구하기
	right_sum = 0
	right_max_sum = A[right]
	for i in range(m+1,right+1):
		right_sum += A[i]
		right_max_sum = max(right_max_sum, right_sum)
	
	# A의  양쪽에 모두 걸치는 경우
	M = left_max_sum  + right_max_sum
	# A 배열의 최대 구간 합을 반환
	return max(L,R,M)

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)
