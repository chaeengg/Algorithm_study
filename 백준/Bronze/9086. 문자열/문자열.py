n = int(input())

for i in range(n):
    sentence = input()
    
    if len(sentence) > 1:
        print(sentence[0],sentence[-1], sep='')

    else:
        print(sentence*2)