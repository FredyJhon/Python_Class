

ARCHIVOS_PEDIDOS = "pedidos.txt"

def mostrar_historial():
    try:
        print("\n Historial de pedidos de cafe")
        with open(ARCHIVOS_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate (pedidos, start=1):
                    print(str(i) + "." + pedido.strip())
            else:
                print("No hay pedidos en el historial.")
    except FileNotFoundError:
        print("\n Todavia no existe un historial de pedidos.")
