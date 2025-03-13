mul = 1
for _ in range(3):
    mul = mul * int(input())
for i in range(0, 10):
    print(str(mul).count(str(i)))