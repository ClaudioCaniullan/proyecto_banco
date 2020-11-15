
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

class Cliente():
        
    def __init__(self):
        self.nombre = self.nombre
        self.id_cliente = self.id_cliente
        self.saldo = self.saldo

    def girar(self):
        pass

    def abonar(self):
        pass

    def mostrar_saldo(self):
        pass


class Financiera():

    def __init__(self):
        self.nombre = self.nombre
        self.id_financiera = self.id_financiera
        self.saldo_institucional = self.saldo_institucional
        self.clientes = []

    def agregar_cliente(self): # verificar que se cumple condicion del 10 % sino rechazar
        pass

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

