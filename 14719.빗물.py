'''
백준 골드5
14179번 빗물
'''

def calculate_trapped_water(heights):
    if not heights:
        return 0
    
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    trapped_water = 0

    # 왼쪽에서 최대 높이 구하기
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])
    
    # 오른쪽에서 최대 높이 구하기
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    
    # 현재 위치에서 쌓일 수 있는 빗물 계산
    for i in range(n):
        trapped_water += min(left_max[i], right_max[i]) - heights[i]
    
    return trapped_water

# 입력 받기
H, W = map(int, input().split())
heights = list(map(int, input().split()))

# 결과 출력
print(calculate_trapped_water(heights))
