
import uuid
# uuid4 genera valores aleatorios
'''
for i in range(3):
    print(uuid.uuid4())
'''
#######################################################################################################################
# Crear mecánica para líneas de crédito (Línea de crédito con saldo negativo)
# Cubierto por el saldo instutucional = 1000000 (1 millón por persona)
# limite max de lineas de credito <= saldo institucional * 0.10
# limitar cantidad max de clientes y monto disponible para transferencias desde saldo_institucional
# 


#------------> HACER: transferir y giros totales <------------#


class Cliente():
        

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.id_cliente = uuid.uuid4()
        self.saldo = saldo
        self.datos_cliente = []
        self.datos_cliente.append(nombre)
        self.datos_cliente.append(self.id_cliente)
        self.datos_cliente.append(saldo)

    def girar(self):
        pass

    def abonar(self):
        pass

    def mostrar_saldo(self):
        pass




class Financiera():

    base_clientes: {}
    total_clientes = 0

    def __init__(self, nombre, id_financiera, saldo_institucional):
        self.nombre = nombre
        self.id_financiera = uuid.uuid4()
        self.saldo_institucional = saldo_institucional
        self.clientes = []
        
    def agregar_cliente(self, *lista): # verificar que se cumple condicion del 10 % sino rechazar
        self.datos_cliente= lista # guarda informacion cliente   
        self.linea_credito = 1000000  # por un cliente
        self.lim_max_cred = self.saldo_institucional * 0.10 # se establece max de linea de credito
        self.acceso_credito = 0


    def eliminar_cliente(self):
        pass

        # debe permitir transferencias entre la financiera y el banco
    def transferir(self): # verificar saldo_institucional 10% segun cantidad de clientes actuales sino rechazar
        pass

    def giros_totales(self):
        pass

    def abonos_totales(self):
        pass

    def mostrar_saldo_institucional(self):
        pass




# Creando financieras
pasa_todo = Financiera("Pasa Todo", "", 100000000)
sin_niuno = Financiera("Sin niuno", "", 100000000)

# Creando cliente (4 x Financiera)
cliente_a1 = Cliente("Seba", 1000000)
pasa_todo.agregar_cliente(cliente_a1.datos_cliente) # se agrega el cliente en lista de financiera

cliente_a2 = Cliente("Walter", 1000000)
cliente_a3 = Cliente("Claudio", 1000000)
cliente_a4 = Cliente("Miguel", 1000000)

cliente_b1 = Cliente("Jonathan", 1000000)
cliente_b2 = Cliente("Luis", 1000000)
cliente_b3 = Cliente("Gloria", 1000000)
cliente_b4 = Cliente("Vania", 1000000)







if __name__ == "__main__":
    pass
