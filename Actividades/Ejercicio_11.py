listaNotas = []

for notas in range(5):
    notas = float(input("Ingrese la nota del alumno: "))
    listaNotas.append(notas)
    print(listaNotas)

print("=" * 60)

# Promedio de las calificaciones
sumaTotalNotas = sum(listaNotas)
cantidadNotas = len(listaNotas)
promedioNotas = sumaTotalNotas/cantidadNotas
print(f"El promedio de las notas es: {promedioNotas}")

print("=" * 60)

# Total de alumnos que aprobaron (condiderando aprobado con 7 o mas) y desaprobaron
cantidadAprobados = 0
cantidadDesaprobados = 0

for notas in listaNotas:
    if notas >= 7:
        cantidadAprobados += 1
    else:
        cantidadDesaprobados += 1

print(f"Aprobaron {cantidadAprobados} alumnos")
print(f"Desaprobaron {cantidadDesaprobados} alumnos")

print("=" * 60)

# Listado de notas que superen la media calculada
notasSuperanMedia = []

for notas in listaNotas:
    if notas >= promedioNotas:
        notasSuperanMedia.append(notas)

print(notasSuperanMedia)