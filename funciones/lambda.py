# Lambda es una funcion peque;a y anonima que puede tener mchos argumentos pero una expresion.

#Sintaxis lambda argumentos > expresion.

# x = lambda a, b : a + b #La expresion es lo que se ejecuta y se devuelve como resultado de la funcion.

# print(x(2,3))

def miFuncion(n):
    return lambda a: a * n

duplicador = miFuncion(2)
triplicador = miFuncion(3)
quintuplicador = miFuncion(5)

print(duplicador(5)) # 10
print(triplicador(5)) # 15
print(quintuplicador(5)) # 25

