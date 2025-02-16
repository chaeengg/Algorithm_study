money = {'Franklin': 100, 'Grant': 50, 'Jackson': 20, 'Hamilton': 10, 'Lincoln': 5, 'Washington': 1}

n = int(input())

for i in range(n):
    sum_money = 0
    sentence = list(input().split())
    
    for j in sentence:
        if j in money.keys():
            sum_money += money[j]
    print(f'${sum_money}')