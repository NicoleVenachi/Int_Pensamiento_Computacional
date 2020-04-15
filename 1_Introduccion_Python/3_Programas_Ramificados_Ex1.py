name_1 = input('Digita tu nombre, usuario 1: \t')
num_1 = int(input('Digita tu edad, usuario 1: \t'))
name_2 = input('Digita tu nombre, usuario 2: \t')
num_2 = int(input('Digita tu edad, usuario 2: \t'))

if (num_1 > num_2):
    print(f'{name_1} es mayor')
elif (num_1 < num_2):
    print(f'{name_2} es mayor')
else:
    print(f'{name_1} y {name_2} tienen la misma edad, de {num_1} years')
