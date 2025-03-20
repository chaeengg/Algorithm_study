T = int(input())
answer = list(map(int, input().split()))

cnt = 0
for i in answer:
    if T == i:
        cnt += 1
print(cnt)