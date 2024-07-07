'''
백준 실버2 3758번
KCPC
'''

T = int(input()) # 테스트 데이터의 수를 나타내는 정수

for _ in range(T):
    n, k, t, m = map(int, input().split()) # n: 팀의 개수, k: 문제의 개수, t: 당신 팀의 ID, m: 로그 엔트리의 개수
    rankingBoard = []  # 각 팀 별 결과를 저장할 중첩리스트

    # rankingBoard 초기화
    for _ in range(n):
        rankingBoard.append([0, 0, [0 for _ in range(k)]]) # 각 팀별 시도 횟수, 제출 시간, 문제 별 점수
    

    for time in range(m): 
        i, j, s = map(int, input().split()) # i: 팀 ID, j: 문제 번호, s: 획득한 점수
        rankingBoard[i-1][0] += 1 # 해당 팀의 제출 횟수 추가
        rankingBoard[i-1][1] = time # 제출 시간 저장      
        rankingBoard[i-1][2][j-1] = max(s, rankingBoard[i-1][2][j-1]) # 문제 j의 점수 저장(최고 점수 기준)

    # 최종 점수 합산
    sumScore = [0] * n
    for id in range(n):
        sumScore[id] = sum(rankingBoard[id][2])
    
    # 등수 계산
    my = 1
    for team in range(n):
        if team+1 == t:
            continue
        else:
            if sumScore[team] > sumScore[t-1]:# 더 높은 점수를 가지는 팀이 존재하는 경우
                my += 1
            elif sumScore[team] == sumScore[t-1]: # 최종 점수가 같을 경우
                if rankingBoard[team][0] < rankingBoard[t-1][0]: # 우리 팀의 제출 횟수가 더 많으면, 순위가 내려감
                    my += 1
                elif rankingBoard[team][0] == rankingBoard[t-1][0]: # 제출횟수가 같은 경우,
                    if rankingBoard[team][1] < rankingBoard[t-1][1]: # 마지막 제출 시간이 더 빠른 팀이 이김
                        my += 1
    
    print(my)





        
        
