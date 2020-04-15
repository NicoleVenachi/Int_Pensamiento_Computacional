objetivo = int(input('Escoge un numero: \t'))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)  # Libro de negativos
respuesta = (alto + bajo) / 2  # Hallo el elemento de la mitad

while abs(respuesta**2 - objetivo) >= epsilon:  # Si el elemento a la mitad al cuadrado no es la raiz cuadrada, continuo. Se detendria cuando sea menor la diferencia sea menor que epsilon, es decir, cuando me pase, bien sea por el limite superior o inferior
    if respuesta**2 < objetivo:  # Defino si me voy a la mitad superior o inferior. Si la mitad al cuadrado es mayor, el nuevo punto bajo es la anteroir respuesta, es decir, la mitad. El nuevo punto bajo es la mitad
        bajo = respuesta
    else:
        alto = respuesta  # El nuevo punto alto es la mitad

    respuesta = (alto + bajo) / 2  # parto a la mitad el espacio de busqueda
    # print(f'{alto} {bajo} {respuesta}')

print(f'La raiz cuadrada de { objetivo} es la {respuesta}')
