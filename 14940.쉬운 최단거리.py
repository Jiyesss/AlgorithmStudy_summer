'''
백준 실버1
14940번
쉬운 최단거리
'''

from collections import deque

def bfs(grid, start, H, W):
    distances = [[-1] * W for _ in range(H)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    distances[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == 1 and distances[nx][ny] == -1:
                distances[nx][ny] = distances[x][y] + 1
                queue.append((nx, ny))
    
    return distances

# 입력 받기
H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]

# 목표지점 찾기
start = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 2:
            start = (i, j)
            break
    if start:
        break

# BFS 실행하여 최단 거리 계산
distances = bfs(grid, start, H, W)

# 결과 출력
for i in range(H):
    for j in range(W):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(distances[i][j], end=' ')
    print()
