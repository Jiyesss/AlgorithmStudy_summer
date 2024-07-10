'''
백준 골드5
13549번
숨바꼭질3
'''

from collections import deque

n, k = map(int, input().split())


queue = deque([(n, 0)]) # (현재위치, 경과시간)

visited = [False] * 100001 # 방문하지 않은 노드 : false, 방문한 노드: true
visited[n] = True

while queue:
    current, time = queue.popleft()

    # 수빈이가 동생을 찾은 경우
    if current == k:
        print(time)
        break

    # 다음에 방문할 수 있는 노드의 경우의 수
    next_positions = [current * 2, current - 1, current + 1]

    for next_pos in next_positions:
        if 0 <= next_pos < 100001 and not visited[next_pos]:
            visited[next_pos] = True
            
            # 순간이동을 하는 경우
            if next_pos == current * 2:
                queue.appendleft((next_pos, time))
            # -1 또는 +1 로 이동하는 경우
            else:
                queue.append((next_pos, time + 1))

    
    
