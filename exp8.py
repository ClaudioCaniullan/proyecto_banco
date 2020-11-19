## En este ejemplo se entiende que el monto maximo destinada para creditos
## corresponde al 10% del saldo institucional de 100 millones , osea, 10 millones en total para
## repartir en creditos, si el monto maximo que puede recibir cada cliente es de 1 millon
## entonces a lo mas la financiera puede otorgar 10 creditos de 1 millon

import uuid

class Cliente():

	def __init__(self, nombre, saldo):
		self.saldo_apertura = saldo
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
		self.total_clientes = len(self.clientes)
		if self.total_clientes < 10:
			tupla = (cliente.nombre, cliente.saldo + 10**6)
			self.saldo_institucional = self.saldo_institucional - 10**6
			self.clientes.append(tupla)
			print('Financiera: Se ha agregado el siguiente cliente', self.clientes)
			cliente.abonar(10**6)
		else:
			print("No se puede agregar cliente")

	def eliminar(self):
		i = input('ingrese el indice en la lista que corresponde al cliente a eliminar: ')
		self.clientes.pop(i)
		print('el cliente ha sido eliminado', self.clientes)


	def tranferir(self, cliente1, monto, cliente2):
		print(cliente1.nombre, 'tranfiere el monto de', monto, 'a', cliente2.nombre)
		cliente1.girar(monto)
		cliente2.abonar(monto)
		

	def giros_totales(self, cliente):
<<<<<<< HEAD
		
		self.girosT.append(cliente.giro)
		print('Tus giros totales son:', self.girosT)

	def abonos_totales(self, cliente):
		self.abono = + 1
		self.abonosT.append(cliente.abono)
		print('Tus abonos totales son:', self.abonosT)
		return self.abono
=======
		self.girosT.append(cliente.giro)
		print('Los giros totales son:', self.girosT)

	def abonos_totales(self, cliente):	
		self.abonosT.append(cliente.abono)
		print('Los abonos totales son:', self.abonosT)
>>>>>>> 68879d1994addf0ed51346091c07a29f32cb8098

	def mostrar_saldo_institucional(self):
		n = 0
		while n < len(self.clientes):
			self.saldo_institucional += self.clientes[n][1] - 10**6
			n += 1
		print("Saldo acumulado de la financiera: ", self.saldo_institucional)

# crear clientes
cliente1 = Cliente('juana', 60000)
cliente2 = Cliente('Carlos', 0)
cliente3 = Cliente('Pepe', 0)
cliente4 = Cliente('Pepe1', 0)
cliente5 = Cliente('Pepe2', 0)
cliente6 = Cliente('Pepe3', 0)
cliente7 = Cliente('Pepe4', 0)
cliente8 = Cliente('Pepe5', 0)
cliente9 = Cliente('Pepe6', 0)
cliente10 = Cliente('Pepe7', 0)
cliente11 = Cliente('Pepe8', 0)
cliente12 = Cliente('Pepe9', 0)

# crear financiera 
financiera1 = Financiera('piraña')

# agregar clientes
print('SE AGREGAN CLIENTES A FINANCIERA')
financiera1.agregar(cliente1)
financiera1.agregar(cliente2)
financiera1.agregar(cliente3)
financiera1.agregar(cliente4)
financiera1.agregar(cliente5)
financiera1.agregar(cliente6)
financiera1.agregar(cliente7)
financiera1.agregar(cliente8)
financiera1.agregar(cliente9)
financiera1.agregar(cliente10)
financiera1.agregar(cliente11)
financiera1.agregar(cliente12)



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
cliente2.girar(2544)


# revisar abonos totales
print('REVISANDO ABONOS TOTALES')
financiera1.abonos_totales(cliente1)
cliente1.abonar(1234)
financiera1.abonos_totales(cliente1)
cliente2.abonar(4654)
financiera1.abonos_totales(cliente2)


# revisar girtos totales
print('REVISANDO GIROS TOTALES')
financiera1.giros_totales(cliente1)
<<<<<<< HEAD
=======
cliente2.girar(1250)
financiera1.giros_totales(cliente2)
cliente3.girar(150000)
financiera1.giros_totales(cliente3)

>>>>>>> 68879d1994addf0ed51346091c07a29f32cb8098
# dos forma de invocar a un metedo de cliente1
#cliente1.mostrar_saldo()
#Cliente.mostrar_saldo(cliente1)

financiera1.mostrar_saldo_institucional()
input()

		