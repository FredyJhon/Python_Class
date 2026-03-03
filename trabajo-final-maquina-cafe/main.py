from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import mostrar_historial

def  main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            pedir_cafe()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            print("\n Gracias por usar la maquina de cafe, hasta luego!")
            break
        else:
            print("Opcion no valida, por favor selecciona una opcion valida.")

if __name__ == "__main__":
    main()