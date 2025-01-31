N = int(input())

for i in range(N, 1003002):
    if i < 2:
        continue

    prime = True
    for j in range(2, int(i**0.5)+1):
        if (i % j == 0):
            prime = False
            break

    if prime:
        str_i = str(i)
        if str_i[0:] == str_i[::-1]:
            print(i)
            break