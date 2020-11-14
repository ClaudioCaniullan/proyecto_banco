

# clase Cliente 

class Cliente:

	# inicializamos dos atributos de instancia
	def __init__(self, nombre, id_unico, saldo):
		self.nombre = nombre
		self.id_unico = id_unico
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

	#lista_clientes = []

	def __init__(self, nombre, id_unico, saldo_institucional, clientes):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo_institucional = saldo_institucional
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
financiera1 = Financiera('piraña',1, 2, 3)

# se crean clientes
cliente1 = Cliente('Ale', 1, 1)
cliente2 = Cliente('Pedro', 2, 2)
cliente3 = Cliente('Jorge',3,3)

# se agregan clientes a la financiera
financiera1.agregar_cliente(cliente1)
financiera1.agregar_cliente(cliente2)
financiera1.agregar_cliente(cliente3)

# se elimina el cliente1
financiera1.eliminar_cliente()

# verificacion de los clientes en la financiera
print('Los clientes en la financiera1 son: ',financiera1.clientes)


input()

