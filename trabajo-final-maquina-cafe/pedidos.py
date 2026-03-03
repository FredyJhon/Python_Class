ARCHIVOS_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elige el cafe que prefieres.")
    print("1. Expresso")
    print("2. Americano")
    print("3. Capuchino")
    print("4. Volver al menu principal")

    opcion = input("Selecciona una opcion: ")

    cafes = {
        "1": "Expresso",
        "2": "Americano",
        "3": "Capuchino",
        "4": "Volver al menu principal"
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Has pedido un "+ cafe_elegido + ". 'Preprando tu cafe!...'")

        with open(ARCHIVOS_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opcion no valida, por favor selecciona una opcion valida.")
