contador = 0
suma = 0
maximo = None
minimo = None

numero = int(input("Ingrese un numero: "))

while numero != 0:
    contador += 1
    suma += numero
    if maximo is None or numero > maximo:
        maximo = numero
        # Si todavía no tengo un máximo, 
        # O si el número actual es mayor que el máximo que tengo guardado, 
        # entonces el máximo pasa a ser el número actual.

    if minimo is None or numero < minimo:
        minimo = numero
        # Si todavía no tengo un minimo, 
        # O si el número actual es mayor que el máximo que tengo guardado, 
        # entonces el minimo pasa a ser el número actual.
    
    numero = int(input("Ingrese un numero: "))

promedio = suma / contador

print("Fin del recorrido")
print("Cantidad de números:", contador)
print("Suma total:", suma)
print("Promedio:", promedio)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)