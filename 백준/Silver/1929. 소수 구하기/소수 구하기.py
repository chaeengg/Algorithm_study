M, N = map(int, input().split())

for i in range(M, N+1):
    if i < 2:
        continue

    prime = True

    for j in range(2, int(i**0.5)+1):
        if (i % j == 0):
            prime = False
            break
    if prime:
        print(i)