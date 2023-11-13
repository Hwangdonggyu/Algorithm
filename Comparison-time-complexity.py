import time, random

def evaluate_n2(A, x):
	# code for O(n^2)-time function
	result = 0
	for i in range(len(A)):
		coef = A[i]
		for j in range(i):
			coef *= x
		result += coef
	return result	
	
def evaluate_n(A, x):
	# code for O(n)-time function
	result = 0
	x_coef = 1
	for i in range(len(A)):
		coef = A[i]
		if(i==0):
			pass
		else:
			x_coef *= x
		result += coef*x_coef
	return result
		
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [random.randint(-1000,1000) for i in range(n)]
x = random.randint(-1000,1000)

# 두 함수의 수행시간 출력
time_c = []
s = time.process_time()
evaluate_n2(A,x) # evaluate_n2 호출
e = time.process_time()

time_c.append(e-s)

s = time.process_time()
evaluate_n(A,x) # evaluate_n 호출
e = time.process_time()

time_c.append(e-s)

print(f"O(n) 수행시간 = {time_c[1]}")
print(f"O(n^2) 수행시간 = {time_c[0]}")
