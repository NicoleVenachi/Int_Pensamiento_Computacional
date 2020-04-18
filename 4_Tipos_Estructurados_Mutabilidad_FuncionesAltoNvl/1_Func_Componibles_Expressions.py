def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

sumar = lambda x, y: x + y

nums = [1, 2, 3]

print(aplicar_operaciones(-2))
print(aplicar_operacion(multiplicar_por_dos, nums))

print(aplicar_operacion(sumar_dos, nums))

print(sumar(2, 3))

print(type(sumar))
