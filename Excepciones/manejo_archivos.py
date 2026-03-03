# open(nombre, modo)

# R (read) Lectura
# W (write) Escritura
# X (Crea archivo nuevo)

# try:
#     with open("archivo.txt", "r", encoding="utf-8") as f: #El bloque with se utiliza para manejar archivos de manera segura, asegurando que el archivo se cierre correctamente despues de su uso, incluso si ocurre un error durante la operacion.
#         print(f.readline())
#         print(f.readline())
# except FileNotFoundError:
#     print("El archivo no existe.")

# f = open("archivo.txt", "r")
# print(f.readline())
# f.closed()#Cierra el archivo, es importante cerrar el archivo despues de usarlo para liberar los recursos del sistema.



# try:
#     with open("archivo.txt", "a") as f: 
#         f.write("\n")
#         f.write("Hola, mundo desde el write en el white.")
#     with open("archivo.txt", "r", encoding="utf-8") as f: #El bloque with se utiliza para manejar archivos de manera segura, asegurando que el archivo se cierre correctamente despues de su uso, incluso si ocurre un error durante la operacion.
#         print(f.read())
# except FileNotFoundError:
#     print("No se ha encontrado el archivo.")
# # con este bloque usando la W se sobreescribe el contenido del archivo.


# try:
#     with open("archivo.txt", "r", encoding="utf-8") as f: #El bloque with se utiliza para manejar archivos de manera segura, asegurando que el archivo se cierre correctamente despues de su uso, incluso si ocurre un error durante la operacion.
#         print(f.readline())
#         print(f.readline())
# except FileNotFoundError:
#     print("El archivo no existe.")


try:
    with open("archivo.txt", "r", encoding="utf-8") as f: #El bloque with se utiliza para manejar archivos de manera segura, asegurando que el archivo se cierre correctamente despues de su uso, incluso si ocurre un error durante la operacion.
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x")
    print("No se encontro el archivo.")


try:
    with open("archivo.txt", "a") as f: 
        f.write("Hola, mundo desde el write en el white.")
        f.write("\n")
    with open("archivo.txt", "r", encoding="utf-8") as f: #El bloque with se utiliza para manejar archivos de manera segura, asegurando que el archivo se cierre correctamente despues de su uso, incluso si ocurre un error durante la operacion.
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo.")
# con este bloque usando la W se sobreescribe el contenido del archivo.

