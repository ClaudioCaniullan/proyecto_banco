
import finanzas as cls

# 1.CREAR 2 FINANCIERAS
print("\n")
financiera1 = cls.Financiera('Piraña')
financiera2 = cls.Financiera('Money')
print('Creacion de financieras: ',
             financiera1.nombre ,
             ', ', financiera2.nombre, '\n' )


# 2.CREAR 4 CLIENTES POR FINANCIERA
print('Para cada financiera se crean 4 clientes:')
print()
print('● Financiera Piraña\n')
cliente1 = cls.Cliente('Juan', 0)
cliente2 = cls.Cliente('María', 20000)
cliente3 = cls.Cliente('Seba', 30000)
cliente4 = cls.Cliente('Claudio', 0)


financiera1.agregar(cliente1)
financiera1.agregar(cliente2)
financiera1.agregar(cliente3)
financiera1.agregar(cliente4)

print('\n● Financiera Money\n')
cliente5 = cls.Cliente('Marta', 60000)
cliente6 = cls.Cliente('Marcela', 100000)
cliente7 = cls.Cliente('Roberto', 15000)
cliente8 = cls.Cliente('Carlos', 12000)

financiera2.agregar(cliente5)
financiera2.agregar(cliente6)
financiera2.agregar(cliente7)
financiera2.agregar(cliente8)

input()


print("\n")

# 3.REALIZAR 3 OPERACIONES POR CADA CLIENTE DE DISTINTO TIPO GIROS, ABONOS (AGREGADO OK)
print('3 clientes realizan una transferencia\n')
financiera1.tranferir(cliente4, 10000, cliente2)
financiera2.tranferir(cliente3, 40000, cliente1)
financiera1.tranferir(cliente1, 600000, cliente2)
print("\n")
input()

# 4.RELIZAR GIROS EN DOS CLIENTES QUE DEMUESTREN QUE NO PUEDEN RETIRAR 10**6
print('REALIZAR GIROS PROHIBIDOS DE 1 MILLON CUANDO SE TIENE EL MISMO SALDO\n')
cliente1.mostrar_saldo()
cliente1.girar(10**6)
cliente4.mostrar_saldo()
cliente4.girar(10**6)

print("\n")
input()


# 5.RALIZAR 4 TRANSFERENCIAS ENTRE CLIENTES
print("Tranferencias entre clientes misma finaciera:\n")
financiera1.tranferir(cliente1, 60000, cliente2)
financiera1.tranferir(cliente3, 40000, cliente4)

financiera2.tranferir(cliente5, 80000, cliente6)
financiera2.tranferir(cliente7, 30000, cliente8)
print("\n")
input()

# 6. REALIZAR 2 TRANSFERENCIAS ENTRE CLIENTE Y FINANCIERA
#print('REALIZAR 2 TRANSFERENCIAS ENTRE CLIENTE Y FINANCIERA')
print("Tranferencias entre clientes distintas financieras:\n")
financiera1.tranferir(cliente1, 200000, cliente5)
financiera2.tranferir(cliente8, 70000, cliente2)
print("\n")
input()

# 7.REALIZAR 2 OPERACIONES EN CADA FINANCIERA QUE DEMUESTREN QUE EL CLIENTE
# NO PUEDE QUEDAR CON SALDO MENOR A -10**6
print('REALIZAR 2 OPERACIONES EN CADA FINANCIERA QUE DEMUESTREN QUE EL CLIENTE NO PUEDE QUEDAR CON SALDO MENOR A -10**6\n')
cliente4.girar(20**6)
cliente5.girar(20**6)
input()

# 8. REALIZAR DOS OPERACIONES QUE DEMUESTREN QUE SE RECHAZAN TRANSFERENCIAS POR VIOLAR EL LIMITE DEL 10%
print('REALIZAR DOS OPERACIONES QUE DEMUESTREN QUE SE RECHAZAN TRANSFERENCIAS POR VIOLAR EL LIMITE DEL 10%')
financiera1.tranferir(cliente1, 1000001, cliente2)
financiera2.tranferir(cliente5, 1020000, cliente7)
print("\n")
input()

# 9.DEMOSTRAR QUE NO SE PUEDEN AGREGAR CLIENTES CUANDO SE VIOLA EL LIMITE DEL 10%
print('DEMOSTRAR QUE NO SE PUEDEN AGREGAR CLIENTES CUANDO SE VIOLA EL LIMITE DEL 10%\n')

cliente9 = cls.Cliente('Juan', 17000)
cliente10 = cls.Cliente('Andres', 0)
cliente11 = cls.Cliente('Renata', 36000)
cliente12 = cls.Cliente('Francisca', 36000)
cliente13 = cls.Cliente('Juan', 17000)
cliente14 = cls.Cliente('Andres', 0)
cliente15 = cls.Cliente('Renata', 36000)

financiera1.agregar(cliente9)
financiera1.agregar(cliente10)
financiera1.agregar(cliente11)
financiera1.agregar(cliente12)
financiera1.agregar(cliente13)
financiera1.agregar(cliente14)
financiera1.agregar(cliente15)

print("\n")
input()

# 10.IMPRIMA ESTADO DE CUENTA DE CADA CLIENTE Y LAS FINANCIERAS
# estado de cuenta de cada cliente
print("Estado de clientes: ") 
cliente1.mostrar_saldo()
cliente2.mostrar_saldo()
cliente3.mostrar_saldo()
cliente4.mostrar_saldo()
print("Estado financiero: ")
financiera1.mostrar_saldo_institucional()

#finaciera dos 
print("Estado de clientes: ")
cliente5.mostrar_saldo()
cliente6.mostrar_saldo()
cliente7.mostrar_saldo()
cliente8.mostrar_saldo()
print("Estado financiero: ")
financiera2.mostrar_saldo_institucional()
