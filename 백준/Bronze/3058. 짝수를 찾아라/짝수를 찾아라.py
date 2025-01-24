T = int(input())
step = 0

while True:
    step += 1
    sum = 0 
    min_list = []       
    num_list = []
    num_list[0:7] = map(int, input().split())

    for i in range(7):
        if num_list[i] % 2 == 0:
            sum += num_list[i]
            min_list.append(num_list[i])
    print(sum, min(min_list))

    if step == T:
        break