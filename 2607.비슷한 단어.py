'''
백준 2607번
실버2 비슷한 단어
'''
import sys
input = sys.stdin.readline

# 각 단어에 있는 알파벳 개수를 세주는 함수
def countAlphabet(word):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_list = [0] * 26

    for ch in word:
        idx = alphabet.find(ch)
        alpha_list[idx] += 1
    
    return alpha_list

# 비슷한 단어를 확인하는 함수
def is_similar(word1, word2):
    if abs(len(word1) - len(word2)) > 1:
        return False

    count1 = countAlphabet(word1)
    count2 = countAlphabet(word2)

    diff_count = 0
    for i in range(26):
        diff_count += abs(count1[i] - count2[i])

    if len(word1) == len(word2):
        return diff_count <= 2
    else:
        return diff_count <= 1

# 단어의 수를 입력받음
n = int(input().strip())
words = [input().strip() for _ in range(n)]

first = words.pop(0)  # 첫 번째 단어 제거

cnt = 0  # 비슷한 단어를 셈

# 첫 번째 단어를 제외한 나머지 단어 순회
for word in words:
    if is_similar(first, word):
        cnt += 1

print(cnt)
