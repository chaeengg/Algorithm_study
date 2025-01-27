hamburger = []
drink = []
set_menu = []

for i in range(3):
    hamburger.append(int(input()))

for j in range(2):
    drink.append(int(input()))

for ham in range(3):
    for dr in range(2):
        set_menu.append(hamburger[ham] + drink[dr])
        
print(min(set_menu)-50)