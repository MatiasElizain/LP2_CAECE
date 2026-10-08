# Funciones y programación funcional

**Ejercicio 18: números positivos**  
Escribir una función que reciba una lista de números y devuelva otra lista que contenga únicamente los números positivos. Pedir al usuario los números y mostrar el resultado. Resolver el filtrado de dos maneras: con `filter()` y con *list comprehension*.

**Ejercicio 19: cuadrados**  
Escribir una función que reciba un número y devuelva su cuadrado. Luego, pedir al usuario una lista de números y generar una nueva lista con sus cuadrados. Resolver la transformación con `map()` y con *list comprehension*.

**Ejercicio 20: palabras largas**  
Pedir al usuario una lista de palabras. Crear una función que reciba una palabra y un número mínimo de caracteres, y devuelva `True` si la palabra supera esa longitud. Usar la función para filtrar la lista. Mostrar las palabras resultantes en mayúsculas.

**Ejercicio 21: precios con descuento**  
Escribir una función que reciba un precio y un porcentaje de descuento, y devuelva el precio final. Pedir al usuario una lista de precios y un porcentaje. Generar una nueva lista con los precios descontados usando `map()` y una función `lambda`.

**Ejercicio 22: temperaturas**  
Escribir una función que convierta grados Celsius a Fahrenheit. Pedir al usuario varias temperaturas en Celsius y mostrar sus conversiones. Después, filtrar las temperaturas originales que sean mayores a 30 °C. Comparar una solución con `map()` y `filter()` con otra que use *list comprehension*.

**Ejercicio 23: notas de estudiantes**  
Dada una lista de notas, crear una función que determine si una nota está aprobada según una nota mínima indicada por el usuario. Mostrar por separado las notas aprobadas y las desaprobadas. Calcular también el promedio de cada grupo mediante una función. Considerar qué debe devolver la función si un grupo está vacío.

**Ejercicio 24: nombres sin repetir**  
Pedir al usuario una lista de nombres que pueda contener espacios sobrantes, diferencias entre mayúsculas y minúsculas, y nombres repetidos. Crear funciones para normalizar cada nombre y obtener una lista sin duplicados, conservando el orden de aparición. Mostrar la lista final ordenada alfabéticamente.

**Ejercicio 25: desafío integrador**  
Pedir al usuario una lista de números. Crear funciones para:

- Conservar solamente los números pares.
- Elevar al cuadrado los números conservados.
- Calcular el promedio de los resultados.

Resolver los dos primeros pasos una vez con `filter()` y `map()`, y otra vez con *list comprehension*. Comprobar que ambas alternativas producen el mismo resultado.