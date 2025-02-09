k = int(input())
num_list = []

for i in range(k):
    num = int(input())
    
    if num != 0:
        num_list.append(num)

    else:
        if not num_list:
            continue
        else:
            del num_list[-1]

print(sum(num_list))