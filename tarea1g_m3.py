

# clase Cliente 

class Cliente:

	# inicializamos dos atributos de instancia
	def __init__(self, nombre, id_unico, saldo):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo = saldo


	# métodos
	def girar(self, id_unico, giro):
		if self.id_unico.saldo>= giro:
			self.id_unico.saldo -=giro
		else:
			print("No se puede efectuar la transacción")

	def abonar(self, id_unico, abono):
		self.id_unico.saldo +=abono

	def mostrar_saldo(self, id_unico):
		return id_unico.saldo
		



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

#Giro de cliente 
cliente1.girar(1, 50000)
#Abono a cliente
cliente1.abonar(1, 15000)
#Mostrar saldo cliente
cliente1.mostrar_saldo(1)

clientes.append(cliente1)

Financiera1 = Financiera('Piraña', 1, 100000, clientes)



