# Carga de nombres
nombresLista = []
seguirAgregando = "S"

while seguirAgregando == "S":
    nombre = input("Ingrese un nombre: ")
    nombresLista.append(nombre)
    seguirAgregando = input("¿Quiere seguir agregando nombres? S/N: ").upper()


# Resolucion mediante funciones y ciclos for
def estandarizarNombres(nombres):
    nombresEstandarizados = []

    for nombre in nombres:
        nombresEstandarizados.append(nombre.strip().capitalize())

    return nombresEstandarizados


def filtrarNombresLargos(nombres):
    nombresFiltrados = []

    for nombre in nombres:
        if len(nombre) > 4:
            nombresFiltrados.append(nombre)

    return nombresFiltrados


def convertirAMayusculas(nombres):
    nombresMayusculas = []

    for nombre in nombres:
        nombresMayusculas.append(nombre.upper())

    return nombresMayusculas


nombresEstandarizados = estandarizarNombres(nombresLista)
nombresFiltrados = filtrarNombresLargos(nombresEstandarizados)
nombresMayusculas = convertirAMayusculas(nombresEstandarizados)

print("\nResultados utilizando funciones y ciclos for")
print("Nombres estandarizados:", nombresEstandarizados)
print("Nombres con mas de 4 letras:", nombresFiltrados)
print("Nombres en mayusculas:", nombresMayusculas)


# Resolucion mediante list comprehension
nombresEstandarizadosComprension = [
    nombre.strip().capitalize() for nombre in nombresLista
]

nombresFiltradosComprension = [
    nombre for nombre in nombresEstandarizadosComprension if len(nombre) > 4
]

nombresMayusculasComprension = [
    nombre.upper() for nombre in nombresEstandarizadosComprension
]

print("\nResultados utilizando list comprehension")
print("Nombres estandarizados:", nombresEstandarizadosComprension)
print("Nombres con mas de 4 letras:", nombresFiltradosComprension)
print("Nombres en mayusculas:", nombresMayusculasComprension)


# Comparacion de ambas alternativas
print("\nComparacion de resultados")
print(
    "La estandarizacion produjo el mismo resultado:",
    nombresEstandarizados == nombresEstandarizadosComprension
)
print(
    "El filtrado produjo el mismo resultado:",
    nombresFiltrados == nombresFiltradosComprension
)
print(
    "La conversion a mayusculas produjo el mismo resultado:",
    nombresMayusculas == nombresMayusculasComprension
)
