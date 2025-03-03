import sys
from collections import Counter

N = int(sys.stdin.readline())
num = []
sum_num = 0
for _ in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

print(round(sum(num)/N))
print(num[N//2])

bin = Counter(num).most_common(2)   # 최빈값
if len(num) > 1:
    if bin[0][1] == bin[1][1]:
        print(bin[1][0])            # 최빈값 중 두번째로 작은 값 
    else:
        print(bin[0][0])
else:
    print(bin[0][0])

print(num[-1]-num[0])