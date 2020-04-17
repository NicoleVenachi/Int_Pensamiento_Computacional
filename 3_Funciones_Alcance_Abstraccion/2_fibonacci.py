def fibonacci(n):
    """Calcula la sucesion de fibonacci para n repeticiones.
        n int >= 0
        return n = n_anterior - n_pre_anterior
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n -2)

n = int(input('Escribe el elemento de la sucesion de fibonacci que desees hallar: \t'))
print(f'El elemento {n} de la sucesion, es {fibonacci(n)}')
