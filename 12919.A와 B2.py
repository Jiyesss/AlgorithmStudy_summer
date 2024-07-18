'''
백준 골드5
12919번
A와 B 2
'''

import sys

S = list(input().strip())
T = list(input().strip())

def dfs(t):
    if t == S:
        print(1)
        sys.exit()
    if len(t) < len(S):
        return
    if t[-1] == 'A':  # 마지막 문자가 A인 경우
        dfs(t[:-1])  # 마지막 문자 A를 제거하고 재귀 호출
    if t[0] == 'B':  # 첫 번째 문자가 B인 경우
        dfs(t[1:][::-1])  # 첫 번째 문자 B를 제거하고 문자열을 뒤집어 재귀 호출

dfs(T)
print(0)

