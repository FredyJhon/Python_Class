# Funcion: Es un bloque de codigo que solo se ejecuta cuando la llamamos.
#Permite organizar y modularizar el codigo ("Reutilizacion de codigo"), ademas de mejorar la legibilidad del mismo.

def saludar(nombre, nacionalidad="Colombia"): #Argumento se le llama a lo que va dentro de los corchetes.
    print("Hola",nombre,"de", nacionalidad)

# saludar("Pedro") #Se llama parametros a los valores que le pasamos a la funncion.
# saludar("John", "Argentina")
# saludar("Sofia")

def sumar(a,b):
    return a + b #La palabra reservada return se utiliza para devolver un valor desde la funcion.

resultado = sumar(2,3)
print(resultado)


def funcion():
    pass #La palabra reservada pass se utiliza como un marcador de posicion para indicar que no se ha implementado el codigo de la funcion aun. Es util para evitar errores de sintaxis cuando se esta desarrollando el codigo.


def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

resultado_resta = restar(10,4)
print(resultado_resta)

resultado_multiplicacion = multiplicar(20,10)
print(resultado_multiplicacion)

resultado_division = dividir(100,50)
print(resultado_division)