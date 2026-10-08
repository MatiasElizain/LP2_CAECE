listaNumeros = []
seguirAgregando = "S"

while seguirAgregando == "S":
    numero = int(input("Escriba el numero a agregar: "))
    listaNumeros.append(numero)

    seguirAgregando = input("Quiere seguir agregando S/N: ").upper()


print(listaNumeros)

# Con funcion
def positivos (numeros):
    listaPositivo = []

    for numero in numeros:
        if numero >= 0:
            listaPositivo.append(numero)
    return listaPositivo

print(f"La lista de numeros positivos es: {positivos(listaNumeros)}")

print("=" * 80)

# Con filter
son_positivos = lambda numeros: numeros >= 0
numerosPositivos = filter(son_positivos, listaNumeros)
print(f"Los numeros posivos son: {list(numerosPositivos)}")

print("=" * 80)

# Con list comprehension
comprehensionPositivos = [numero for numero in listaNumeros if numero >= 0]
print(f"Positivos con list comprehension: {comprehensionPositivos}")