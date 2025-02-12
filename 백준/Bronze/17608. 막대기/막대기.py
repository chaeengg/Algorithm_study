import sys 

N = int(sys.stdin.readline())
stick = []

for i in range(N):
    stick.append(int(sys.stdin.readline()))

stick.reverse()
top = stick[0]
count = 1

for i in range(1, N):
    if top < stick[i]:
        count += 1
        top = stick[i]

print(count)