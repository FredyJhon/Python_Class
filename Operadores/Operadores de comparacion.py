#Operadores de comparación
x = 5
y = 3
z = 5
print(x == y) #¿Si es igual ? False
print(x != y) #¿Si es diferente? True
print(x > y) #¿Si es mayor? True
print(x < y) #¿Si es menor? False
print(x >= y) #¿Si es mayor o igual? True
print(x >= z) #¿Si es mayor o igual? True
print(x <= z) #¿Si es menor o igual? True


# Operadores logicos
#Nos van a permitir realizar mas de una condicion a la vez.

print(x > y and y > z) #¿Si x es mayor que y y y es mayor que z? False
print(x > y or y > z) #¿Si x es mayor a y o y es mayor a z? True

v = True
f = False

print(not(v))
print(not(f))