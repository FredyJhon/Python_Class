# Declaramos una variable N para definir la cantidad de numeros de Fibonacci que queremos generar.
N = 20
# Inicializamos las varibales a y b que son los dos primeros numeros de la secuencia fibonacci, en este caso 0 y 1.
a = 0
b = 1
# Debemos de implementar un ciclo for que se ejecute N veces, en cada iretación y se recorra la secuencia de fibonnaci.
for i in range(N):
    print(a)
    a,b = b, a+b
#En python usamos la coma en a, b oara permitir la asignación multiple o "Desempaquetado de tuplas"
#Esto hace que evalue todo el lado derecho de la linea 9 primero y cree una tupla temporal (b, a+b) y luego, asigne los valores
#simultaneamente a las variables de la izquierda, esto permite intercambiar o actualizar valores sin usar una variable temporal.

print("_______________________")
