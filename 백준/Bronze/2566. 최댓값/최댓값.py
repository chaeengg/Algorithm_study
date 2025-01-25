max_num = 0
row_num = 0
col_num = 0
num_list = []

for i in range(9):
    num_list.append(list(map(int, input().split())))

# 행 
for row in range(9):
    if max_num < max(num_list[row]):
        max_num = max(num_list[row])
        row_num = row                 

# 열
col_num = num_list[row_num].index(max_num)

print(max_num)
print(row_num+1, col_num+1)       # index이므로 각 +1