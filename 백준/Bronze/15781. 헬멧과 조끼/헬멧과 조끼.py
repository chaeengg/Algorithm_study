N, M = map(int, input().split())

helmet = list(map(int, input().split()))
jokki = list(map(int, input().split()))

print(max(helmet) + max(jokki))