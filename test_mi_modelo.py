import unittest
from classes.empleado import Empleado
from classes.tarjeta import TarjetaAcceso
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["empresa"]
empleados_collection = db["empleados"]
tarjetas_collection = db["tarjetas"]

class TestModelo(unittest.TestCase):

    def setUp(self):
        empleados_collection.delete_many({})
        tarjetas_collection.delete_many({})

    def test_creacion_relacionada(self):
        emp = Empleado("Luis Pérez", "Contador", "Finanzas")
        emp_id = emp.save()
        self.assertIsNotNone(emp_id)

        tarjeta = TarjetaAcceso("NF1234", "Medio", True, emp_id)
        tarjeta_id = tarjeta.save()
        self.assertIsNotNone(tarjeta_id)

        emp.update_tarjeta_id(tarjeta_id)
        updated = empleados_collection.find_one({"_id": emp_id})
        self.assertEqual(updated["tarjeta_id"], tarjeta_id)

    def test_tarjeta_referencia_empleado(self):
        emp = Empleado("Maria Rivera", "Recursos Humanos", "RRHH")
        emp_id = emp.save()

        tarjeta = TarjetaAcceso("CARD555", "Bajo", True, emp_id)
        tarjeta_id = tarjeta.save()

        doc = tarjetas_collection.find_one({"_id": tarjeta_id})
        self.assertEqual(doc["empleado_id"], emp_id)

if __name__ == '__main__':
    unittest.main()
