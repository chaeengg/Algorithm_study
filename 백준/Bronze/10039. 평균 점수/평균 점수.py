sum_num = 0

for i in range(5):
    num = int(input())

    if num >= 40:
        sum_num += num
    else:
        sum_num += 40
        
print(int(sum_num/5))