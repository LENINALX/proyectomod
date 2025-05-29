from modelos.vuelo import VueloDB
from modelos.pasajero import PasajeroDB

class SistemaGestionAeropuerto:
    def __init__(self, db):
        self.vuelos_db = VueloDB(db)
        self.pasajeros_db = PasajeroDB(db)

    def crear_vuelo(self, numero_vuelo, origen, destino, hora_salida, hora_llegada):
        if self.vuelos_db.obtener(numero_vuelo):
            print(f"El vuelo {numero_vuelo} ya existe.")
        else:
            self.vuelos_db.crear({
                "numero_vuelo": numero_vuelo,
                "origen": origen,
                "destino": destino,
                "hora_salida": hora_salida,
                "hora_llegada": hora_llegada,
                "pasajeros": []
            })
            print(f"Vuelo {numero_vuelo} creado.")

    def eliminar_vuelo(self, numero_vuelo):
        if self.vuelos_db.obtener(numero_vuelo):
            self.vuelos_db.eliminar(numero_vuelo)
            print(f"Vuelo {numero_vuelo} eliminado.")
        else:
            print(f"El vuelo {numero_vuelo} no existe.")

    def registrar_pasajero(self, id_pasajero, nombre, apellido, pasaporte):
        if self.pasajeros_db.obtener(id_pasajero):
            print(f"El pasajero {id_pasajero} ya existe.")
        else:
            codigo_abordaje = f"{id_pasajero}-{pasaporte[:3]}"
            self.pasajeros_db.crear({
                "id_pasajero": id_pasajero,
                "nombre": nombre,
                "apellido": apellido,
                "pasaporte": pasaporte,
                "codigo_abordaje": codigo_abordaje
            })
            print(f"Pasajero {nombre} {apellido} registrado.")

    def eliminar_pasajero(self, id_pasajero):
        if self.pasajeros_db.obtener(id_pasajero):
            self.pasajeros_db.eliminar(id_pasajero)
            print(f"Pasajero {id_pasajero} eliminado.")
        else:
            print(f"El pasajero {id_pasajero} no existe.")

    def asignar_pasajero_a_vuelo(self, id_pasajero, numero_vuelo):
        vuelo = self.vuelos_db.obtener(numero_vuelo)
        pasajero = self.pasajeros_db.obtener(id_pasajero)

        if not vuelo or not pasajero:
            print("Vuelo o pasajero no existen.")
            return

        if id_pasajero not in vuelo.get("pasajeros", []):
            vuelo["pasajeros"].append(id_pasajero)
            self.vuelos_db.modificar(numero_vuelo, {"pasajeros": vuelo["pasajeros"]})
            print(f"Pasajero {id_pasajero} asignado al vuelo {numero_vuelo}.")

    def mostrar_vuelos(self):
        vuelos = self.vuelos_db.listar()
        if not vuelos:
            print("No hay vuelos registrados.")
        else:
            for vuelo in vuelos:
                print(f"Vuelo {vuelo['numero_vuelo']}: {vuelo['origen']} -> {vuelo['destino']}, "
                      f"Salida: {vuelo['hora_salida']}, Llegada: {vuelo['hora_llegada']}, "
                      f"Pasajeros: {vuelo.get('pasajeros', [])}")

    def mostrar_pasajeros(self):
        pasajeros = self.pasajeros_db.listar()
        if not pasajeros:
            print("No hay pasajeros registrados.")
        else:
            for p in pasajeros:
                print(f"{p['id_pasajero']} - {p['nombre']} {p['apellido']} | Pasaporte: {p['pasaporte']} | "
                      f"Código de abordaje: {p['codigo_abordaje']}")
