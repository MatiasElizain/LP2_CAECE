primerNumero = int(input("Ingrese el primer numero: "))
segundoNumero = int(input("Ingrese el segundo numero: "))

def sumar (a, b):
    return a + b

print("Resultado suma: ", sumar(primerNumero, segundoNumero))
print("=" * 60)

def restar (a, b):
    return a - b

print("Resultado resta: ", restar (primerNumero, segundoNumero))
print("=" * 60)

def multiplicar (a, b):
    return a * b

print("Resultado multiplicacion: ", multiplicar (primerNumero, segundoNumero))
print("=" * 60)

def dividir (a, b):
    return a / b

print("Resultado division: ", dividir (primerNumero, segundoNumero))
print("=" * 60)

def potencia (a, b):
    return a ** b

print("Resultado potencia: ", potencia (primerNumero, segundoNumero))
print("=" * 60)

def restoDivision (a, b):
    return a % b

print("Resultado resto de división: ", restoDivision (primerNumero, segundoNumero))
print("=" * 60)