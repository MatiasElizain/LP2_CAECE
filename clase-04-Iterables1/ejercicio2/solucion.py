diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# Desempaquetar los dias en variables individuales
primerDia, segundoDia, tercerDia, cuartoDia, quintoDia = diasSemana
print("Desempaquetado:")
print(f"   ➤  Primer dia de la semana: {primerDia}")
print(f"   ➤  Segundo dia de la semana: {segundoDia}")
print(f"   ➤  Tercer dia de la semana: {tercerDia}")
print(f"   ➤  Cuarto dia de la semana: {cuartoDia}")
print(f"   ➤  Quinto dia de la semana: {quintoDia}")

# Mostrar el nombre de cada dia por separado
print("Cada dia por separado:")
for dia in diasSemana:
    print(dia)


# Agregar una nueva ciudad a la lista de dias
diasSemana.append("Quilmes")
print(f"Lista de dias con la ciudad agregada: {diasSemana}")
