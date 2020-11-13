

# clase Cliente 

class Cliente:

	# inicializamos dos atributos de instancia
	def __init__(self, nombre, id, saldo):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo = saldo


	# métodos
	def girar(self, monto):
		pass

	def abonar(self, monto):
		pass

	def mostrar_saldo(self,):
		pass



# Clase Financiera

class Financiera:

	def __init__(self, nombre, id_unico, saldo_institucional, clientes):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo_institucional = saldo_institucional
		self.clientes = clientes

	def agregar_cliente(self, ):
		pass

	def eliminar_cliente(self, ):
		pass

	def tranferir(self, ):
		pass

	def giros_totales(self, ):
		pass

	def abonos_totales(self, ):
		pass

	def mostrar_saldo_institucional(self, ):
		pass

		
clientes = []

cliente1 = Cliente('perro', 1, 1000000)
cliente2 = Cliente('perra,', 2, 2000000)

clientes.append(cliente1)

Financiera1 = Financiera('Piraña', 1, 100000, clientes)



