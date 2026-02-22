# Tuplas> Colecciones ordenadas e inmutables de elementos que permiten duplicados.
#                  0            1           2
tecnologias = ("Python", "JavaScriptt", "Java", "Python")

print(tecnologias)
print(tecnologias[1])

print(len(tecnologias))

print(type(tecnologias))

fruta =("Manzana",) 

print(type(fruta))

tupla = ("Python", 5, True)

print(tupla)
print(type(tupla))


#Desempaquetado de tuplas
x, y, z = tupla

print(x)
print(y)
print(z)

tupla1=(1, 2, 3)
tupla2=(4, 5, 6)
#Permite la duplicidad de los elementos
tupla3=tupla1 + tupla2

print(tupla3)

#Repetir tuplas con el operador de multiplicación
tupla = ("Python", 5, True)
print(tupla * 2)

for item in tupla:
    print(item)

print("----------------------")

#convertir tupla a lista para modificarla y luego volver a convertirla a tupla
tuplaAModificar = ("Python", "Java","Go")
listaComodin = list(tuplaAModificar)
print(listaComodin)
listaComodin.append("JavaScript")
tuplaAModificar = tuple(listaComodin)
#Casteo de lista a tupla para modificar la tupla original, ya que las tuplas son inmutables
print(tuplaAModificar)

