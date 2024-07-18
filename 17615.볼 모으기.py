'''
백준 실버1
17615번. 볼 모으기
'''

def min_moves_to_collect_balls(balls):
    n = len(balls)
    
    # 왼쪽 끝과 오른쪽 끝에서 연속된 'R'과 'B'의 개수
    left_R, left_B = 0, 0
    right_R, right_B = 0, 0
    
    # 왼쪽 끝에서 연속된 'R' 세기
    for i in range(n):
        if balls[i] == 'R':
            left_R += 1
        else:
            break
    
    # 왼쪽 끝에서 연속된 'B' 세기
    for i in range(n):
        if balls[i] == 'B':
            left_B += 1
        else:
            break
    
    # 오른쪽 끝에서 연속된 'R' 세기
    for i in range(n-1, -1, -1):
        if balls[i] == 'R':
            right_R += 1
        else:
            break
    
    # 오른쪽 끝에서 연속된 'B' 세기
    for i in range(n-1, -1, -1):
        if balls[i] == 'B':
            right_B += 1
        else:
            break
    
    # 전체 'R'과 'B'의 개수
    total_R = balls.count('R')
    total_B = balls.count('B')
    
    # 각 경우의 이동 횟수 계산
    moves_left_R = total_R - left_R
    moves_left_B = total_B - left_B
    moves_right_R = total_R - right_R
    moves_right_B = total_B - right_B
    
    # 최소 이동 횟수 반환
    return min(moves_left_R, moves_left_B, moves_right_R, moves_right_B)

# 입력 받기
n = int(input().strip())
balls = input().strip()

# 결과 출력
print(min_moves_to_collect_balls(balls))
