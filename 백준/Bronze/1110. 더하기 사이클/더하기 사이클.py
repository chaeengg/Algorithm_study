num_list = []           

N = input()
if int(N) < 10:
    N = '0' + N
num_list.append(N)
num_list.extend(N)
        
count = 0
while True:
    count += 1
    
    plus = int(num_list[4*count-3]) + int(num_list[4*count-2])
    if plus < 10:
        num_list.append('0')
        num_list.append(str(plus))
    else:
        num_list.extend(str(plus))

    num_list.append(num_list[4*count-2])
    num_list.append(num_list[4*count])

            
    if num_list[4*count-2] + num_list[4*count] == N:
        print(count)
        break 