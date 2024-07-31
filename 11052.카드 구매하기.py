'''
백준 실버1
11052번.카드 구매하기
'''

import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))


dp = [0] * (n+1) # dp안에 각 개수별 최대값을 집어넣을 것임


# 각 개수별로 최대값을 저장
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i],dp[i-j]+ p[j])



print(dp[n])
 




