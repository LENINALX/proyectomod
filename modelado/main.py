from database.mongo_manager import MongoManager
from system.gestor import SistemaGestionAeropuerto

def main():
    print(">>> Iniciando sistema de gestión de aeropuerto...")

    db = MongoManager()
    sistema = SistemaGestionAeropuerto(db)

    while True:
        print("\n--- Menú ---")
        print("1. Crear vuelo")
        print("2. Registrar pasajero")
        print("3. Asignar pasajero a vuelo")
        print("4. Mostrar vuelos")
        print("5. Mostrar pasajeros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = input("Número de vuelo: ")
            origen = input("Origen: ")
            destino = input("Destino: ")
            salida = input("Hora de salida: ")
            llegada = input("Hora de llegada: ")
            sistema.crear_vuelo(numero, origen, destino, salida, llegada)

        elif opcion == '2':
            id_pasajero = input("ID del pasajero: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            pasaporte = input("Pasaporte: ")
            sistema.registrar_pasajero(id_pasajero, nombre, apellido, pasaporte)

        elif opcion == '3':
            id_pasajero = input("ID del pasajero: ")
            numero_vuelo = input("Número de vuelo: ")
            sistema.asignar_pasajero_a_vuelo(id_pasajero, numero_vuelo)

        elif opcion == '4':
            sistema.mostrar_vuelos()

        elif opcion == '5':
            sistema.mostrar_pasajeros()

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
