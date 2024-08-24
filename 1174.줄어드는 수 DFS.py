'''
백준 줄어드는 수
'''
import sys
input = sys.stdin.readline

def dfs():

    # array 존재하는 경우
    if array:
        # 줄어드는 수에 해당
        decrease.append(int(''.join(map(str,array))))

    # 0~9
    for i in range(10):
        
        # 첫번째 자리이거나, 줄어드는 경우
        if len(array) == 0 or array[-1] > i:
            
            array.append(i)
            dfs()
            array.pop()



# N 입력받기
n = int(input())

# 줄어드는 수 찾기
array = [] # 현재 탐색중인 숫자 담을거
decrease = [] # 줄어드는 수 담을거
dfs()

print(decrease)
try:
    print(sorted(decrease)[n-1])

except:
    print("-1")