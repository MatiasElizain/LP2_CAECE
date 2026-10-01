# Funcion para ver si el numero es par o impar
numeroTF = int(input("Ingrese un numero: "))

def par_impar (numeroParImpar):
    if numeroParImpar % 2 == 0:
        return True
    else:
        return False

print("Tu numero es par? ", par_impar(numeroTF))

print("=" * 80)

# Ahora con el filter y lambda
numeroLista = []
seguirAgregando = "S"

while seguirAgregando == "S":
    numero = int(input("Ingrese un numero: "))
    numeroLista.append(numero)
    seguirAgregando = input("Quiere seguir agregando? S/N ").upper()

es_par = lambda numero: numero % 2 == 0
es_impar = lambda numero: numero % 2 != 0

numerosPares = filter(es_par, numeroLista)
numerosImpares = filter(es_impar, numeroLista)

print("Los numeros pares son:", list(numerosPares))
print("Los numeros impares son:", list(numerosImpares))

""" es_par = lambda numero: numero % 2 == 0

numerosFiltrados = filter(es_par, numeroLista)

# numerosFiltrados = filter(lambda numero: numero % 2 == 0, numeroLista) Alternativa

print("Los numeros pares son:", list(numerosFiltrados)) """