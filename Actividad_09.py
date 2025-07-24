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
                turistas[codigo]["destino"] = []

                while True:
                    cantidad_destinos = int(input("¿Cuántos destinos desea ingresar? (mínimo 1, máximo 5): "))
                    if cantidad_destinos >= 1 and cantidad_destinos < 5:
                        break
                    else:
                        print("Error: debe ingresar entre 1 y 5 destinos.")

                for j in range(cantidad_destinos):
                    destino = input(f"Destino #{j + 1}: ")
                    turistas[codigo]["destinos"].append(destino)





