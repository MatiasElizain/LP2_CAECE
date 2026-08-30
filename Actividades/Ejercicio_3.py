numero = 1
numeroAnterior = 0

for indice in range (1,11):
    print(f"Resultado: {numeroAnterior}")
    resultado = numero + numeroAnterior
    numeroAnterior = numero
    numero = resultado