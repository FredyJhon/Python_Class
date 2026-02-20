# #Listas: Las listas son ordenadas, modificables y permiten valores duplicados

# # indices :   0         1           2        3
# frutas = ["Manzana", "Naranja", "Mango", "Naranja"]
# # Las listas son organizadas y  cada una tiene su posición
# print(frutas)
# print(type(frutas))

# frutas[1] = "Banana"
# #Son modificables y permiten duplicados

# print(frutas[1])
# print(frutas)

# #Permiten tener dentro de las listas varios tipos de datos por ejemplo
# #int, str, float
# listas=["John", 12, "Aroca", 12.5]
# print(listas)

# #se usa la función print, se selecciona la lista del elementos que vamos a imprimir
# #y enseguida le ponemos entre corchetes el numero del elemento a llamar.
# print(listas[3])

# #Se usa los : para indicar hasta que posición se debe de imprimir
# #en este caso imprimiria la posición 0 y 1 no imprime el 2 porque no es inclusive.
# print(frutas[0:2])

# #En este ejemplo usamos el if para identificar si tenemos un elemento dentro de una lista
# #Si el elemento es verdadero la instrucción if va a ser que se imprima el mensaje.
# if "Manzana" in frutas:
#         print("La manzana esta dentro de las frutas")

# #Con el atajo Ctrl + } y seleccionando todo el bloque de codigo que quieren comentar los puedes hacer mas rapido
# #Al usar este atajo de las teclas rapidas.

#               0       1       2
vehiculos = ["auto", "Moto", "Avión"]

#Metodos
#Append (agregar un elemento a una lista)
vehiculos.append("Barco") #Indice 3 ya que esta agregado a la lista
print(vehiculos)

#insert este metodo nos sirve para insertar un elemento pero en la posición que queremos que este.
vehiculos.insert(1, "Bicicleta")
print(vehiculos)

#Remove quita un elemento de una lista por su valor y toma el primer elemento que coincida.
vehiculos.remove("auto")
print(vehiculos)

#Pop quita un elemento por su indice (posición)
vehiculos.pop(1)
print(vehiculos)

# Sort organiza los elementos de una lista alfabeticamente
vehiculos.sort()
print(vehiculos)

#Reverse organiza los elementos de una lista a la inversa
vehiculos.reverse()
print(vehiculos)

#Unir Listas
coleccion1 = [1,2,3]
coleccion2 = [4,5,6]

#Si creamos una nueva lista podemos concatenar ambas listas en la nueva colección3 sin modificar ninguna de las 2
coleccion3= coleccion1 + coleccion2
print(coleccion3)

#En este caso si usamos el metodo extend va a modificar una de las dos listas
coleccion1.extend(coleccion2)
print(coleccion1)