v = True
f = False

print(v)
print(f)

print(5 > 3) # Verdadero
print(2 > 4) # Falso
print(3 > 1) # Verdadero

print(type(v))

print(bool("Hola Mundo")) # En este caso la cadena no esta vacia por lo que nos va a decir que es True.
print(bool("")) # En este caso la cadena esta vacia por lo que nos va a decir que es False.

#True

print(bool("abc"))
print(bool(123))
print(bool(["Manzana", 1 ,"Pera"]))

#False

print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None))

#Ejemplo de uso de isinstance() para verificar si una variable es de un tipo específico.
x = 10.5
print(isinstance(x, int))

