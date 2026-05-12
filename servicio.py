# Importamos herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# =========================================
# CLASE ABSTRACTA SERVICIO
# =========================================

# Esta clase representa un servicio general
class Servicio(ABC):

    # Constructor
    def __init__(self, nombre, precio_base):

        # Validamos que el precio sea correcto
        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor a cero")

        # Atributos del servicio
        self.nombre = nombre
        self.precio_base = precio_base

    # Método abstracto
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    # Método abstracto
    @abstractmethod
    def descripcion(self):
        pass

# =========================================
# CLASE RESERVA DE SALA
# =========================================

# Esta clase hereda de Servicio
class ReservaSala(Servicio):

    # Método para calcular el costo
    def calcular_costo(self, horas):

        # Validamos las horas
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        # Calculamos el total
        total = self.precio_base * horas

        return total

    # Método descripción
    def descripcion(self):

        return f"Servicio de reserva de sala: {self.nombre}"
    
# =========================================
# CLASE ALQUILER DE EQUIPOS
# =========================================

# Esta clase hereda de Servicio
class AlquilerEquipo(Servicio):

    # Método para calcular el costo
    def calcular_costo(self, horas):

        # Validamos las horas
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        # Calculamos el total
        total = (self.precio_base * horas) + 20

        return total

    # Método descripción
    def descripcion(self):

        return f"Servicio de alquiler de equipos: {self.nombre}"
    
# =========================================
# CLASE ASESORIA
# =========================================

# Esta clase hereda de Servicio
class Asesoria(Servicio):

    # Método para calcular el costo
    def calcular_costo(self, horas):

        # Validamos las horas
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a cero")

        # Calculamos el total con incremento del 15%
        total = (self.precio_base * horas) * 1.15

        return total

    # Método descripción
    def descripcion(self):

        return f"Servicio de asesoría especializada: {self.nombre}"
    
# =========================================
# PRUEBAS DEL SISTEMA
# =========================================

try:
    # Creamos servicios
    servicio1 = ReservaSala("Sala VIP", 50)
    servicio2 = AlquilerEquipo("Computadores", 30)
    servicio3 = Asesoria("Asesoría Python", 100)

    # Mostramos información
    print(servicio1.descripcion())
    print("Costo:", servicio1.calcular_costo(5))

    print("---------------------------------------------------")

    print(servicio2.descripcion())
    print("Costo:", servicio2.calcular_costo(3))

    print("---------------------------------------------------")

    print(servicio3.descripcion())
    print("Costo:", servicio3.calcular_costo(2))

except ValueError as error:

    print("Error detectado:", error)
