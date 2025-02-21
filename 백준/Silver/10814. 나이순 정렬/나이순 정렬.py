N = int(input())

people = []
for _ in range(N):
    age, name = map(str, input().split())
    people.append([int(age), name])
    
people.sort(key = lambda x: x[0])
for i in range(N):
    print(*people[i])