import math

N = int(input())
ring = list(map(int, input().split()))

for i in range(1, N):
    yaksu = math.gcd(ring[0], ring[i])
    print(f'{int(ring[0]/yaksu)}/{int(ring[i]/yaksu)}')