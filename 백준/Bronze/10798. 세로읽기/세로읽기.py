sentence_list = []    # 가로 한 줄씩 
result = []           # 세로 한 줄씩 
max_len = 0

for i in range(5):
    sentence = list(input())

    if max_len < len(sentence):
        max_len = len(sentence)

    sentence_list.append(sentence)
    
for j in range(5):      # 세로로 확인할 때 공백 고려 
    while len(sentence_list[j]) < max_len:
        sentence_list[j].append(' ')

for k in range(max_len):
    new = ''.join(sentence_list[j][k] for j in range(5))
    result.append(new)
    
print(''.join(result).replace(' ', ''))