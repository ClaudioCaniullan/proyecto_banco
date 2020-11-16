## En este ejemplo se entiende que el monto maximo que se puede asignar a una linea de 
## credito no sera superior al 10% del monto institucional de 100 milloines, osea, un credito
# personal no exedera los 10 millones 



# el codigo se debe modificar para satisfacer la condicion de arriba 

import uuid

class Cliente():

	def __init__(self, nombre, saldo):
		self.nombre = nombre
		self.saldo = saldo
		self.id_cliente = uuid.uuid4()


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
		i = input('ingrese el indice en la lista del cliente a eliminar: ')
		self.clientes.pop(i)
		print('el cliente ha sido eliminado', self.clientes)


	def tranferir(self):
		pass

	def giros_totales(self):
		pass

	def abonos_totales(self):
		pass

	def mostrar_saldo_institucional(self):
		pass

# info del cliente creado 
cliente1 = Cliente('juana', 60000)
l1 = [cliente1.nombre, cliente1.saldo, cliente1.id_cliente]
print(l1)


# crear financiera y agregar cliente 

financiera1 = Financiera('piraña')
l2 = [financiera1.nombre, financiera1.saldo_institucional, financiera1.id_unico, financiera1.clientes ]
print(l2)

# se agrega cliente1
financiera1.agregar(cliente1)
print(financiera1.saldo_institucional)


cliente2 = Cliente('Carlos', 0)
financiera1.agregar(cliente2)
print(financiera1.saldo_institucional)

input()