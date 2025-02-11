N = int(input())

for i in range(N):
    sentence = list(input().split())
    print(f"Case #{i+1}:", *sentence[::-1])