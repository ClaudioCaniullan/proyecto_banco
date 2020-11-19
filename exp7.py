import uuid

class Cliente():

	def __init__(self, nombre, saldo):
		self.nombre = nombre
		self.saldo = saldo
		self.id_cliente = uuid.uuid4()

	def girar(self, giro):
		if self.saldo >= giro:
			self.saldo -= giro
			print(self.saldo)
		else:
			print('no puede efectuar la transacción')

	def abonar(self, abonar):
		self.saldo += abonar
		print(self.saldo)

	def mostrar_saldo(self):
		print(self.saldo)



class Financiera():

	def __init__(self, nombre):
		self.nombre = nombre
		self.saldo_institucional = 100000000
		self.id_unico = uuid.uuid4()
		self.clientes = []

	def agregar(self, cliente):
		tupla = [cliente.nombre, cliente.saldo + 10**6]
		self.saldo_institucional = self.saldo_institucional - 10**6
		self.clientes.append(tupla)

		print('cliente agregado', self.clientes)

	def eliminar(self):
		i = input('ingrese el indice en la lista que corresponde al cliente a eliminar: ')
		self.clientes.pop(i)
		print('el cliente ha sido eliminado', self.clientes)


	def tranferir(self, cliente1, monto, cliente2):
		cliente1.saldo -= monto
		cliente2.saldo += monto 
		print( 'saldos actuales clientes 1 y 2',cliente1.saldo, cliente2.saldo, self.clientes)

		pass

	def giros_totales(self):
		pass

	def abonos_totales(self):
		pass

	def mostrar_saldo_institucional(self):
		pass


cliente1 = Cliente('carlos', 30000)
cliente2 = Cliente('jose', 45000)

financiera1 = Financiera('Vida')
financiera1.agregar(cliente1)
financiera1.agregar(cliente2)


financiera1.tranferir(cliente1, 10000, cliente2)


input()