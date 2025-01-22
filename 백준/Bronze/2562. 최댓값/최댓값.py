num = []
max = 0     

for i in range(9):
    num.append(int(input()))

    if num[i] > max:
        max = num[i]

print(max)
print(num.index(max)+1)