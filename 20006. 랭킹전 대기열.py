''' 
백준 실버2
20006번 랭킹전 대기열
'''

import sys
input = sys.stdin.readline


p, m = map(int, input().strip().split())  # p: 플레이어수, m: 방의 정원
players = [input().strip().split() for _ in range(p)]
players = [(int(level), nickname) for level, nickname in players]

rooms = []

for level, nickname in players:
    placed = False
    for room in rooms:
        if len(room) > 0 and len(room) < m and abs(room[0][0] - level) <= 10:
            room.append((level, nickname))
            placed = True
            break
    
    if not placed:
        rooms.append([(level, nickname)])

for room in rooms:
    room.sort(key=lambda x: x[1])
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for player in room:
        print(player[0], player[1])