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
			print('Despues de Girar: te informamos', self.nombre ,'que tu saldo es de', self.saldo)
		else:
			print('no puede efectuar la transacción')

	def abonar(self, abonar):
		self.saldo += abonar
		print('Despues de Abonar: te informamos', self.nombre ,'que tu saldo es de', self.saldo)

	def mostrar_saldo(self):
		print('Consulta de saldo:',self.nombre, 'tu saldo es de',self.saldo)




class Financiera():

	def __init__(self, nombre):
		self.nombre = nombre
		self.saldo_institucional = 100000000
		self.id_unico = uuid.uuid4()
		self.clientes = []

	def agregar(self, cliente):
		tupla = (cliente.nombre, cliente.saldo + 10**6)
		self.saldo_institucional = self.saldo_institucional - 10**6
		self.clientes.append(tupla)
		print('Financiera: Se ha agregado el siguiente cliente', self.clientes)
		cliente.abonar(10**6)

	def eliminar(self):
		i = input('ingrese el indice en la lista que corresponde al cliente a eliminar: ')
		self.clientes.pop(i)
		print('el cliente ha sido eliminado', self.clientes)


	def tranferir(self, cliente1, monto, cliente2):
		cliente1.girar(monto)
		cliente2.abonar(monto)
		

	def giros_totales(self):
		pass

	def abonos_totales(self):
		pass

	def mostrar_saldo_institucional(self):
		pass

# crear clientes
cliente1 = Cliente('juana', 60000)
cliente2 = Cliente('Carlos', 0)

# crear financiera 
financiera1 = Financiera('piraña')

# agregar clientes
financiera1.agregar(cliente1)
financiera1.agregar(cliente2)

#cliente1.mostrar_saldo()

# realizar transferencia
financiera1.tranferir(cliente1, 10000, cliente2)

#revisar saldos de clientes
cliente1.mostrar_saldo()
cliente2.mostrar_saldo()


# dos forma de invocar a un metedo de cliente1
#cliente1.mostrar_saldo()
#Cliente.mostrar_saldo(cliente1)


input()

		