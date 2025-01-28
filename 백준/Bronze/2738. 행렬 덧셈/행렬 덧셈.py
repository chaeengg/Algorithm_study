N, M = map(int, input().split())

num_list = []
final_list = []

for i in range(N*2):
    num_list.append(list(map(int, input().split())))

for row in range(N):
    for col in range(M):
        print(num_list[row][col] + num_list[row+N][col], end=" ")
    print()