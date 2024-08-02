'''
백준 9372번
상근이의 여행
실버4'''
import sys
input = sys.stdin.readline

# 테스트 케이스 개수 입력받기
T = int(input().strip())

for _ in range(T):
    # 국가의 수 N과 비행기의 종류 M 입력받기
    N, M = map(int, input().strip().split())

    # 비행기 쌍 입력받기
    for _ in range(M):
        a, b = map(int, input().strip().split())
       

    # 모든 국가를 방문하는 최소 비행기 수는 항상 N-1
    print(N-1)