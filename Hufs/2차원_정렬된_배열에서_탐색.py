# 2차원 정렬된 배열에서 탐색 O(n)의 시간복잡도를 가짐 분할정복법을 사용함
def search(A, k, row_start, row_end, col_start, col_end):
		if row_start > row_end or col_start > col_end:
			return (-1, -1)

		mid_row = (row_start + row_end) // 2 # 중앙 행
		mid_col = (col_start + col_end) // 2 # 중앙 열

		if A[mid_row][mid_col] == k:
			return (mid_row, mid_col)
		elif A[mid_row][mid_col] < k:
			right = search(A, k, row_start, mid_row, mid_col + 1, col_end)
			down = search(A, k, mid_row + 1, row_end, col_start, col_end)
			if(right != (-1, -1)):
				return right
			else:
				return down
		else:
			# k는 현재 중간 값보다 왼쪽 또는 위쪽 부분 배열에 있을 수 있음
			# 오른쪽 하단 부분 배열은 제외하고 재귀
			left = search(A, k, row_start, mid_row - 1, col_start, col_end)
			up = search(A, k, mid_row, row_end, col_start, mid_col - 1)
			if(left != (-1, -1)):
				return left
			else:
				return up

# 입력값 및 결과 출력
n, k = map(int, input().split())
A = [list(map(int, input().split())) for x in range(n)]
print(search(A, k, 0, n - 1, 0, n - 1))
