"""
crear un archivo py
y dentro crearéis una clase Vehículo,
haréis un objeto de ella,
lo guardaréis en un archivo
y luego lo cargamos.
"""
import pickle

# Creamos la clase Vehiculo
class Vehiculo:
    marca = ""
    precio = 0.0

    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

    def get_brand(self):
        return self.marca


# Hacemos un objeto de la clase
v1 = Vehiculo("Seat", 15000.3)

# Serializamos el objeto vehiculo en un fichero
f = open('vehiculo.bin', 'wb') # b porque queremos que sea binario
pickle.dump(v1, f)
f.close()

# Abrimos el fichero
file = open('vehiculo.bin', 'rb') # Ahora r porque leemos
vehiculo = pickle.load(file)
file.close()

print(type(file))
print(vehiculo.get_brand(), "precio: ", vehiculo.precio)
