N = int(input())
num = []

num[0:N] = map(int, input().split())

print(min(num), max(num))