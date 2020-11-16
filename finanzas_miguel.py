
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
        
    def __init__(self, nombre, id_cliente, saldo):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.saldo = saldo

    def girar(self):
        pass

    def abonar(self):
        pass

    def mostrar_saldo(self):
        pass

    def generador_id(self): # Generador id funcionando ok 
        self.id_cliente = uuid.uuid4()
        return self.id_cliente


class Financiera():

    def __init__(self, nombre, id_financiera, saldo_institucional, clientes):
        self.nombre = nombre
        self.id_financiera = id_financiera
        self.saldo_institucional = saldo_institucional
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

    def generador_id(self): # Generador id funcionando ok 
        self.id_financiera = uuid.uuid4()
        return self.id_financiera

if __name__ == "__main__":
    cliente_prueba = Cliente("cliente_prueba", "", 1000)
    print(cliente_prueba.generador_id())