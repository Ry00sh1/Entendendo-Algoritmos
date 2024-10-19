#Um exemplo clássico para aplicarmos o algoritmo de recursão é para calcular o fatorial de um número:

def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number-1)

print(factorial(10))