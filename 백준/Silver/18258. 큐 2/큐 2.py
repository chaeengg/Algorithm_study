import sys 
from collections import deque
N = int(input())

stack = deque([])
for _ in range(N):
    order = sys.stdin.readline().strip().split()

    if order[0] == 'push':
        stack.append(order[1])

    elif order[0] == 'pop':
        if len(stack) != 0:
            print(stack[0])
            stack.popleft()
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    
    elif order[0] == 'front':
        if len(stack) != 0:
            print(stack[0])
        else:
            print(-1)

    elif order[0] == 'back':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)