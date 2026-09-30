estudiantes = [
    {"nombre": "Ana", "notas": [8, 9, 7]},
    {"nombre": "Juan", "notas": [6, 5, 7]},
    {"nombre": "Lucia", "notas": [10, 9, 8]}
]

# Obtener la media de calificaciones por alumno
for estudiante in estudiantes:
    promedio = sum(estudiante["notas"]) / len(estudiante["notas"])
    estudiante["promedio"] = promedio

    print(f'{estudiante["nombre"]} tiene promedio: {promedio}')

print("=" * 60)

# Identificar al alumno con el desempeño más alto
mejorAlumno = estudiantes[0]

for estudiante in estudiantes:
    if estudiante["promedio"] > mejorAlumno["promedio"]:
        mejorAlumno = estudiante

print(
    f'El alumno con mejor desempeño es {mejorAlumno["nombre"]} '
    f'con promedio {mejorAlumno["promedio"]}'
)

print("=" * 60)

# Buscar alumno por nombre
nombreABuscar = input("Ingrese el nombre del alumno a buscar: ")

encontrado = False

for estudiante in estudiantes:
    if estudiante["nombre"].upper() == nombreABuscar.upper():
        print(f'Nombre: {estudiante["nombre"]}')
        print(f'Notas: {estudiante["notas"]}')
        print(f'Promedio: {estudiante["promedio"]}')
        encontrado = True
        break

if encontrado == False:
    print("Alumno no encontrado")