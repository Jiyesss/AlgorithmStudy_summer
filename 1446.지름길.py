'''
백준 실버1
1446번
지름길
'''
import sys
import heapq

N, D = map(int, sys.stdin.readline().split())

# 지름길 정보를 담을 리스트
shortcuts = []

for _ in range(N):
    depart, arrive, length = map(int, sys.stdin.readline().split())
    if arrive - depart > length and arrive <= D:
        shortcuts.append((depart, arrive, length))

# 출발위치 오름차순 + 도착위치 내림차순으로 정렬
shortcuts.sort(key=lambda s: (s[0], -s[1]))

# 거리 배열, 초기값은 최대로 설정
distance = [i for i in range(D + 1)]

# 다익스트라 알고리즘을 활용한 최단거리 계산
for i in range(D + 1):
    if i != 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)  # 현재 위치까지의 거리 업데이트

    for depart, arrive, length in shortcuts:
        if depart == i and arrive <= D:
            distance[arrive] = min(distance[arrive], distance[depart] + length)

print(distance[D])
