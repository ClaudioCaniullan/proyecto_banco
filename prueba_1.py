
class Cliente:

	# inicializamos dos atributos de instancia
	def __init__(self, nombre, id, saldo):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo = saldo


	# métodos
	def girar(self, monto):
		self.saldo -=monto

	def abonar(self, abono):
		self.saldo +=abono

	def mostrar_saldo():

Cliente1 = Cliente('Sebastian', 179207575, 50000)
		