edad = int(input("Ingrese su edad: "))

# Sin estructuras condicionales

#menorDeEdad = edad < 18
#print(f"Sos menor de edad: {menorDeEdad}")
#adulto = edad >= 18 and edad <= 65
#print(f"Sos adulto: {adulto}")
#mayorDeEdad = edad > 65
#print(f"Sos mayor de edad: {mayorDeEdad}")

# Con estructura condicional

if edad < 18:
    print("Sos menor de edad")
elif edad >= 18 and edad <= 65:
    print("Sos adulto")
else:
    print("Sos mayor de edad")