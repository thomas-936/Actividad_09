print("Actividad 09")

opcion = 0

turistas = {}

while opcion != 4:
    print("\n +++MENU+++")
    print("1. Registrar clientes")
    print("2. Listado de clintes")
    print("3. Cliente con más destinos")
    print("4. Salir....")

    try:
        opcion =  int(input("Ingrse su Opcion: "))
    except ValueError:
        print("Ingrese una opcion valida... ")
        continue

    match opcion:
        case 1:
            print("Registrar clientes: ")
            cantidad_clietes = int(input("Ingrese la cantidad de clinetes que desea registrar: "))

            for i in range(cantidad_clietes):
                print(f"Clinete #{i+1}:")
