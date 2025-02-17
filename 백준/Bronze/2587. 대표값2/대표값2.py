sum_num = 0
num_list = []
for _ in range(5):
    num = int(input())
    num_list.append(num)
    sum_num += num
print(int(sum_num/5))
print(sorted(num_list)[2])