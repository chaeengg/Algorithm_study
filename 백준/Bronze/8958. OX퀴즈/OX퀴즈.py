N = int(input())

for _ in range(N):
    sen = input()
    cnt = 0 
    score_sum = 0
    
    for i in sen:
        if i == 'O':
            cnt += 1
            score_sum += cnt
        else:
            cnt = 0
    print(score_sum)