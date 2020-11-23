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
		if 10000000 > self.saldo > giro:
			self.saldo -= giro
			print('te informamos', self.nombre ,'que tu saldo es de:$', self.saldo)
		else:
			print(self.nombre ,'no puede efectuar la transacción')

	def abonar(self, abono):
		self.abono = abono
		self.saldo += abono
		print('te informamos', self.nombre ,'que tu saldo es de:$ ', self.saldo)

	def mostrar_saldo(self):
		print('Consulta de saldo:',self.nombre, 'tu saldo es de:$ ',self.saldo)




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
		print(cliente1.nombre, 'tranfiere el monto de:$', monto, 'a', cliente2.nombre)
		is self.monto > 10000000:
		    cliente1.girar(monto)
		    cliente2.abonar(monto)
		else:
			print("Rechazada la transacción")
		

	def giros_totales(self, cliente):
		self.girosT.append(cliente.giro)
		print('Los giros totales son:', self.girosT)

	def abonos_totales(self, cliente):	
		self.abonosT.append(cliente.abono)
		print('Los abonos totales son:', self.abonosT)

	def mostrar_saldo_institucional(self):
		n = 0
		while n < len(self.clientes):
			self.saldo_institucional += self.clientes[n][1] - 10**6
			n += 1
		print("Saldo acumulado de la financiera: ", self.saldo_institucional)

# 1.CREAR 2 FINANCIERAS
financiera1 = Financiera('Piraña')
financiera2 = Financiera('Money')
print('Se han creado las financieras', financiera1.nombre ,'y', financiera2.nombre)

# 2.CREAR 4 CLIENTES POR FINANCIERA

print('AGREGAMOS 4 CLIENTES A FINANCIERA PIRAÑA')
cliente1 = Cliente('Juan', 0)
cliente2 = Cliente('María', 20000)
cliente3 = Cliente('Seba', 30000)
cliente4 = Cliente('Claudio', 40000)

financiera1.agregar(cliente1)
financiera1.agregar(cliente2)
financiera1.agregar(cliente3)
financiera1.agregar(cliente4)

print('AGREGAMOS 4 CLIENTES A FINANCIERA MONEY')
cliente5 = Cliente('Pedro', 0)
cliente6 = Cliente('Miguel', 60000)
cliente7 = Cliente('Walter', 70000)
cliente8 = Cliente('Francisca', 80000)

financiera2.agregar(cliente5)
financiera2.agregar(cliente6)
financiera2.agregar(cliente7)
financiera2.agregar(cliente8)

# 3.REALIZAR 3 OPERACIONES POR CADA CLIENTE DE DISTINTO TIPO GIROS, ABONOS
print('RELIZAR 3 OPERACIONES POR CADA CLIENTE')


# 4.RELIZAR GIROS EN DOS CLIENTES QUE DEMUESTREN QUE NO PUEDEN RETIRAR 10**6
print('REALIZAR GIROS PROHIBIDOS DE 1 MILLON CUANDO SE TIENE EL MISMO SALDO')
cliente1.girar(10**6)
cliente5.girar(10**6)

# 5.RALIZAR 4 TRANSFERENCIAS ENTRE CLIENTES
print('RALIZAR 4 TRANSFERENCIAS ENTRE CLIENTES')
financiera1.tranferir(cliente1, 50000, cliente2)
financiera1.tranferir(cliente3, 50000, cliente4)

financiera2.tranferir(cliente5, 50000, cliente6)
financiera2.tranferir(cliente7, 50000, cliente8)

# 6. REALIZAR 2 TRANSFERENCIAS ENTRE CLIENTE Y FINANCIERA
print('REALIZAR 2 TRANSFERENCIAS ENTRE CLIENTE Y FINANCIERA')


# 7.REALIZAR 2 OPERACIONES EN CADA FINANCIERA QUE DEMUESTREN QUE EL CLIENTE
# NO PUEDE QUEDAR CON SALDO MENOR A -10**6
print('REALIZAR 2 OPERACIONES EN CADA FINANCIERA QUE DEMUESTREN QUE EL CLIENTE NO PUEDE QUEDAR CON SALDO MENOR A -10**6')

# 8. REALIZAR DOS OPERACIONES QUE DEMUESTREN QUE SE RECHAZAN TRANSFERENCIAS POR VIOLAR EL LIMITE DEL 10%
print('REALIZAR DOS OPERACIONES QUE DEMUESTREN QUE SE RECHAZAN TRANSFERENCIAS POR VIOLAR EL LIMITE DEL 10%')

# 9.DEMOSTRAR QUE NO SE PUEDEN AGREGAR CLIENTES CUANDO SE VIOLA EL LIMITE DEL 10%
print('DEMOSTRAR QUE NO SE PUEDEN AGREGAR CLIENTES CUANDO SE VIOLA EL LIMITE DEL 10%')
# 10.IMPRIMA ESTADO DE CUENTA DE CADA CLIENTE Y LAS FINANCIERAS
print('IMPRIMA ESTADO DE CUENTA DE CADA CLIENTE Y LAS FINANCIERAS')

