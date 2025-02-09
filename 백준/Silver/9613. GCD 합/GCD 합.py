import math

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    n = num[0]
    sum = 0

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            sum += math.gcd(num[i], num[j])
    print(sum)