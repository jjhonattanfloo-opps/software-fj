from servicio import Servicio

class Reserva:
    def __init__(self, cliente, servicio, horas):
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"
from servicio import Servicio

class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if cliente == "":
                raise ValueError("Cliente invalido")

            if not isinstance(servicio, Servicio):
                raise TypeError("Servicio invalido")

            if horas <= 0:
                raise ValueError("Horas invalidas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except Exception as e:
            raise Exception(f"Error al crear reserva: {e}")
from servicio import Servicio

class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if cliente == "":
                raise ValueError("Cliente invalido")

            if not isinstance(servicio, Servicio):
                raise TypeError("Servicio invalido")

            if horas <= 0:
                raise ValueError("Horas invalidas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except Exception as e:
            raise Exception(f"Error al crear reserva: {e}")

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar_reserva(self):
        costo = self.servicio.calcular_costo(self.horas)
        return costo
from servicio import Servicio, ReservaSala

class Reserva:
    def __init__(self, cliente, servicio, horas):
        try:
            if cliente == "":
                raise ValueError("Cliente invalido")

            if not isinstance(servicio, Servicio):
                raise TypeError("Servicio invalido")

            if horas <= 0:
                raise ValueError("Horas invalidas")

            self.cliente = cliente
            self.servicio = servicio
            self.horas = horas
            self.estado = "Pendiente"

        except Exception as e:
            raise Exception(f"Error al crear reserva: {e}")

    def confirmar(self):
        self.estado = "Confirmada"
        print(f"Reserva confirmada para {self.cliente}")

    def cancelar(self):
        self.estado = "Cancelada"
        print(f"Reserva cancelada para {self.cliente}")

    def procesar_reserva(self):
        try:
            costo = self.servicio.calcular_costo(self.horas)
            print(f"Cliente: {self.cliente}")
            print(f"Servicio: {self.servicio.descripcion()}")
            print(f"Costo total: {costo}")
            self.confirmar()

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    servicio1 = ReservaSala("Sala VIP", 50)
    reserva1 = Reserva("Juan Perez", servicio1, 2)
    reserva1.procesar_reserva()    