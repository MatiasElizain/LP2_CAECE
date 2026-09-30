listaNumeros = []
seguir = "S"

while seguir == "S":
    numero = int(input("Ingrese un numero: "))
    listaNumeros.append(numero)

    seguir = input("¿Quiere ingresar otro? S/N: ").upper()

print(listaNumeros)

def promedio (listaNumeros):
    sumaLista = sum(listaNumeros)
    cantidadNumeros = len(listaNumeros)
    promedio = sumaLista / cantidadNumeros
    return promedio

print("El promedio de los numeros es: ", promedio(listaNumeros))