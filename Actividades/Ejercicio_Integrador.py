import random

def crearCuenta (numero, nombre, tipoCuenta, saldoInicial):
    return {
        "numero": numero,
        "nombre": nombre,
        "tipoCuenta": tipoCuenta,
        "saldo": saldoInicial
    }


def pedirDatosParaCrearCuenta():

    print("Inicia el proceso de creacion de cuenta")

    numero = random.randint(100000, 999999)
    nombre = input("Nombre: ")

    tipoCuenta = input("Tipo de cuenta: COR/AHO: ").upper()
    while tipoCuenta != "COR" and tipoCuenta != "AHO":
        print("Tipo de cuenta invalido")
        tipoCuenta = input("Vuelva a ingresar tipo de cuenta: COR/AHO: ").upper()

    saldoInicial = 0
    if tipoCuenta == "COR":
        saldoInicial = 2000000
    else:
        saldoInicial = 3000000

    print("Finaliza el proceso de creacion de cuenta")
    return crearCuenta(numero, nombre, tipoCuenta, saldoInicial)

def buscarCuenta(numeroCuenta):
    cuentaEncontrada = None
    for cuenta in cuentas:
        if numeroCuenta == cuenta.get("numero"):
            cuentaEncontrada = cuenta

    return cuentaEncontrada

# Ahora quiero agregar cuentas nuevas a un listado
cuentas = []
sigueAgregandoCuenta = "SI"
while sigueAgregandoCuenta == "SI":
    cuentas.append(pedirDatosParaCrearCuenta())
    sigueAgregandoCuenta = input("Seguir agregando? SI/NO: ").upper()

print(f"Cuentas bancarias: {cuentas}")

print("=" * 80)

# Depositos
cuentaABuscar = cuentas[0]["numero"]
print(f"Cuenta encontrada: {buscarCuenta(cuentaABuscar)}")
