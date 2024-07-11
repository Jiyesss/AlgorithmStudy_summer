'''
백준 실버3
21921번 블로그
'''
import sys
input = sys.stdin.readline

n, x = map(int, input().strip().split())
visitors = list(map(int, input().strip().split()))


max_visitors = 0
current_window_sum = sum(visitors[:x])
max_visitors = current_window_sum
max_periods = 1


for i in range(x, n):
    current_window_sum += visitors[i] - visitors[i - x]
    if current_window_sum > max_visitors:
        max_visitors = current_window_sum
        max_periods = 1
    elif current_window_sum == max_visitors:
        max_periods += 1


if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(max_periods)
