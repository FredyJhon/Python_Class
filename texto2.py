#Siempre que empezemos a contar los indices con python
#Se empieza desde el numero 0
# ind    0123456789
texto = "Este es un texto"
print(texto[0])  # Salida: E
print(texto[4])  # Salida:

#Si queremos obtener el total de los caracteres a imprimir
#usaremos entre corchetes el indice inicial y : sin embargo 
#se pueden usar los indices negativos para contar desde el final
#O se añaden las posiciones que se quieren imprimir.
print(texto[5:]) 


#El metodo replace() nos permite reemplazar una subcadena
#Este metodo modifica todas las apariciones de esa palabra
#si esta varias veces en la cadena de texto
curso = "Este curso es de JavaScript"
print(curso.replace("JavaScript","Python"))  
#Salida: Este curso es de Python


#El metodo split() permite dividir una cadena de texto
#en varias subcadenas segun el separador que se le indique.
textoDividido = texto.split(" ")
print(textoDividido)

#Normalización

#Usamos lower()para convertir todo a minuscula y asi encontrar la subcadena que necesitamos
#sin importar si esta en mayusculas o minusculas 
#Lo importante es que comparemos ambas subcadenas en el mismo formato.
texto2 = "Este texto tiene MAYUSCULAS y minisculas y necesito encontrar algunas palabras"
print("mayusculas".lower() in texto2.lower())  #Salida: True

