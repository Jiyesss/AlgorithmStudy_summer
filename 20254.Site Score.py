'''
백준
20254번. Site Score
'''
import sys
input = sys.stdin.readline

ur, tr, uo, to = map(int, input().split())

print(56*ur + 24*tr + 14*uo + 6*to)