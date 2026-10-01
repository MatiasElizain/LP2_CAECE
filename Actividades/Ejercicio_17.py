nombresLista = []
seguirAgregando = "S"

while seguirAgregando == "S":
    nombre = input("Ingrese un nombre: ")
    nombresLista.append(nombre)
    seguirAgregando = input("Quiere seguir agregando nombres? S/N ").upper()

print(nombresLista)

print("=" * 80)

# Estandarizo el formato de los nombres
def estandarizacionFormato (nombres):
    nombresEstandarizados = []
    for nombre in nombres:
        nombre = nombre.strip().capitalize()
        nombresEstandarizados.append(nombre)

    return nombresEstandarizados

nombresLista = estandarizacionFormato(nombresLista)

print(nombresLista)

print("=" * 80)

# Filtrar y conservar unicamente aquellos con extension superior a 4 letras

tiene_mas_de_4_letras = lambda nombre: len(nombre) > 4

nombresFiltrados = filter(tiene_mas_de_4_letras, nombresLista)
print("Nombres con mas de 4 letras ", list(nombresFiltrados))

print("=" * 80)

# Generar un nuevo listado transformando todo a letras mayusculas

todo_mayusculas = lambda nombre: nombre.upper()

nombresMayusculas = map(todo_mayusculas, nombresLista)

print("Todos los nombres en mayusculas:", list(nombresMayusculas))

""" nombresMayusculas = []

for nombre in nombresLista:
    nombresMayusculas.append(nombre.upper())

print(nombresMayusculas) """