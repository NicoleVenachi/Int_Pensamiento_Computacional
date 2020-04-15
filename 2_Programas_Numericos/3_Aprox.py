objetivo = int(input('Escoge un entero: \t'))
epsilon = 0.001
paso = epsilon**2  # Esto es lo que le va sumadno a la respuesta
respuesta = 0.0

while (abs(respuesta**2 - objetivo) >= epsilon) and (respuesta <= objetivo):  # conforme la diferencia se aproxima a epsilon, sigo elevando al cuadrado al exponencial. Y blindo ante negativos
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:  # Si se paso de iteraciones
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
