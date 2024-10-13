paquetes_turisticos = []
paquete_creado = []

#------------------------------------------------------------------------------------------
 
def mostrar_menu_principal():
    print("Bienvenido al sistema de paquetes turísticos")
    print("1. Ver paquetes turísticos")
    print("2. Crear su propio paquete turístico")
    print("3. Salir")

def mostrar_menu_paquetes():
    print("Paquetes turísticos disponibles:")
    print("1. Paquete A: Playa y Sol")
    print("2. Paquete B: Aventura en la Montaña")
    print("3. Paquete C: Tour por la Ciudad")
    print("4. Mostar los paquetes que tienes registrados")
    print("5. Volver al menú principal")

def crear_paquete():
    nombre = input("Ingrese el nombre de su paquete turístico: ")
    paquete_creado.append(nombre)
    descripcion = input("Ingrese una descripción para su paquete turístico: ")
    paquete_creado.append(descripcion)
    hotel = input("Ingrese el hotel de su preferencia referente a las estrellas (Hoteles 5 a 1 Estrella)") #Debemos de conectar esta variable con el de hoteles que genere una lista de los que haya.
    paquete_creado.append(hotel)
    precio = input("Ingrese el precio del paquete turístico: ")
    paquete_creado.append(precio)
    print (f"\n___________Paquete se ha creado___________\nNombre del Paquete: {paquete_creado[0]} \nDescripcion del paquete: {paquete_creado[1]} \nHotel que eligio es: {paquete_creado[2]} Estrellas \nPrecio del paquete: ${paquete_creado[3]}")
    print ("Se ha Guardado con exito su paquete!!")
    # print(f"Paquete '{nombre}' creado con éxito!")
    # print(f"Descripción: {descripcion}")
    # print(f"Precio: {precio}")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            while True:
                mostrar_menu_paquetes()
                opcion_paquete = input("Seleccione un paquete o vuelva al menú principal: ")

                if opcion_paquete == '5':
                    break
                elif opcion_paquete == '1':
                    print("Ha seleccionado el Paquete A: Playa y Sol")
                    paquetes_turisticos.append(opcion_paquete)
                elif opcion_paquete == '2':
                    print("Ha seleccionado el Paquete B: Aventura en la Montaña")
                    paquetes_turisticos.append(opcion_paquete)
                elif opcion_paquete == '3':
                    print("Ha seleccionado el Paquete C: Tour por la Ciudad")
                    paquetes_turisticos.append(opcion_paquete)
                elif opcion_paquete == '4':
                    print(f"Paquetes que has registrando son los siguientes: {paquetes_turisticos}")
                else:
                    print("Opción no válida, por favor intente de nuevo.")
        elif opcion == '2':
            crear_paquete()
        elif opcion == '3':
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()


print ("Hola mundo")