temperatura = float(input("Ingrese una temperatura en Celsius: "))

conversion = input("¿A qué desea convertirla? (F/K): ").upper()

if conversion == "F":
    resultado = (temperatura * 1.8) + 32
    print("La temperatura en Fahrenheit es:", resultado)

elif conversion == "K":
    resultado = temperatura + 273.15
    print("La temperatura en Kelvin es:", resultado)

else:
    print("Opción inválida.")