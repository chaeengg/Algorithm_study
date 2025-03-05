N = int(input())

queue = []
for _ in range(N):
    order = input()

    if 'push' in order:
        num = order.split()[1]
        queue.append(int(num))

    elif 'pop' == order:
        if len(queue) != 0:
            print(queue[0])
            queue.pop(0)
        else:
            print(-1)
    
    elif 'size' == order:
        print(len(queue))

    elif 'empty' == order:
        if len(queue) == 0:
            print(1)
        else: 
            print(0)

    elif 'front' == order:
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    
    elif 'back' == order:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)