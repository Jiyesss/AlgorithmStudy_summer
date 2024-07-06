'''
백준 20922번
겹치는 건 싫어
'''

n , k = map(int,input().split() )# n = 수열의 길이, # k = 최장 연속 부분 수열에서 포함될 수 있는 같은 정수의 최대 개수

seq = list(map(int, input().split())) # 수열 

# sequence에 대해 원소 별 개수를 세서 K+1 개 이상인 원소를 반환하는 함수
def countNum(seq, k):
    counts = {}

    # sequence의 원소별 개수를 셈
    for i in seq:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    # k+1 개 이상의 원소 반환 (num: 0으로 초기화)
    return  {num: 0 for num,count in counts.items() if count > k}

overk = countNum(seq, k)
longest = 0
start = 0 # sequence의 시작 0으로 초기화

for end in range(n): # sequence의 마지막 0으로 초기화

    if seq[end] in overk: # 수열에 포함된 원소의 개수가 K개보다 큰 원소인 경우
        overk[seq[end]] += 1 # 원소 count 추가 
    
        while overk[seq[end]] > k: # 부분 수열의 원소의 개수가 K개를 넘었을 때
            if seq[start] in overk: # start가 수열에 포함된 원소의 개수가 K보다 큰 원소일 경우
                overk[seq[start]] -= 1 # 원소 count 감소
            start += 1 # start를 앞으로 이동시킴
    
    longest = max(longest, end - start + 1)

print(longest)