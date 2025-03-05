from collections import deque

N = int(input())
card = deque()

for _ in range(1, N+1):
    card.append(_)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])