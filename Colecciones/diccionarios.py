#Esto es un ejemplo de un diccionario en Python.
from encodings import johab


auto = { 
    "marca": "Toyota",
    "modelo": "TXL",
    "año": 2025
}

print(auto)
print(auto["marca"]) #Si no esta la clave, se genera un error.
print(auto["modelo"])
print(auto["año"])
print(auto.get("marca")) #Si no esta la clave, devuelve None.


print(auto.keys()) #Devuelve las claves del diccionario.
print(auto.values()) #Devuelve los valores del diccionario.

if "marca"in auto:
    print("La marca es una de las propiedades de este diccionario.")


#Modificar un valor del diccionario.
auto["año"] = 2024
print(auto)

#Agrega un nuevo clave-valor al diccionario.
auto["color"] = "blanco"
print(auto)

#Actualizar el diccionario con el metodo update, si la clave ya existe, se actualiza su valor, si no existe, se agrega la nueva clave-valor.
auto.update({"año": 2023, "color": "rojo", "puertas": 4})
print(auto)

# auto.pop("puertas")
# print(auto)

# #Elimina el ultmo elementos agregado al diccionario.
# auto.popitem()
# print(auto)

# #Elimina todos los elementos del diccionario.
# auto.clear()
# print(auto)


for k in auto: #Recorre las claves del diccionario.
    print(k)

print("-------------------")

#Recorre los valores del diccionario.
for v in auto.values(): 
    print(v)


#Recorre las claves y valores del diccionario.
for k, v in auto.items(): 
    print(k, v)

print("-------------------")

#Diccionarios Anidados
#Los diccionarios tambien llevan el nombre de objetos directos
#Diccionario externo
familia = {
   "hijo1" : {   # Este es un diccionario es una clave del diccionario externo.
    "nombre": "John", #Teniendo como valor un diccionario interno.
    "edad": 29 
   },  
   "hijo2" : {
    "nombre": "Andres",
    "edad": 32 
   }, 
   "hijo3" : {
    "nombre": "Sofia",
    "edad": 14
   } 
}
print(familia["hijo1"]["nombre"], familia["hijo1"]["edad"]) #Accede al valor del diccionario interno.
