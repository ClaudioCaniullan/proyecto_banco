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
		self.giro = giro
		if self.saldo >= giro:
			self.saldo -= giro
			print('te informamos', self.nombre ,'que tu saldo es de', self.saldo)
		else:
			print('no puede efectuar la transacción')

	def abonar(self, abono):
		self.abono = abono
		self.saldo += abono
		print('te informamos', self.nombre ,'que tu saldo es de', self.saldo)

	def mostrar_saldo(self):
		print('Consulta de saldo:',self.nombre, 'tu saldo es de',self.saldo)




class Financiera():

	def __init__(self, nombre):
		self.nombre = nombre
		self.saldo_institucional = 100000000
		self.id_unico = uuid.uuid4()
		self.clientes = []
		self.abonosT = []
		self.girosT = []

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
		print(cliente1.nombre, 'tranfiere el monto de', monto, 'a', cliente2.nombre)
		cliente1.girar(monto)
		cliente2.abonar(monto)
		

	def giros_totales(self, cliente):
		self.girosT.append(cliente.giro)
		print('Los giros totales son:', self.girosT)

	def abonos_totales(self, cliente):	
		self.abonosT.append(cliente.abono)
		print('Los abonos totales son:', self.abonosT)

	def mostrar_saldo_institucional(self):
		pass

# crear clientes
cliente1 = Cliente('juana', 60000)
cliente2 = Cliente('Carlos', 0)
cliente3 = Cliente('Pepe', 500000)

# crear financiera 
financiera1 = Financiera('piraña')

# agregar clientes
print('SE AGREGAN CLIENTES A FINANCIERA')
financiera1.agregar(cliente1)
financiera1.agregar(cliente2)
financiera1.agregar(cliente3)

#cliente1.mostrar_saldo()

# realizar transferencia
print('SE REALIZA TRANSFERENCIA')
financiera1.tranferir(cliente1, 10000, cliente2)
financiera1.tranferir(cliente2, 40000, cliente3)

#revisar saldos de clientes
print('SE REVISAN SALDO DE CLIENTE')
cliente1.mostrar_saldo()
cliente1.girar(45)
cliente2.mostrar_saldo()


# revisar abonos totales
print('REVISANDO ABONOS TOTALES')
financiera1.abonos_totales(cliente1)
cliente1.abonar(1234)
financiera1.abonos_totales(cliente1)


# revisar girtos totales
print('REVISANDO GIROS TOTALES')
financiera1.giros_totales(cliente1)
cliente2.girar(1250)
financiera1.giros_totales(cliente2)
cliente3.girar(150000)
financiera1.giros_totales(cliente3)

# dos forma de invocar a un metedo de cliente1
#cliente1.mostrar_saldo()
#Cliente.mostrar_saldo(cliente1)


input()

		