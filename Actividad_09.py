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
                print(f"Cliente #{i+1}:")
                while True:
                    codigo =  input("Ingrese el codigo del clinete: ")
                    if codigo in turistas:
                        print("Este codigo de clinte ya fue registrado ingrse otro.")
                    else:
                        break

                turistas[codigo] = {}
                turistas[codigo]["nombre"] = input("Ingrese el nombre del clinte: ")
                turistas[codigo]["destino"] = {}

                cantidad_destinos = int(input("Cuntos destinos desea ingresar: "))
                for j in range(cantidad_destinos):
                    print(f"Destino #{i+1}:")
                    destino = input("Ingrse el nombre del desttino: ")




