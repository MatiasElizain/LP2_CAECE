listaNumeros = []
seguirAgregando = "S"

while seguirAgregando == "S":
    numero = int(input("Agregue un numero: "))
    seguirAgregando = input("Quiereseguir agregando S/N: ").upper()
    listaNumeros.append(numero)

print(listaNumeros)

print("=" * 80)

def paresCuadrados (numeros):
    listaParesCuadrados = []
    for numero in numeros:
        if numero % 2 == 0:
            numeroCuadrado = numero ** 2
            listaParesCuadrados.append(numeroCuadrado)
    return listaParesCuadrados

print(f"La lista con los numeros pares al cuadrado quedan asi: {paresCuadrados(listaNumeros)}")

print("=" * 80)

# Filter y map
numerosPares = filter(lambda numero: numero % 2 == 0, listaNumeros)
numerosParesCuadrados = map(lambda numero: numero ** 2, numerosPares)

CuadradoYParesLista = list(numerosParesCuadrados)

print(f"Con Filter y Map: {CuadradoYParesLista}")

print("=" * 80)

# Con list comprehension
paresYCuadrados = [numero ** 2 for numero in listaNumeros if numero % 2 == 0]

print(f"Con list comprehension: {list(paresYCuadrados)}")

# Promedio de los resultados
print(f"El promedio de los resultados es: {sum(CuadradoYParesLista) / len(CuadradoYParesLista)}")