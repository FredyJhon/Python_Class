x = 1
y = 2.5
z = 1j

print(type(x))  # Salida: <class 'int'>
print(type(y))  # Salida: <class 'float'>
print(type(z))  # Salida: <class 'complex'>

positivo = 5.5
negativo = -5.5
imaginario = -5 + -1j

#casteo de tipos
xf = float(x)  # Convierte int a float

print(type(xf))  # Salida: <class 'float'>
print(xf)

#Tener cuidado al convertir float a int, ya que se pierde la parte decimal
#Mas cuando se maneja datos financieros
ye = int(y)
print(type(ye))
print(ye)


entero= 5
flotante = 5.5

enteroComplejo = complex(entero)
flotanteComplejo = complex(flotante)

print(enteroComplejo)
print(type(enteroComplejo))

print(flotanteComplejo)
print(type(flotanteComplejo))


#Numeros aleatorios se importa la libreria random
#Sirve para generar numero aleatorias, por ejemplo en juegos.
import random  # noqa: E402

print(random.randrange(1,10)) #Output: Numero aleatorio entre 1 y 9


