n = int(input())
list = []
d = 0
p = 0
for i in range(n):
    list.append(input())

for l in list:
    if l == 'D':
        d += 1
        if d >= p +2:
            break

    else:
        p += 1
        if p >= d + 2:
            break

print(d,":",p,sep="")
