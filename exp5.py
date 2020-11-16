## En este ejemplo se entiende que el monto maximo destinada para creditos
## corresponde al 10% del saldo institucional de 100 millones , osea, 10 millones en total para
## repartir en creditos, si el monto maximo que puede recibir cada cliente es de 1 millon
## entonces a lo mas la financiera puede otorgar 10 creditos de 1 millon

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
			print("No se puede efectuar la transacción")

	def abonar(self, abonar):
		self.saldo += abonar
		print(self.saldo)

	def mostrar_saldo(self):
		return self.saldo


class Financiera():

	def __init__(self, nombre):
		self.nombre = nombre
		self.saldo_institucional = 100000000
		self.id_unico = uuid.uuid4()
		self.clientes = []

	def agregar(self, cliente):
		tupla = (cliente.nombre, cliente.saldo + 10**6, cliente.id_cliente)
		self.saldo_institucional = self.saldo_institucional - 10**6
		self.clientes.append(tupla)

		print('cliente agregado', self.clientes)

	def eliminar(self):
		i = int(input('ingrese el indice en la lista que corresponde al cliente a eliminar: '))
		self.clientes.pop(i)
		print('el cliente ha sido eliminado', self.clientes)


	def tranferir(self):

		c1 = self.clientes[0][1]
		print(c1)
		


	def giros_totales(self):
		pass

	def abonos_totales(self):
		pass

	def mostrar_saldo_institucional(self):
		print('El saldo institucional a la fecha es de :', self.saldo_institucional)

# se crea cleinte1 y se verifica sus datos  
cliente1 = Cliente('juana', 60000)
l1 = [cliente1.nombre, cliente1.saldo, cliente1.id_cliente]
print(l1)


# crear financiera y se verifican sus datos 
financiera1 = Financiera('piraña')
l2 = [financiera1.nombre, financiera1.saldo_institucional, financiera1.id_unico, financiera1.clientes ]
print(l2)

# se agrega cliente1
financiera1.agregar(cliente1)
print(financiera1.saldo_institucional)


# se crea cliente 2 y se agrega, observar que el saldo de la financiera disminuye en 2 millones
cliente2 = Cliente('Carlos', 0)
financiera1.agregar(cliente2)
print(financiera1.saldo_institucional)

# idem, cliente 3 
cliente3 = Cliente('Gato', 120000)
financiera1.agregar(cliente3)
print(financiera1.saldo_institucional)

financiera1.tranferir()


input()

		