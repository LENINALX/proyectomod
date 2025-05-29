class VueloDB:
    def __init__(self, db):
        self.collection = db.get_collection("vuelos")

    def crear(self, datos):
        self.collection.insert_one(datos)

    def obtener(self, numero_vuelo):
        return self.collection.find_one({"numero_vuelo": numero_vuelo})

    def modificar(self, numero_vuelo, cambios):
        self.collection.update_one({"numero_vuelo": numero_vuelo}, {"$set": cambios})

    def eliminar(self, numero_vuelo):
        self.collection.delete_one({"numero_vuelo": numero_vuelo})

    def listar(self):
        return list(self.collection.find())