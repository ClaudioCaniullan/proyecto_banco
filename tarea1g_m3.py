<<<<<<< HEAD

import uuid
# clase Cliente 

class Cliente:

	# inicializamos dos atributos de instancia
	def __init__(self, nombre,saldo):
		self.nombre = nombre
        self.id_cliente = uuid.uuid4()
		self.saldo = saldo


	# métodos
	def girar(self, monto):
		pass

	def abonar(self, monto):
		pass

	def mostrar_saldo(self):
		pass
=======
class Cliente:

# inicializamos dos atributos de instancia
    def __init__(self, nombre, id_unico, saldo):
        self.nombre = nombre
        self.id_unico = id_unico
        self.saldo = saldo


	# métodos
    def girar(self, giro):
        if self.saldo >= giro:
            self.saldo -= giro
            print(self.saldo)
        else:
            print("No se puede efectuar la transacción")
>>>>>>> a5267fe572efe979c00f6e87186f6984244edc51

    def abonar(self, abonar):
        self.saldo += abonar
        print(self.saldo)

    def mostrar_saldo(self):
        return self.saldo

# Clase Financiera

class Financiera:

	self.saldo_institucional = 100000000

	def __init__(self, nombre):
		self.nombre = nombre
        self.id_unico = uuid.uuid4()
		self.clientes = []

    # claudio, revisar script
	def agregar_cliente(self, cliente):
		# se agregan los atributos del cliente a una tupla
		tupla = (cliente.nombre, cliente.id_unico, cliente.saldo)
		self.clientes.append(tupla) # la tupla se guarda en la lista de instancia
		# se verifica que se guardo el cliente
		print('El cliente ha sido agregado : ', self.clientes)
    
    # claudio, revisar script
	def eliminar_cliente(self):
		i = int(input('ingrese el indice en la lista que corresponde al cliente a eliminar: '))
		self.clientes.pop(i)
		print('El cliente ha sido eliminado : ', self.clientes)


	def tranferir(self):
		pass

	def giros_totales(self):
		pass

	def abonos_totales(self):
		pass

	def mostrar_saldo_institucional(self):
		pass

### Modelos de pruebas de funciones agregar y eliminar clientes

# se crea financiera
financiera1 = Financiera('piraña')

"""
# se crean clientes
cliente1 = Cliente('Ale', 1, 1)


<<<<<<< HEAD
# se agregan clientes a la financiera
financiera1.agregar_cliente(cliente1)
=======
cliente1 = Cliente('Walter', 1, 100000)
cliente2 = Cliente('Claudio', 2, 500000)
cliente3 = Cliente('Miguel', 3, 600000)
cliente4 = Cliente('Sebastian', 1, 700000)

print("Nombre cliente: ", cliente1.nombre, "Cliente Giro: ", cliente1.girar(20000), "Cliente Abono: ", cliente1.abonar(15000), "Mostrar Saldo: ", cliente1.saldo)
print("Nombre cliente: ", cliente2.nombre, "Cliente Giro: ", cliente2.girar(50000), "Cliente Abono: ", cliente2.abonar(20000), "Mostrar Saldo: ", cliente2.saldo)
print("Nombre cliente: ", cliente3.nombre, "Cliente Giro: ", cliente3.girar(25000), "Cliente Abono: ", cliente3.abonar(14000), "Mostrar Saldo: ", cliente3.saldo)
print("Nombre cliente: ", cliente4.nombre, "Cliente Giro: ", cliente4.girar(25000), "Cliente Abono: ", cliente4.abonar(20000), "Mostrar Saldo: ", cliente4.saldo)
>>>>>>> a5267fe572efe979c00f6e87186f6984244edc51


# se elimina el cliente1
financiera1.eliminar_cliente()

# verificacion de los clientes en la financiera
print('Los clientes en la financiera1 son: ',financiera1.clientes)
"""

input()

