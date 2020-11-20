import uuid
import time


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
            print('Se ha agregado el siguiente cliente: ', cliente.nombre)
            cliente.abonar(10**6)
            time.sleep(0.5)
        else:
            print(cliente.nombre, "No puedes ingresar a Financiera. Límite 10%\n")

    def eliminar(self):
        i = input('ingrese el indice en la lista que corresponde al cliente a eliminar: ')
        self.clientes.pop(i)
        print('el cliente ha sido eliminado', self.clientes)


    def tranferir(self, cliente1, monto, cliente2):

        if monto < 10**6:
            print(cliente1.nombre, 'tranfiere el monto de: $', monto, 'a', cliente2.nombre)
            cliente1.girar(monto)
            cliente2.abonar(monto)
            time.sleep(0.5)
        else:
            print(cliente1.nombre, "No puedes transferir el monto de", monto, "a", cliente2.nombre, "porque tu saldo actual es de ", cliente1.saldo)


    def giros_totales(self, cliente):
        self.girosT.append(cliente.giro)
        print('Los giros totales son:$', self.girosT)

    def abonos_totales(self, cliente):	
        self.abonosT.append(cliente.abono)
        print('Los abonos totales son:$', self.abonosT)

    def mostrar_saldo_institucional(self):
        n = 0
        while n < len(self.clientes):
            self.saldo_institucional += self.clientes[n][1] - 10**6
            n += 1
        print("Saldo acumulado de la financiera:$", self.saldo_institucional, "\n")
