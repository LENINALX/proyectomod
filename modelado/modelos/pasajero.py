class PasajeroDB:
    def __init__(self, db):
        self.collection = db.get_collection("pasajeros")

    def crear(self, datos):
        self.collection.insert_one(datos)

    def obtener(self, id_pasajero):
        return self.collection.find_one({"id_pasajero": id_pasajero})

    def eliminar(self, id_pasajero):
        self.collection.delete_one({"id_pasajero": id_pasajero})

    def listar(self):
        return list(self.collection.find())