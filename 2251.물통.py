'''
백준 2251번
골드5 물통
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(A, B, C):
    visited = set()
    possible_C = set() # 물통A가 비어있을 때 물통 C의 물의 양을 저장하는 집합
    queue = deque([(0, 0, C)])

    while queue:
        a, b, c = queue.popleft()
        
        # 이미 방문했다면 skip
        if (a, b, c) in visited:
            continue
        
        visited.add((a, b, c))
        
        # 물통 A가 비어있는 경우
        if a == 0:
            possible_C.add(c)
        
        # A->B
        queue.append((max(0, a + b - B), min(B, a + b), c))
        # A->C
        queue.append((max(0, a + c - C), b, min(C, a + c)))
        # B->A
        queue.append((min(A, b + a), max(0, b + a - A), c))
        # B->C
        queue.append((a, max(0, b + c - C), min(C, b + c)))
        # C->A
        queue.append((min(A, c + a), b, max(0, c + a - A)))
        # C->B
        queue.append((a, min(B, c + b), max(0, c + b - B)))
    
    return sorted(possible_C)



A, B, C = map(int, input().split())
result = bfs(A, B, C)
print(' '.join(map(str, result)))

