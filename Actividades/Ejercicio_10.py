ciudades = ("Buenos Aires", "Cordoba", "Mendoza", "Rosario", "Quilmes")

# Desempaqueta la lista en variables individuales
(primero, segundo, tercero, cuarto, quinto) = ciudades
print("Desempaquetado:")
print(f"   ➤  Primera ciudad: {primero}")
print(f"   ➤  Segunda ciudad: {segundo}")
print(f"   ➤  Tercera ciudad: {tercero}")
print(f"   ➤  Cuarta ciudad: {cuarto}")
print(f"   ➤  Quinta ciudad: {quinto}")

print("=" * 60)

# Mostrar el nombre de cada ciudad por separado
for ciudad in ciudades:
    print(ciudad)

print("=" * 60)

# Intentar modificar una de las ciudades en la tupla
try:
    ciudades[1] = "Avellaneda"  # Esto genera un error
except TypeError as e:
    print("Error:", e)
    print("⚠️ No se puede modificar una tupla porque es inmutable.")