listaNotas = []
seguirAgregando = "S"
minimaAprobacion = float(input("Ingrese la nota minima para aprobar: "))

while seguirAgregando == "S":
    notas = float(input("Ingrese la nota del alumno: "))
    listaNotas.append(notas)
    seguirAgregando = input("Quiere seguir agregando notas S/N: ").upper()

print(f"La lista de notas es: {listaNotas}")


def aprueba_desaprueba(notas, nota_minima):
    notas_aprobadas = []
    notas_desaprobadas = []

    for nota in notas:
        if nota >= nota_minima:
            notas_aprobadas.append(nota)
        else:
            notas_desaprobadas.append(nota)

    return notas_aprobadas, notas_desaprobadas


def promedio(notas):
    if len(notas) == 0:
        return None

    return sum(notas) / len(notas)


aprobadas, desaprobadas = aprueba_desaprueba(listaNotas, minimaAprobacion)

promedio_aprobadas = promedio(aprobadas)
promedio_desaprobadas = promedio(desaprobadas)

print(f"\nLista completa de notas: {listaNotas}")
print(f"Notas aprobadas: {aprobadas}")
print(f"Notas desaprobadas: {desaprobadas}")

if promedio_aprobadas is None:
    print("No hay notas aprobadas para calcular el promedio.")
else:
    print(f"Promedio de las notas aprobadas: {promedio_aprobadas:.2f}")

if promedio_desaprobadas is None:
    print("No hay notas desaprobadas para calcular el promedio.")
else:
    print(f"Promedio de las notas desaprobadas: " f"{promedio_desaprobadas:.2f}")
