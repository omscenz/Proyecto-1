from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["empresa"]
tarjetas_collection = db["tarjetas"]

class TarjetaAcceso:
    def __init__(self, codigo, nivel_acceso, activo, empleado_id):
        self.codigo = codigo
        self.nivel_acceso = nivel_acceso
        self.activo = activo
        self.empleado_id = empleado_id

    def save(self):
        result = tarjetas_collection.insert_one({
            "codigo": self.codigo,
            "nivel_acceso": self.nivel_acceso,
            "activo": self.activo,
            "empleado_id": ObjectId(self.empleado_id)
        })
        self._id = result.inserted_id
        return self._id
