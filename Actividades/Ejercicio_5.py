unidades = int(input("Ingrese unidades a comprar: "))
precioPorUnidad = 10

if unidades >= 5 and unidades <= 10:
    subtotal = unidades * precioPorUnidad
    descuentoDel_10 = subtotal * 0.1
    total = subtotal - descuentoDel_10
    print("Subtotal:", subtotal)
    print("Descuento del 10%:", descuentoDel_10)
    print("Total a pagar:", total)
elif unidades > 10:
    subtotal = unidades * precioPorUnidad
    descuentoDel_20 = subtotal * 0.2
    total = subtotal - descuentoDel_20
    print("Subtotal:", subtotal)
    print("Descuento del 20%:", descuentoDel_20)
    print("Total a pagar:", total)
else:
    total = unidades * precioPorUnidad
    print(f"El precio final no incluye descuento: {total}")
