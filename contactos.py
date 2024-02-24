class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono):
        contacto = Contacto(nombre, telefono)
        self.contactos.append(contacto)
        print(f"Contacto '{nombre}' agregado con éxito.")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}")
        else:
            print("La agenda está vacía.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}")
                return
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")

agenda = Agenda()

agenda.agregar_contacto("Juan", "+50523456789")
agenda.agregar_contacto("María", "+50587654321")

agenda.mostrar_contactos()

agenda.buscar_contacto("Juan")
agenda.buscar_contacto("Pedro")
