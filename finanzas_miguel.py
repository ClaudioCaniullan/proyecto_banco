
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
    
    def info_cliente(self):
        self.info_lista = []


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
        
        for _cliente in self.clientes: # Indica cantidad de cliente en la financiera
            contador = 0
            contador += 1
            _total_clientes = contador
        

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

    def generador_id(self): # Generador id funcionando ok 
        self.id_financiera = uuid.uuid4()
        return self.id_financiera


# Creando financieras
pasa_todo = Financiera("Pasa Todo", "", 100000000, "")
sin_niuno = Financiera("Sin niuno", "", 100000000, "")

# Creando cliente (4 x Financiera)
cliente_a1 = Cliente("Seba", "", 1000000)
cliente_a2 = Cliente("Walter", "", 1000000)
cliente_a3 = Cliente("Claudio", "", 1000000)
cliente_a4 = Cliente("Miguel", "", 1000000)

cliente_b1 = Cliente("Jonathan", "", 1000000)
cliente_b2 = Cliente("Luis", "", 1000000)
cliente_b3 = Cliente("Gloria", "", 1000000)
cliente_b4 = Cliente("Vania", "", 1000000)




print("Numero de clientes en financiera: ", pasa_todo.clientes)
print(Cliente.__init__)












if __name__ == "__main__":
    cliente_prueba = Cliente("cliente_prueba", "", 1000)
    print(cliente_prueba.generador_id())