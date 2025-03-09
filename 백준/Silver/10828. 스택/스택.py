import sys 
N = int(input())

stack = []
for _ in range(N):
    order = sys.stdin.readline().strip().split()

    if order[0] == 'push':
        stack.append(order[1])

    elif order[0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(stack))

    elif order[0] == 'empty':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    
    elif order[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)