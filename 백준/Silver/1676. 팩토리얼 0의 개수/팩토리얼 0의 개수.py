mul = 1
cnt = 0

for i in range(1, int(input())+1):
    mul = mul * i

for j in range(len(str(mul))-1, -1, -1):
    if str(mul)[j] == '0':
        cnt += 1
    else:
        break
print(cnt)