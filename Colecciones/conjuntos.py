frutas ={"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))
print(len(frutas))

print("Manzana" in frutas) # Verifica si un elemento esta presente en un conjunto
print("Pera" not in frutas) # verifica si un elemento no esta presente en un conjunto

#Agregar elementos a un conjunto
#Add
frutas.add("Pera")
print(frutas)

#Update
frutasTropicales = {"Piña", "Mango", "Papaya"}
frutas.update(frutasTropicales) # Agregar listas, tuplas o conjuntos a un conjunto.
print(frutas)

#Eliminar elementos a un conjunto
#remove
frutas.remove("Mango")
print(frutas)

#discard
#La diferencia entre remove y discard es que remove genera un error si el elementos no existe en el conjunto.
frutas.discard("Piña")
print(frutas)

#Pop
#Elimina un elemento aleatorio del conjunto y lo devueelve. Si el conjunto esta vacio, genera un error.
frutas.pop()
print(frutas)

#Clear
#Elimina todos los elementos del conjunto, dejando el conjunto vacio.
frutas.clear()
print(frutas)


# conjuntos = {"Python", 254, True}
# print(conjuntos)
# print(type(conjuntos))

# for item in conjuntos:
#     print(item)

print("----------------------")

#Operaciones con conjuntos con la funcion union
a ={"a", "b", "c"}
b ={"c", "d", "e"}

c= a.union(b) # Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos, sin duplicados.
print(c)

i = a.intersection(b) # Devuelve un nuevo conjunto con los elementos comunes a ambos conjuntos.
print(i)

d = a.difference(b) # Devuelve un nuevo conjunto con los elementos que estan en el primer conjunto pero no en el segundo.
print(d)











