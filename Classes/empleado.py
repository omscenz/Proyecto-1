from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["empresa"]
empleados_collection = db["empleados"]

class Empleado:
    def __init__(self, nombre, cargo, departamento):
        self.nombre = nombre
        self.cargo = cargo
        self.departamento = departamento
        self.tarjeta_id = None

    def save(self):
     result = empleados_collection.insert_one({
        "nombre": self.nombre,
        "cargo": self.cargo,
        "departamento": self.departamento,
        "tarjeta_id": self.tarjeta_id
    })
     self._id = result.inserted_id 
     return self._id

    def update_tarjeta_id(self, tarjeta_id):
        self.tarjeta_id = tarjeta_id
        empleados_collection.update_one(
            {"_id": self._id},
            {"$set": {"tarjeta_id": ObjectId(tarjeta_id)}}
        )
