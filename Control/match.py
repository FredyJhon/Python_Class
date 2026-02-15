dia = 10

match dia:
    case 1:
        print("Hoy es Lunes")
    case 2:
        print("Hoy es Martes")
    case 3:
        print("Hoy es Miercoles")
    case 4:
        print("Hoy es Jueves")
    case 5:
        print("Hoy es Viernes")
    case 6:
        print("Hoy es Sabado")
    case 7:
        print("Hoy es Domingo")
    case _:
        print("No coincide con las opciones disponibles")

#El match es una nueva sentencia incorpotada en la version de python 3.10
#Se usa la expresion _ para captura los datos que no se encuentren disponibles
#en los casos de match

mes = int(input("Por favor, ingrese el numero del mes que quiere consultar: "))

match mes:
    case 1:
        print("estamos en el mes de Enero")
    case 2:
        print("estamos en el mes de Febrero")
    case 3:
        print("estamos en el mes de Marzo")  
    case 4:
        print("estamos en el mes de Abril")
    case 5:
        print("estamos en el mes de Mayo")
    case 6:
        print("estamos en el mes de Junio")
    case 7:
        print("estamos en el mes de Julio")
    case 8:
        print("estamos en el mes de Agosto")
    case 9:
        print("estamos en el mes de Septiembre")
    case 10:
        print("estamos en el mes de Octubre")
    case 11:
        print("estamos en el mes de Noviembre")
    case 12:
        print("estamos en el mes de Diciembre")
    case _:
        print("Este dato no coincide con los meses del año")