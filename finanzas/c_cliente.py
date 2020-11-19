import uuid

class Cliente():

	def __init__(self, nombre, saldo):
		self.saldo_apertura = saldo
		self.nombre = nombre
		self.saldo = saldo
		self.id_cliente = uuid.uuid4()

	def girar(self, giro):
		self.giro = giro
		if self.saldo > giro:
			self.saldo -= giro
			print('te informamos', self.nombre ,'que tu saldo es de:$', self.saldo)
		else:
			print(self.nombre ,'no puede efectuar la transacción')

	def abonar(self, abono):
		self.abono = abono
		self.saldo += abono
		print('te informamos', self.nombre ,'que tu saldo es de:$', self.saldo)

	def mostrar_saldo(self):
		print('Consulta de saldo:',self.nombre, 'tu saldo es de:$',self.saldo)