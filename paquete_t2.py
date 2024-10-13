paquete_t = []
paquete_creado = []
adicional_paquete = []

while True:

    print("---------------MENU DE PAQUETES TURISTICOS--------------- \nSeleccione 1 opcion para ingresar al modulo\n------------------------------")
    print("1. Mostar paquetes")
    print("2. Crear paquete a su preferencia")
    print("3. Salir del modulo")
    print("------------------------------")
    
    opcion = input("Eliga una opcion: ")

    if opcion == '1':
        while True:
              print("----------Paquetes mas vendidos----------\n------------------------------")
              print("1. Paquete Turistico economico incluye lo siguiente \n* Hotel 1 Estrellas \n* Desayuno Incluido \n* Vuelo incluido de ida\n------------------------------")
              print("2. Paquete Turistico basico incluye lo siguiente \n* Hotel 3 Estrellas \n* Desayuno, almuerzo y cena incluido \n* Transporte al hotel\n------------------------------")
              print("3. Paquete Turistico Premium incluye lo siguiente \n* Hotel 5 Estrellas \n* Alimentacion Incluida mas bares \n* Vuelos incluidos de ida y vuelta \n* Trasporte al Hotel\n------------------------------")
              # print("4. Mostrar paquete seleccionado\n------------------------------")
              print("4. Salir.")
              print("------------------------------")
              #-----------------------------------------------------------------------------
              opcion_p = input("Ingresa una opcion: ")
              print("------------------------------")
              paquete_t.append(opcion_p)

              if opcion_p == '4':
                 break
              elif opcion_p == '1':
                print ("Usted ah ingresado la opcion 1 Paquete Turistico economico.\n------------------------------")
                break
              elif opcion_p == '2':
                print ("Usted ah ingresado la opcion 2 Paquete Turistico Basico.\n------------------------------")
                break
              elif opcion_p == '3':
                print ("Usted ah ingresado la opcion 3 Paquete Turistico Premium.\n------------------------------")
                break
              else:
                print("Elige nuevamente una opcion que sea correcta.\n------------------------------")
                # print(f"Los paquete que ha seleccionado son los siguientes {paquete_t}")
                
    elif opcion == '2':
      
      print(f"-----------------------CREA TU PAQUETE!!-----------------------")
      
      nombre_paquete = input("Ingrese un nombre para tu paquete personalizado: ")
      paquete_creado.append(nombre_paquete)
      #------------------------------
      descripcion = input("Ingrese la Descripcion del paquete: ")
      paquete_creado.append(descripcion)
      #------------------------------
      adicional = input("Ingrese lo que incluye el paquete (separado por comas): ")
      adicional_paquete.append(adicional)
      #------------------------------
      lista_adicional = adicional.split(',')
      adicional_paquete.extend(lista_adicional)
      lista_adicional = [item.strip() for item in lista_adicional]
      #------------------------------
      precio = float(input("Ingrese el precio que tiene el paquete: "))
      paquete_creado.append(precio)
      #------------------------------
      
      print(f"-----------------------PAQUETE CREADO-----------------------")
      print(f"Nombre del paquete: {paquete_creado[0]}")
      print(f"Descripcion del producto: {paquete_creado[1]}")
      print(f"Precio del paquete: ${paquete_creado[2]} COP")
      print(f"Lo que incluye el paquete:")
      for item in lista_adicional:
        print(f"-{item}")
      # print(f"Lo que incluye el paquete: {paquete_creado[2]}")
             
    elif opcion == '3':
      print("Gracias por su visita!!\n------------------------------")
      break   
    else:
      print("Eliga una opcion correcta nuevamente.")

    