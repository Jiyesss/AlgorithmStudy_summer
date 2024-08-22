'''
백준 줄어드는 수
'''
import sys
input = sys.stdin.readline

# 줄어드는 수인지 확인
def decrease(integer):
    integer = str(integer) # String으로 변환

    # 1의 자리인 경우 -> 줄어드는 수
    if len(integer) == 1: 
        return True
    
    # 1의 자리가 아닌 경우
    else:
        for i in range(len(integer)-1):
        
            if integer[i] <= integer[i+1]: # 줄어드는 수가 아닌 경우
                return False
            
    return True


# N 입력받기
n = int(input())

# 몇번째 줄어드는 수인지 count
count = 0

# N은 1000000보다 작거나 같은 자연수
for i in range(1000001):

    # 줄어드는 수에 해당하는 경우
    if decrease(i):
        count += 1

    # 종료조건
    if count == n:
        print(i)
        break

if i < 1000000:
    print(i)
else:
    print("-1")