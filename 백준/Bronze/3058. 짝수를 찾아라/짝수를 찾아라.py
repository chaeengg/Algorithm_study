T = int(input())

for i in range(T):
    sum = 0
    min_list = []
    num_list= list(map(int, input().split()))

    for j in range(7):
        if num_list[j] % 2 == 0:
            sum += num_list[j]
            min_list.append(num_list[j])

    print(sum, min(min_list))