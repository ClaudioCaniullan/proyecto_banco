
import classes as cls

# 1.CREAR 2 FINANCIERAS
financiera1 = cls.Financiera('Piraña')
financiera2 = cls.Financiera('Money')
print('Se han creado las financieras', financiera1.nombre ,'y', financiera2.nombre)

# 2.CREAR 4 CLIENTES POR FINANCIERA

print('AGREGAMOS 4 CLIENTES A FINANCIERA PIRAÑA')
cliente1 = cls.Cliente('Juan', 0)
cliente2 = cls.Cliente('María', 20000)
cliente3 = cls.Cliente('Seba', 30000)
cliente4 = cls.Cliente('Claudio', 40000)

financiera1.agregar(cliente1)
financiera1.agregar(cliente2)
financiera1.agregar(cliente3)
financiera1.agregar(cliente4)

print('AGREGAMOS 4 CLIENTES A FINANCIERA MONEY')
cliente5 = cls.Cliente('Pedro', 0)
cliente6 = cls.Cliente('Miguel', 60000)
cliente7 = cls.Cliente('Walter', 70000)
cliente8 = cls.Cliente('Francisca', 80000)

financiera2.agregar(cliente5)
financiera2.agregar(cliente6)
financiera2.agregar(cliente7)
financiera2.agregar(cliente8)

# 3.REALIZAR 3 OPERACIONES POR CADA CLIENTE DE DISTINTO TIPO GIROS, ABONOS
print('RELIZAR 3 OPERACIONES POR CADA CLIENTE')


# 4.RELIZAR GIROS EN DOS CLIENTES QUE DEMUESTREN QUE NO PUEDEN RETIRAR 10**6
print('REALIZAR GIROS PROHIBIDOS DE 1 MILLON CUANDO SE TIENE EL MISMO SALDO')
cliente1.girar(10**6)
cliente5.girar(10**6)

# 5.RALIZAR 4 TRANSFERENCIAS ENTRE CLIENTES
print('RALIZAR 4 TRANSFERENCIAS ENTRE CLIENTES')
financiera1.tranferir(cliente1, 50000, cliente2)
financiera1.tranferir(cliente3, 50000, cliente4)

financiera2.tranferir(cliente5, 50000, cliente6)
financiera2.tranferir(cliente7, 50000, cliente8)

# 6. REALIZAR 2 TRANSFERENCIAS ENTRE CLIENTE Y FINANCIERA
print('REALIZAR 2 TRANSFERENCIAS ENTRE CLIENTE Y FINANCIERA')


# 7.REALIZAR 2 OPERACIONES EN CADA FINANCIERA QUE DEMUESTREN QUE EL CLIENTE
# NO PUEDE QUEDAR CON SALDO MENOR A -10**6
print('REALIZAR 2 OPERACIONES EN CADA FINANCIERA QUE DEMUESTREN QUE EL CLIENTE NO PUEDE QUEDAR CON SALDO MENOR A -10**6')

# 8. REALIZAR DOS OPERACIONES QUE DEMUESTREN QUE SE RECHAZAN TRANSFERENCIAS POR VIOLAR EL LIMITE DEL 10%
print('REALIZAR DOS OPERACIONES QUE DEMUESTREN QUE SE RECHAZAN TRANSFERENCIAS POR VIOLAR EL LIMITE DEL 10%')

# 9.DEMOSTRAR QUE NO SE PUEDEN AGREGAR CLIENTES CUANDO SE VIOLA EL LIMITE DEL 10%
print('DEMOSTRAR QUE NO SE PUEDEN AGREGAR CLIENTES CUANDO SE VIOLA EL LIMITE DEL 10%')
# 10.IMPRIMA ESTADO DE CUENTA DE CADA CLIENTE Y LAS FINANCIERAS
print('IMPRIMA ESTADO DE CUENTA DE CADA CLIENTE Y LAS FINANCIERAS')

