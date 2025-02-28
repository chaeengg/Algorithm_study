import sys
A, B = map(str, sys.stdin.readline().split())
sum_num = 0
for i in A:
    for j in B:
        sum_num += int(i)*int(j)
print(sum_num)