#El bloque try y except se deben de usar de forma consiente, sabiendo que error se va a generar y como saberlo manejar
try:
    numero = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")
x = 10

try:
    print(x)
except NameError: #El Error se debe de capturar en el except, de lo contrario se genera un error y el programa se detiene.
    print("La variable x no esta definida.")
finally: #El bloque finally se ejecuta siempre, sin importar si se genero un error o no.
    print("Este bloque se ejecutara siendo exitoso o no el bloque try.")

#De esta forma se maneja los errores de forma consiente, en python.
