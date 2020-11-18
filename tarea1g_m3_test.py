class Cliente:

# inicializamos dos atributos de instancia
    def __init__(self, nombre, id_unico, saldo):
        self.nombre = nombre
        self.id_unico = id_unico
        self.saldo = saldo


	# métodos
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

# Clase Financiera

class Financiera:

	def __init__(self, nombre, id_unico, saldo_institucional, clientes):
		self.nombre = nombre
		self.id_unico = id_unico
		self.saldo_institucional = saldo_institucional
		self.clientes = clientes

	def agregar_cliente(self, ):
		pass

	def eliminar_cliente(self, ):
		pass

	def tranferir(self, ):
		pass

	def giros_totales(self, ):
		pass

	def abonos_totales(self, ):
		pass

	def mostrar_saldo_institucional(self, ):
		pass

		
clientes = []

cliente1 = Cliente('Walter', 1, 100000)
cliente2 = Cliente('Claudio', 2, 500000)
cliente3 = Cliente('Miguel', 3, 600000)
cliente4 = Cliente('Sebastian', 1, 700000)

print("Nombre cliente: ", cliente1.nombre, "Cliente Giro: ", cliente1.girar(20000), "Cliente Abono: ", cliente1.abonar(15000), "Mostrar Saldo: ", cliente1.saldo)
print("Nombre cliente: ", cliente2.nombre, "Cliente Giro: ", cliente2.girar(50000), "Cliente Abono: ", cliente2.abonar(20000), "Mostrar Saldo: ", cliente2.saldo)
print("Nombre cliente: ", cliente3.nombre, "Cliente Giro: ", cliente3.girar(25000), "Cliente Abono: ", cliente3.abonar(14000), "Mostrar Saldo: ", cliente3.saldo)
print("Nombre cliente: ", cliente4.nombre, "Cliente Giro: ", cliente4.girar(25000), "Cliente Abono: ", cliente4.abonar(20000), "Mostrar Saldo: ", cliente4.saldo)

clientes.append(cliente1)

Financiera1 = Financiera('Piraña', 1, 100000, clientes)



