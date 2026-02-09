#Texto Strings con diferentes tipos de comillas
comillasSimples ='Comillas Simples'
ComillasDobles ="Comillas Dobles"
ComillasTriples = '''Comillas Triples '''

print(comillasSimples)
print(ComillasDobles)
print(ComillasTriples)

#Numeros

a= 10
b= 3.14
c= 5+2j  #Numero complejo
print(a)
print(b)
print(c)

# Listas
#Son mutable, se puede modificar su contenido
lista = [0,1,2,3,4,5]
#Cada una de las posiciones de la lista se llama indice.
#Coleccion ordenada de elementos


#Tuplas
#Son inmutables, no se puede modificar su contenido
tupla = ("a", "b", "c")


#Diccionarios
#Podremos acceder a los elementos mediante una clave de cada 
#uno de ellos
#Son elementos mutables
diccionario={
    "nombre":"Juan",
    "edad":30,
    "ciudad":"Madrid"
}


#Conjuntos (sets)
#Coleccion desordenada de elementos unicos
conjunto ={1,1,2,2,3} #Output esperado: {1.2.3}

print(conjunto)


#Booleanos
booleanoVerdadero =True
booleanoFalso = False


