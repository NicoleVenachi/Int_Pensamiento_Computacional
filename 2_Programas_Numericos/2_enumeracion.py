objetivo = int(input('Escoge un entero: \t'))
respuesta = 0

while respuesta**2 < objetivo:  # Saco el exp 2 de todos los enteros
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')  # El entero es
else:
    print(f'{objetivo} no tiene raiz cuadrada exacta')
