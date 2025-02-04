import math

A, B = map(int, input().split())
    
print(math.gcd(A, B))
print(int(A * B / math.gcd(A, B)))