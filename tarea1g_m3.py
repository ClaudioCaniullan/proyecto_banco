
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


# se agregan clientes a la financiera
financiera1.agregar_cliente(cliente1)


# se elimina el cliente1
financiera1.eliminar_cliente()

# verificacion de los clientes en la financiera
print('Los clientes en la financiera1 son: ',financiera1.clientes)
"""

input()

