from classes.empleado import Empleado
from classes.tarjeta import TarjetaAcceso

# 1. Crear empleado y guardar
empleado = Empleado("Ana López", "Ingeniera de Software", "IT")
empleado_id = empleado.save()

# 2. Crear tarjeta con referencia al empleado
tarjeta = TarjetaAcceso("QR123456", "Alto", True, empleado_id)
tarjeta_id = tarjeta.save()

# 3. Actualizar empleado con el ID de la tarjeta
empleado.update_tarjeta_id(tarjeta_id)

print("Proceso completo exitosamente.")
