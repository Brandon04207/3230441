class metodoDePago:
    def hablar(self, monto):
        raise NotImplementedError ("error")

class papypal (metodoDePago):
    def hablar (self, monto):
        return f"pago {monto} pesos en papypal"
    
class tarjeta (metodoDePago):
    def hablar (self, monto):
        return f"pago {monto} pesos en tarjeta"

class contraEntrega (metodoDePago):
    def hablar (self, monto):
        return f"pago {monto} pesos en contra entrega"
    
class cripto (metodoDePago):
    def hablar (self, monto):
        return f"pago {monto} pesos en cripto"
    
metodoDePagos = [papypal(), tarjeta(), contraEntrega(), cripto()]
 
for metodoDePago in metodoDePagos:
    
  print(metodoDePago.hablar(100))