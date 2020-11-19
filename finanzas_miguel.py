
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
        

    def __init__(self, nombre, saldo_cliente):
        self.datos_cliente = []
        self.nombre = nombre
        self.id_cliente = uuid.uuid4()
        self.saldo_cliente: saldo_cliente
        self.datos_cliente.append(nombre)
        self.datos_cliente.append(self.id_cliente)
        self.datos_cliente.append(saldo_cliente)
        #self.datos_cliente.append(self.saldo_total)
        
        

    def girar(self):
        pass

    def abonar(self):
        pass

    def mostrar_saldo(self):
        pass




class Financiera():
    
    total_saldo_clientes = 0
    

    def __init__(self, nombre):
        self.nombre = nombre
        self.id_financiera = uuid.uuid4()
        self.saldo_institucional = 100000000
        self.clientes = []
        
        
    def agregar_cliente(self, *lista): # verificar que se cumple condicion del 10 % sino rechazar
        #print(lista)
        
        self._10porc = self.saldo_institucional * 0.10
        self.total_clientes = 0
        self.saldo_cte = lista[0][2] # Saldo cliente
        self.total_saldo_clientes = self.total_saldo_clientes + self.saldo_cte
        
        # for elemento in lista[1]:
        #     cont = 0
        #     cont += elemento
        #     self.total_clientes = cont
        #     break
        
        if self.total_saldo_clientes <= self.saldo_institucional:
            print("Cliente OK")
            self.clientes.append(lista[0][0])
        else:
            print("Cliente rechazado")
        
        



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
pasa_todo = Financiera("Pasa Todo")
sin_niuno = Financiera("Sin niuno")

# Creando cliente (4 x Financiera)
cliente_a1 = Cliente("Seba", 10000000)
#print(cliente_a1.datos_cliente)
pasa_todo.agregar_cliente(cliente_a1.datos_cliente) # se agrega el cliente en lista de financiera


cliente_a2 = Cliente("Walter", 10000000)
pasa_todo.agregar_cliente(cliente_a2.datos_cliente) # se agrega el cliente en lista de financiera

cliente_a3 = Cliente("Claudio", 10000000)
pasa_todo.agregar_cliente(cliente_a3.datos_cliente) # se agrega el cliente en lista de financiera

cliente_a4 = Cliente("Miguel", 10000000)
pasa_todo.agregar_cliente(cliente_a4.datos_cliente) # se agrega el cliente en lista de financiera



cliente_b1 = Cliente("Jonathan", 10000000)
pasa_todo.agregar_cliente(cliente_b1.datos_cliente) # se agrega el cliente en lista de financiera

cliente_b2 = Cliente("Luis", 10000000)
pasa_todo.agregar_cliente(cliente_b2.datos_cliente) # se agrega el cliente en lista de financiera

cliente_b3 = Cliente("Gloria", 10000000)
pasa_todo.agregar_cliente(cliente_b3.datos_cliente) # se agrega el cliente en lista de financiera

cliente_b4 = Cliente("Vania", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera

cliente_b5 = Cliente("Gatita", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera

cliente_b6 = Cliente("Sofia", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera

cliente_b7 = Cliente("Renata", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera
cliente_b8 = Cliente("Renata", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera
cliente_b9 = Cliente("Renata", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera
cliente_b10 = Cliente("Renata", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera
cliente_b11 = Cliente("Renata", 10000000)
pasa_todo.agregar_cliente(cliente_b4.datos_cliente) # se agrega el cliente en lista de financiera

print(pasa_todo.total_saldo_clientes)