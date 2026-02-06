#Si necesirtamos usar comillas en una cadena de texto
#Podemos usar las comillas simples o dobles segun
#Segun el ejemplo siguiente:
print("Hola 'mundo'")
print('Hola "Mundo"')

ingles="I'm John"
#Las comillas triples permirten crear saltos de linea
#en la salida de la consola
Multiples="""Hola
Mundo
desde
las
comillas
triples"""

print(ingles)
print(Multiples)

#Con la funcion len() podemos conocer la cantidad de caracteres
#que tiene una cadena de texto
palabra="Murcielago"   
print(len(palabra))  #Salida: 10

#Verifica si una subcadena esta incluida en una cadena
#de caracteres con la palabra reservada 'in'
#Se debe de teber cuidado con mayusculas y minusculas
#Ya que python es case sesitive
texto="Este curso es de fundamentos de python"
estaIncluida="python"in texto

#Verifica si una subcadenas no esta incluida en una cadena

noEstaIncluida="Java"not in texto

print(noEstaIncluida)  #Salida: True
print(estaIncluida)  #Salida: True

#Convierte una cadena de texto a mayusculas y es un metodo
#de los objetos string
mayuscula = texto.upper()
print(mayuscula)  #Salida: ESTE CURSO ES DE FUNDAMENTOS DE PYTHON

#Convierte una cadena de texto a minisculas
minuscula = texto.lower()
print(minuscula)  #Salida: este curso es de fundamentos de python

#Elimina los espacios en blanco tanto al inicio como al final
#de una cadena de texto
#con el metodo strip()
espacios ="     Este es el texto con espacios     "
sinEspacios=espacios.strip()

#Es muy util cuando se leen datos de entrada y pueda que el usuario haya dejado
#espacios y sea en un campo de contraseñas.
print(sinEspacios)


