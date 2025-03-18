S = list(input().strip())

hole_sum = 0
for i in S:
    if i in ['A', 'D', 'O', 'P', 'Q', 'R', 'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q', '@']:
        hole_sum += 1
    elif i == 'B':
        hole_sum += 2
print(hole_sum)