listaNumero = []
indice = 0

for indice in range(5):
    numeroIngresar = int(input("Ingrese un numero: "))
    listaNumero.append(numeroIngresar)

print("=" * 60)

# Imprimir la lista en su orden original
for numero in listaNumero:
    print(numero)

print("=" * 60)

# Ordena la lista de manera ascendente y mostrarla
listaNumero.sort()

for numero in listaNumero:
    print(numero)

print("=" * 60)

# Calcular la suma de todos los elementos de la lista
sumaTotal = sum(listaNumero)
print(f"La suma total es: {sumaTotal}")

print("=" * 60)

# Mostrar el numero mas grande y el mas chico de la lista
numeroMasGrande = max(listaNumero)
numeroMasChico = min(listaNumero)

print(f"El numero mas grande de la lista es: {numeroMasGrande}")
print(f"El numero mas chico de la lista es: {numeroMasChico}")
