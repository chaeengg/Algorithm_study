sentence = input()
re_sentence = []

for i in range(len(sentence)):
    if sentence[i].isupper():
        re_sentence.append(sentence[i].lower())

    else:
        re_sentence.append(sentence[i].upper())

print(*re_sentence, sep='')