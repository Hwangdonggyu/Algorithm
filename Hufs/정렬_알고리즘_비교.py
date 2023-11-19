import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
def quick_sort(A, first, last):
	global Qc, Qs # 비교와 이동
	if first >= last: 
		return
	left, right = first+1, last
	pivot = A[first]
	while left <= right:
			while left <= last and A[left] < pivot:
				left += 1
				Qc += 1
			while right > first and A[right] > pivot:
				right -= 1
				Qc += 1
			if left <= right:
				Qs += 1
				A[left], A[right] = A[right], A[left]
				left += 1
				right -= 1
	A[first], A[right] = A[right], A[first]
	Qs += 1
	quick_sort(A, first, right-1)
	quick_sort(A, right+1, last)
	
def quick_sort2(A, first, last): # 추가 점수 1번
	global Qc2, Qs2
	if first >= last: 
		return
	left, right = first+1, last
	pivot = A[first]
	K = last-first+1
	if(K>=10 and K<=40):
		insertion_sort(A,first,last)
	else:
		while left <= right:
			while left <= last and A[left] < pivot:
				left += 1
				Qc2 += 1
			while right > first and A[right] > pivot:
				right -= 1
				Qc2 += 1
			if left <= right:
				Qs2 += 1
				A[left], A[right] = A[right], A[left]
				left += 1
				right -= 1
		A[first], A[right] = A[right], A[first]
		Qs2 += 1
		quick_sort2(A, first, right-1)
		quick_sort2(A, right+1, last)

def insertion_sort(A, first, last):
	global Qc2, Qs2
	for i in range(first, last + 1):
			j = i-1
			while j >= first and A[j] > A[j + 1]:
				Qc2 += 1
				A[j], A[j + 1] = A[j + 1], A[j]
				Qs2 += 1
				j -= 1

def quick_sort3(A, first, last): # 추가 점수 2번
	global Qc3, Qs3 # 비교와 이동
	if first >= last: 
		return
	left, right = first+1, last
	pivot = A[first]
	K = last-first+1
	if(K>=10 and K<=40):
		return
	else:
		while left <= right:
				while left <= last and A[left] < pivot:
					left += 1
					Qc3 += 1
				while right > first and A[right] > pivot:
					right -= 1
					Qc3 += 1
				if left <= right:
					Qs3 += 1
					A[left], A[right] = A[right], A[left]
					left += 1
					right -= 1
		A[first], A[right] = A[right], A[first]
		Qs3 += 1
		quick_sort3(A, first, right-1)
		quick_sort3(A, right+1, last)


def insertion_sort2(A):
	global Qc3, Qs3
	for i in range(1,n):
			j = i-1
			while j >= 0 and A[j] > A[j + 1]:
				Qc3 += 1
				A[j], A[j + 1] = A[j + 1], A[j]
				Qs3 += 1
				j -= 1
		
		
def merge_sort(A, first, last):
	global Mc, Ms
	if first >= last:
		return
	m = (first + last) // 2
	merge_sort(A, first, m)
	merge_sort(A, m+1, last)
	merge_two_sorted_lists(A, first, last)

def merge_sort2(A, first, last): # 추가 점수 3번
	global Mc2, Ms2
	if first >= last:
		return
	mid = first + ((last- first) // 3)
	mid2 = first + 2 * ((last- first) // 3)
	merge_sort2(A, first, mid)
	merge_sort2(A, mid+1, mid2)
	merge_sort2(A, mid2+1, last)
	merge_three_sorted_lists(A, first, last)

def merge_three_sorted_lists(A, first, last):
	global Mc2, Ms2
	mid = first + ((last- first) // 3)
	mid2 = first + 2 * ((last - first) // 3)
	i, j, k = first, mid+1, mid2+1
	B = []
	while i <= mid and j <= mid2 and k <= last:
		if A[i] <= A[j] and A[i] <= A[k]: # 2번 비교
			Mc2 += 2
			B.append(A[i])
			Ms2 += 1
			i += 1
		elif A[j] <= A[i] and A[j] <= A[k]:
			Mc2 += 2
			B.append(A[j])
			Ms2 += 1
			j += 1
		else:
			Mc2 += 2
			B.append(A[k])
			Ms2 += 1
			k += 1
	while i <= mid and j <= mid2:
		if A[i] <= A[j]:
			Mc2 += 1
			B.append(A[i])
			Ms2 += 1
			i += 1
		else:
			Mc2 += 1
			B.append(A[j])
			Ms2 += 1
			j += 1
	while j <= mid2 and k <= last:
		if A[j] <= A[k]:
			Mc2 += 1
			B.append(A[j])
			Ms2 += 1
			j += 1
		else:
			Mc2 += 1
			B.append(A[k])
			Ms2 += 1
			k += 1
	while i <= mid and k <= last:
		if A[i] <= A[k]:
			Mc2 += 1
			B.append(A[i])
			Ms2 += 1
			i += 1
		else:
			Mc2 += 1
			B.append(A[k])
			Ms2 += 1
			k += 1
	for i in range(i, mid+1):
		B.append(A[i])
		Ms2 += 1
	for j in range(j, mid2+1):
		B.append(A[j])
		Ms2 += 1
	for k in range(k, last+1):
		B.append(A[k])
		Ms2 += 1
	for i in range(first, last+1):
		A[i] = B[i-first]
		Ms2 += 1

	

def merge_two_sorted_lists(A, first, last):
	global Mc, Ms
	m = (first + last) // 2
	i, j = first, m+1
	B = []
	while i <= m and j <= last:
		if A[i] <= A[j]:
			Mc += 1
			B.append(A[i])
			Ms += 1
			i += 1
		else:
			Mc += 1
			B.append(A[j])
			Ms += 1
			j += 1
	for i in range(i, m+1):
		B.append(A[i])
		Ms += 1
	for j in range(j, last+1):
		B.append(A[j])
		Ms += 1
	for k in range(first, last+1):
		A[k] = B[k-first]
		Ms += 1

def heap_sort(A):
	global Hc, Hs
	make_heap(A)
	n = len(A)
	for k in range(n-1, -1, -1):
		A[0], A[k] = A[k], A[0]
		Hs += 1
		n = n-1
		heapify_down(A, 0, n)

def make_heap(A):
    global Hc, Hs
    n = len(A)
    for k in range(n-1, -1, -1):
        heapify_down(A, k, n)

def heapify_down(A,k,n):
	global Hc, Hs
	while 2*k+1 < n:
		L, R = 2*k+1, 2*k+2
		if L < n and A[L] > A[k]:
			Hc += 1
			m = L
		else:
			Hc += 1
			m = k
		if R < n and A[R] > A[m]:
			Hc += 1
			m = R
		if m != k:
			A[k], A[m] = A[m], A[k]
			Hs += 1
			k = m
		else:
			break


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
Qc2, Qs2, Qc3, Qs3, Mc2, Ms2 = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:]
E = A[:]
F = A[:]
G = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))


print("Quick sort2:")
print("time =", timeit.timeit("quick_sort2(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc2, Qs2))

print("Quick sort3:")
print("time =", timeit.timeit("quick_sort3(E, 0, n-1),insertion_sort2(E)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc3, Qs3))

print("Merge sort2:")
print("time =", timeit.timeit("merge_sort2(F, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc2, Ms2))

# 추가 점수 4번
print("Tim sort:")
print("time =", timeit.timeit("G.sort()", globals=globals(), number=1))

print("")

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))
assert(check_sorted(F))
assert(check_sorted(G))
