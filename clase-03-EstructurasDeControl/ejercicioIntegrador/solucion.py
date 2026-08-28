cantidadEstudiantes = int(input("Numero de estudiantes: "))
nombresAlumnos = ""
notaFinal = 0
porcentajeAsistencia = 0

promocionados = 0
regulares = 0
libres = 0
desaprobados = 0

sumaNotas = 0
notaMasAlta = 0

for estudiante in range(cantidadEstudiantes):
    notaFinal = float(input("Ingrese nota: "))
    porcentajeAsistencia = int(input("Porcentaje asistencia: "))
    while (notaFinal < 0 or notaFinal > 10):
        notaFinal = int(input("Ingrese nota: "))

    # Promocionado si obtuvo una nota igual o superior a 7 
    # y una asistencia igual o superior al 75%.
    if porcentajeAsistencia >= 75:
        if notaFinal >= 7:
            print("Promocionado")
            promocionados += 1 # Aumento el contador de promocionados
        elif notaFinal >= 4 and notaFinal < 7:
            print("Regular")
            regulares += 1 # Aumento el contador de regulares
    elif porcentajeAsistencia < 75:
        print("Libre")
        libres += 1 # Aumento el contador de libres
    else:
        print("Desaprobado")
        desaprobados += 1 # Aumento el contador de desaprobados

# Calculo la suma total de todas las notas
sumaNotas += notaFinal

# Calculo la nota mas alta
if notaFinal > notaMasAlta:
    notaMasAlta = notaFinal

# Cantidad total de estudiantes.
print(cantidadEstudiantes)

# Cantidad de estudiantes promocionados.
print("Cantidad de estudiantes promocionados: ", promocionados)

# Cantidad de estudiantes regulares.
print("Cantidad de estudiantes regulares: ", regulares)

# Cantidad de estudiantes libres.
print("Cantidad de estudiantes libres: ", libres)

# Cantidad de estudiantes desaprobados.
print("Cantidad de estudiantes desaprobados: ", desaprobados)

# Calculo el promedio general de todas las notas
promedio = sumaNotas / cantidadEstudiantes

# Promedio general de las notas.
print("Promedio general de las notas: ", promedio)

# Nota más alta obtenida.
print("Nota más alta obtenida: ", notaMasAlta)