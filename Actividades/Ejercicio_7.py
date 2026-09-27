sigueAgregandoPalabras = "S"
listaPalabras = []

while sigueAgregandoPalabras == "S":
    listaPalabras.append(input("Ingresar palabra: "))
    sigueAgregandoPalabras = input("Quiere seguir ingresando? S/N: ").upper()


# Longitud total de la cadena
print(f"La listas tiene {len(listaPalabras)} palabras")

# Identificacion de caracter inicial y final
for palabra in listaPalabras:
    print(f"Palabra: {palabra}")
    print(f"Inicial: {palabra[0]}")
    print(f"Final: {palabra[-1]}")

# Conversion integra a letras mayusculas
for i in range(len(listaPalabras)):
    listaPalabras[i] = listaPalabras[i].upper()

for lista in listaPalabras:
  print(lista)

# Visualizacion del texto en reversa
for palabraInversa in listaPalabras:
    print(f"Palabra: {palabraInversa[::-1]}")

# Verificar si la expresion es palindroma (se escribe igual al derecho y al reves)
for palabra in listaPalabras:
    if palabra == palabra[::-1]:
        print(f"{palabra} es palindroma")
    else:
        print(f"{palabra} no es palindroma")