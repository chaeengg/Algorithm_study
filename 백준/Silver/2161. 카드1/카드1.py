N = int(input())
card = []
waste = []
for _ in range(1, N+1):
    card.append(_)

while True:
    waste.append(card[0])
    card.pop(0)

    if len(card) != 0:
        card.append(card[0])
        card.pop(0)
    else:
        print(*waste)
        break