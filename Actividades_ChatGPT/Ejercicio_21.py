listaPrecios = []
seguirAgregando = "S"

descuento = int(input("Ingrese el descuento sin %: "))

while seguirAgregando == "S":
    precio = float(input("Ingrese el precio: "))
    listaPrecios.append(precio)
    seguirAgregando = input("Quiere seguir agregando precios S/N: ").upper()

print(f"Precios sin descuento aplicado: {listaPrecios}")

print("=" * 80)


def precioDescuento(precios):
    listaPreciosDescuento = []
    for precio in precios:
        precios = precio - (precio * descuento / 100)
        listaPreciosDescuento.append(precios)
    return listaPreciosDescuento


print(
    f"Los precios con el descuento del {descuento}% quedan en: {precioDescuento(listaPrecios)}"
)
