

# clase Cliente 

class Cliente:

	# inicializamos dos atributos de instancia
	def __init__(self, nombre, id, saldo):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo = saldo


	# métodos
	def girar(self, monto):
		pass

	def abonar(self, monto):
		pass

	def mostrar_saldo(self):
		pass



# Clase Financiera

class Financiera:

	lista_clientes = []

	def __init__(self, nombre, id_unico, saldo_institucional, clientes):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo_institucional = saldo_institucional
		self.clientes = clientes

    # claudio, revisar script
	def agregar_cliente(self, cliente):
		clientes.append(cliente)
		print('cliente agregado')
    
    # claudio, revisar script
	def eliminar_cliente(self, cliente):
		clientes.remove(cliente)
		print('cliente eliminado')

	def tranferir(self):
		pass

	def giros_totales(self):
		pass

	def abonos_totales(self):
		pass

	def mostrar_saldo_institucional(self):
		pass


	
cl = Cliente('Ale', 1, 1)

#cliente1 = Cliente('perro', '1', '2')
#cliente2 = Cliente('perra', 2, 2000000)


#Financiera1 = Financiera('Piraña', 1, 100000, clientes)


print('hola')
input()

