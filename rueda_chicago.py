"""Rueda de Chicago - Grupo 8 (arquitectura educativa de referencia).

El motor eléctrico hace girar la rueda; la rueda calcula su ángulo.
Es una simulación de software, no una medición del prototipo.
"""


class MotorElectrico:
    def __init__(self):
        self.encendido = False
        self.rpm = 0

    def encender(self, rpm):
        self.encendido = True
        self.rpm = rpm

    def apagar(self):
        self.encendido = False
        self.rpm = 0


class RuedaChicago:
    def __init__(self, motor, cabinas=8):
        self.motor = motor
        self.cabinas = cabinas
        self.angulo = 0

    def girar(self, segundos):
        grados = self.motor.rpm * 360 / 60 * segundos
        self.angulo = (self.angulo + grados) % 360
        return self.angulo


if __name__ == "__main__":
    motor = MotorElectrico()
    rueda = RuedaChicago(motor)
    motor.encender(rpm=4)
    print(rueda.girar(segundos=2))  # 48.0
