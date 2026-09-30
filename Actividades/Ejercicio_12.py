agenda = [
    {"nombre": "Lucas Garcia", "telefono": 1158239212},
    {"nombre": "Juan Perez", "telefono": 1172937467},
    {"nombre": "Florencia Fernandez", "telefono": 1167628982},
]

# Incorporar nuevo contacto
agregarContacto = input("¿Quiere agregar un nuevo contacto? S/N: ").upper()
seguirAgregando = "S"

if agregarContacto == "S":
    seguirAgregando = "S"

    while seguirAgregando == "S":
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el telefono: ")

        nuevoContacto = {
            "nombre": nombre,
            "telefono": telefono
        }

        agenda.append(nuevoContacto)

        seguirAgregando = input("¿Quiere agregar otro contacto? S/N: ").upper()
else:
    print("No se agregaron nuevos contactos")

print(agenda)

print("=" * 60)

# Buscar el numero de alguien
print("Buscar el numero por nombre del contacto")
nombreBuscar = input("Ingrese el nombre a buscar: ")
encontrado = False

for contacto in agenda:
    if contacto["nombre"].upper() == nombreBuscar.upper():
        print(f"Telefono: {contacto["telefono"]}")
        encontrado = True
        break

if encontrado == False: 
    print("Contacto no encontrado")

print("=" * 60)

# Actualizar un registro telefonico existente
print("Actualizar un registro telefonico existente")
nombreActualizar =  input("Ingrese el nombre a buscar: ")
encontrado = False

for contacto in agenda:
    if contacto["nombre"].upper() == nombreActualizar.upper():
        nuevoTelefono = int(input("Ingrese el nuevo telefono: "))
        contacto["telefono"] = nuevoTelefono
        print("Contacto actualizado")
        break

if encontrado == False: 
    print("Contacto no encontrado")

print(agenda)

print("=" * 60)

# Quitar una persona de la lista
print("Eliminar un contacto de la agenda")
nombreEliminar = input("Ingrese el nombre a eliminar: ")
encontrado = False

for contacto in agenda:
    if contacto["nombre"].upper() == nombreEliminar.upper():
        agenda.remove(contacto)
        print("Contacto eliminado exitosamente")
        break

print("=" * 60)

# Ver el listado completo de la agenda
for contacto in agenda:
    print(f'{contacto["nombre"]} - {contacto["telefono"]}')
    