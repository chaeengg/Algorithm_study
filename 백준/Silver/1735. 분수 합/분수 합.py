import math

A, B = map(int, input().split())
C, D = map(int, input().split())

bunmo = math.lcm(B, D)
mul_a = int(bunmo / B)
mul_c = int(bunmo / D)
bunja = (A * mul_a) + (C * mul_c)

if math.gcd(bunja, bunmo) == 1:
    print(bunja, bunmo)
else:
    yaksu = math.gcd(bunja, bunmo)
    print(int(bunja/yaksu), int(bunmo/yaksu))