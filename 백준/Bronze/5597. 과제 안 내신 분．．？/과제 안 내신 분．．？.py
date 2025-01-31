student = [i for i in range(1, 31)]
ok = []

for i in range(1, 29):
    ok.append(int(input()))

no = [s for s in student if s not in ok]
print(*no)