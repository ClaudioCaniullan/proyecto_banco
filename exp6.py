import uuid

class Cliente():

	def __init__(self, nombre, saldo):
		self.nombre = nombre
		self.saldo = saldo
		self.id_cliente = uuid.uuid4()
    
    # métodos para acceder y modificar nombre cliente
	@property
	def nombre_cliente(self):
		return self.nombre

	@nombre_cliente.setter
	def nombre_cliente(self, nombre):
		self.nombre = nombre

	
class Financiera():

	def __init__(self, nombre):
		self.nombre = nombre
		self.saldo_institucional = 10**8
		self.id_unico = uuid.uuid4()
		self.clientes = []

	@property
	def nombre_financiera(self):
		return self.nombre

	@nombre_financiera.setter
	def nombre_financiera(self, nombre):
		self.nombre = nombre



	


# se crea cliente y se imprime nombre
cliente1 = Cliente('Pedro', 1)
print(cliente1.nombre_cliente)

# se reingresa otro nombre para cliente 1
cliente1.nombre_cliente = 'juan'
print(cliente1.nombre_cliente)

# se crea financiera1 y se imprime nombre
financiera1 = Financiera('piraña')
print(financiera1.nombre_financiera)

# se reingresa otro nombre para financiera1
financiera1.nombre_financiera = 'delano'
print(financiera1.nombre_financiera)

print('hola')
input()

		
