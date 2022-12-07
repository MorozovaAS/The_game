position = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print()
print(" ", position[0] ," ", "|"," ", position[1], " ", "|", " ", position[2]," ")
print("-" * 21)
print(" ", position[3] ," ", "|"," ", position[4], " ", "|", " ", position[5]," ")
print("-" * 21)
print(" ", position[6] ," ", "|"," ", position[7], " ", "|", " ", position[8]," ")
print()
for i in range(1, len(position)+1):
    if i % 2 != 0:
        p = int(input('Выберите позицию: '))
        if position[p-1] == 'X' or position[p-1] == 'O':
            p = int(input('Выберите другую позицию, эта занята: '))  
        position[p-1] = 'X'
        print()
        print(" ", position[0] ," ", "|"," ", position[1], " ", "|", " ", position[2]," ")
        print("-" * 21)
        print(" ", position[3] ," ", "|"," ", position[4], " ", "|", " ", position[5]," ")
        print("-" * 21)
        print(" ", position[6] ," ", "|"," ", position[7], " ", "|", " ", position[8]," ")
        print()
        if position[0] == 'X' and position[1] == 'X' and position[2] == 'X':
            print('X победили')
            break
        elif position[3] == 'X' and position[4] == 'X' and position[5] == 'X':
            print('X победили')
            break
        elif position[6] == 'X' and position[7] == 'X' and position[8] == 'X':
            print('X победили')
            break
        elif position[0] == 'X' and position[4] == 'X' and position[8] == 'X':
            print('X победили')
            break       
        elif position[2] == 'X' and position[4] == 'X' and position[6] == 'X':
            print('X победили')
            break 
        elif position[0] == 'X' and position[3] == 'X' and position[6] == 'X':
            print('X победили')
            break 
        elif position[1] == 'X' and position[4] == 'X' and position[7] == 'X':
            print('X победили')
            break 
        elif position[2] == 'X' and position[5] == 'X' and position[8] == 'X':
            print('X победили')
            break 
 
                
    elif i % 2 == 0:
        p = int(input('Выберите позицию: '))
        if position[p-1] == 'X' or position[p-1] == 'O':
            p = int(input('Выберите другую позицию, эта занята: '))
        position[p-1] = 'O'
        print()
        print(" ", position[0] ," ", "|"," ", position[1], " ", "|", " ", position[2]," ")
        print("-" * 21)
        print(" ", position[3] ," ", "|"," ", position[4], " ", "|", " ", position[5]," ")
        print("-" * 21)
        print(" ", position[6] ," ", "|"," ", position[7], " ", "|", " ", position[8]," ")
        print()
        if position[0] == 'O' and position[1] == 'O' and position[2] == 'O':
            print('O победили')
            break
        elif position[3] == 'O' and position[4] == 'O' and position[5] == 'O':
            print('O победили')
            break
        elif position[6] == 'O' and position[7] == 'O' and position[8] == 'O':
            print('O победили')
            break
        elif position[0] == 'O' and position[4] == 'O' and position[8] == 'O':
            print('O победили')
            break       
        elif position[2] == 'O' and position[4] == 'O' and position[6] == 'O':
            print('O победили')
            break 
        elif position[1] == 'O' and position[4] == 'O' and position[7] == 'O':
            print('O победили')
            break 
        elif position[0] == 'O' and position[3] == 'O' and position[6] == 'O':
            print('O победили')
            break 
        elif position[2] == 'O' and position[5] == 'O' and position[8] == 'O':
            print('O победили')
            break 
