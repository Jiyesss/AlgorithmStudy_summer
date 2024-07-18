'''
백준 실버2
1138번 한 줄로 서기
'''

def arrange_line(heights):
    n = len(heights)
    result = [0] * n
    
    for i in range(n):
        count = heights[i]
        for j in range(n):
            if count == 0 and result[j] == 0:
                result[j] = i + 1
                break
            elif result[j] == 0:
                count -= 1
    
    return result

# 입력 받기
n = int(input().strip())
heights = list(map(int, input().strip().split()))

# 결과 계산
result = arrange_line(heights)

# 결과 출력
print(" ".join(map(str, result)))
