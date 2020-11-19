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
        self.saldo_credito = 1000000


    def girar(self, giro):
        if self.saldo >= giro:
            self.saldo -= giro
            print(self.saldo)
        else:
            print('no puede efectuar la transacción')

    def abonar(self, abonar):
        self.abonar = self.abonar
        self.saldo += abonar
        print(self.saldo)

    def mostrar_saldo(self):
        return self.saldo + self.saldo_credito



class Financiera():

    def __init__(self, nombre):
        self.nombre = nombre
        self.saldo_institucional = 100000000
        self.id_unico = uuid.uuid4()
        self.saldo_credito = 1000000
        self.clientes = []

    def agregar(self, cliente):
        tupla = (cliente.nombre, cliente.saldo + self.saldo_credito, cliente.id_cliente)
        self.saldo_institucional = self.saldo_institucional - self.saldo_credito
        self.clientes.append(tupla)
            

        print('cliente agregado', self.clientes)

    def eliminar(self):
        i = input('ingrese el indice en la lista que corresponde al cliente a eliminar: ')
        self.clientes.pop(i)
        print('el cliente ha sido eliminado', self.clientes)


    def tranferir(self):
        pass

    def giros_totales(self):
        pass

    def abonos_totales(self):
        clientes_abonos = []
        cliente_abonos =(cliente.abonar)
        cliente_abonos.append(clientes_abonos)
        return cliente_abonos
        pass

    def mostrar_saldo_institucional(self):
        return self.saldo_institucional

# se crea cleinte1 y se verifica sus datos

cliente1 = Cliente('juana', 60000)
cliente1.mostrar_saldo
cliente1.abonar(120000)
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
cliente2.mostrar_saldo
financiera1.agregar(cliente2)
print(financiera1.saldo_institucional)

# idem, cliente 3 
cliente3 = Cliente('Gato', 120000)
cliente3.mostrar_saldo
cliente3.abonar(70000)
financiera1.agregar(cliente3)
#print(financiera1.saldo_institucional)

cliente4 = Cliente('claudito', 0)
cliente4.mostrar_saldo
financiera1.agregar(cliente3)

cliente5 = Cliente('claudito', 70000)
cliente5.mostrar_saldo
financiera1.agregar(cliente3)

cliente6 = Cliente('claudito', 7000)
cliente6.mostrar_saldo
financiera1.agregar(cliente3)

cliente7 = Cliente('claudito', 12000)
cliente7.mostrar_saldo
financiera1.agregar(cliente3)

cliente8 = Cliente('claudito', 20000)
cliente8.mostrar_saldo
financiera1.agregar(cliente3)

cliente9 = Cliente('claudito', 701000)
cliente9.mostrar_saldo
financiera1.agregar(cliente3)

cliente10 = Cliente('claudito', 40000)
cliente10.mostrar_saldo
financiera1.agregar(cliente3)



print("saldo cliente:$ ", cliente1.mostrar_saldo())
print("saldo cliente:$ ", cliente2.mostrar_saldo())
print("saldo cliente:$ ", cliente3.mostrar_saldo())
print("saldo cliente:$ ", cliente5.mostrar_saldo())
print("saldo cliente:$ ", cliente6.mostrar_saldo())
print("saldo cliente:$ ", cliente7.mostrar_saldo())
print("saldo cliente:$ ", cliente8.mostrar_saldo())
print("saldo cliente:$ ", cliente9.mostrar_saldo())
print("saldo cliente:$ ", cliente10.mostrar_saldo())


print("Total de financiera:$ ", financiera1.mostrar_saldo_institucional())


