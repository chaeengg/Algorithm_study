N, X = map(int, input().split())
A = list(map(int, input().split()))

num = [x for x in A if x < X]
print(*num)