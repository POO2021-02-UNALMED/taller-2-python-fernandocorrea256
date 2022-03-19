class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, new_color):
        colors = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if not (new_color in colors):
            return
        self.color = new_color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        contador = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                contador += 1

    def verificarIntegridad(self):
        # verificar integridad asientos
        integridad_asientos = True

        registro_asiento = False
        nAsientos = len(self.asientos)
        if nAsientos > 0:
            registro_asiento = self.asientos[0].registro

            i = 1
            while (integridad_asientos) and (i < nAsientos):
                if not (self.asientos[i].registro == registro_asiento):
                    integridad_asientos = False
                i += 1

        if integridad_asientos:
            original = (registro_asiento == self.registro) and (registro_asiento == self.motor.registro)
        else:
            original = False

        if original:
            return "Auto original"
        else:
            return "Las piezas no son originales"
            



class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindors = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevo_registro):
        self.registro = nuevo_registro

    def asignarTipo(self, nuevo_tipo):
        tipos = ["electrico", "gasolina"]
        if not (nuevo_tipo in tipos):
            return
        self.tipo = nuevo_tipo