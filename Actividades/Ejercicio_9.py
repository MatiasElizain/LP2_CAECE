personas = [
    {"nombre": "Carolina Gomez", "edad": 35},
    {"nombre": "Juan Perez", "edad": 29},
    {"nombre": "Mariela Ramirez", "edad": 27},
]

nombreABuscar = input("Nombre a buscar: ").strip()

encontroPersona = False

for persona in personas:
    if persona["nombre"].upper() == nombreABuscar.upper():
        print(f'{persona["nombre"]} tiene {persona["edad"]} años')
        encontroPersona = True
        break

if encontroPersona == False:
    print(f"No se encontró a {nombreABuscar}")