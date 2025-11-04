from abc import ABC, abstractmethod

# -------------------
# OBSERVER
# -------------------
class Observer(ABC):
    @abstractmethod
    def update(self, mensaje):
        pass

class InventarioService(Observer):
    def update(self, mensaje):
        print(f"[Inventario] Actualización recibida: {mensaje}")

class EmailNotifier(Observer):
    def update(self, mensaje):
        print(f"[Email] Notificación enviada al cliente: {mensaje}")

class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
        self.observers = []

    def agregar_observer(self, observer):
        self.observers.append(observer)

    def notificar(self, mensaje):
        for obs in self.observers:
            obs.update(mensaje)

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
            if self.stock == 0:
                self.notificar(f"El producto {self.nombre} se agotó.")
        else:
            print("No hay suficiente stock.")

# -------------------
# STRATEGY
# -------------------
class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class PagoTarjeta(EstrategiaPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con Tarjeta de crédito.")

class PagoEfectivo(EstrategiaPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} en efectivo.")

class PagoPSE(EstrategiaPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} mediante PSE.")

class ContextoPago:
    def __init__(self, estrategia: EstrategiaPago):
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaPago):
        self.estrategia = estrategia

    def procesar_pago(self, monto):
        self.estrategia.pagar(monto)

# -------------------
# DEMO DEL MÓDULO
# -------------------
if __name__ == "__main__":
    # Producto con stock y observadores
    producto = Producto("Leche", 2)
    producto.agregar_observer(InventarioService())
    producto.agregar_observer(EmailNotifier())

    # Venta con estrategia de pago
    venta = ContextoPago(PagoTarjeta())
    producto.vender(1)
    venta.procesar_pago(3000)

    # Cambiar estrategia de pago
    venta.set_estrategia(PagoEfectivo())
    producto.vender(1)
    venta.procesar_pago(3000)
