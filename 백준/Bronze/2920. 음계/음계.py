num_list = list(map(int, input().split()))

if num_list == list(range(1, 9)):
    print('ascending')
elif num_list == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')