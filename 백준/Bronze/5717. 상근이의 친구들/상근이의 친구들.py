while True:
    M, F = map(int, input().split())
    
    if M != 0 and F != 0:
        print(M+F)
    elif M == F == 0:
        break