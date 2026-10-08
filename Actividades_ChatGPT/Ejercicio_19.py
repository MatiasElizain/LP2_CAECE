listaNumeros = []
seguirAgregando = "S"

while seguirAgregando == "S":
    numero = int(input("Agregue un numero: "))
    seguirAgregando = input("Quiereseguir agregando S/N: ").upper()
    listaNumeros.append(numero)

print(listaNumeros)

def cuadrados (numeros):
    listaCuadrados = []
    for numero in numeros:
        numeros = numero ** 2
        listaCuadrados.append(numeros)
    
    return listaCuadrados

print(f"La lista con los valores al cuadrado es: {cuadrados(listaNumeros)}")

print("=" * 80)

# Uso de map
cuadradosMap = map(lambda numero: numero ** 2, listaNumeros)
print(f"Lista con numeros al cuadrado con map: {list(cuadradosMap)}")

print("=" * 80)

# Con list comprehension
comprehensionCuadrados = [numero ** 2 for numero in listaNumeros]
print(f"Lista con numeros al cuadrado con list comprehension: {list(comprehensionCuadrados)}")
