temperatura = float(input("Ingrese la temperatura: "))

origen = input("¿En qué unidad está? (C/F/K): ").upper()
destino = input("¿A qué unidad desea convertirla? (C/F/K): ").upper()

if origen == destino:
    print("La temperatura es:", temperatura, destino)

elif origen == "C":
    if destino == "F":
        resultado = (temperatura * 1.8) + 32
        print("La temperatura es:", resultado, "F")
    elif destino == "K":
        resultado = temperatura + 273.15
        print("La temperatura es:", resultado, "K")
    else:
        print("Unidad de destino inválida.")

elif origen == "F":
    if destino == "C":
        resultado = (temperatura - 32) / 1.8
        print("La temperatura es:", resultado, "C")
    elif destino == "K":
        resultado = ((temperatura - 32) / 1.8) + 273.15
        print("La temperatura es:", resultado, "K")
    else:
        print("Unidad de destino inválida.")

elif origen == "K":
    if destino == "C":
        resultado = temperatura - 273.15
        print("La temperatura es:", resultado, "C")
    elif destino == "F":
        resultado = ((temperatura - 273.15) * 1.8) + 32
        print("La temperatura es:", resultado, "F")
    else:
        print("Unidad de destino inválida.")

else:
    print("Unidad de origen inválida.")