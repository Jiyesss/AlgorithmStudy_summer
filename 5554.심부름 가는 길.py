sum = 0 # 이동시간 총합
for i in range(4):
    sum += int(input())

min = sum // 60
sec =  sum % 60 

print(min)
print(sec)