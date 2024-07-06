'''
백준 15989번_1,2,3 더하기 4
'''

# 일반항 구하는 함수 정의
def general(n, memo):
    if n <= 0:
        return 0
    if memo[n] != -1: # 중복 계산 제외시키기 (메모이제이션)
        return memo[n]
    for i in range(1, n + 1):
        if i == 1:
            memo[i] = 1
        elif i == 2:
            memo[i] = 2
        elif i == 3:
            memo[i] = 3
        else:
            memo[i] = memo[i - 3] + (i // 2) + 1
    return memo[n]


t = int(input()) # 테스트 케이스의 개수
testCase = [] # 테스트 케이스 저장할 리스트 선언
answer = [] # 정답 담을 리스트 선언

# testCase 추가
for _ in range(t):
    testCase.append(int(input()))

memo = [-1] * (max(testCase)+1) 

# 1,2,3의 합 계산
for tc in testCase:
    answer.append(general(tc,memo))
    

# 정답 출력
for a in answer:
    print(a)




