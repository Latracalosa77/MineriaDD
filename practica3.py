class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"Acelerando. La velocidad es:{self.velocidad} km/h")

    def frenar(self, cantidad):
        self.velocidad -= cantidad
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"Frenando. La velocidad es: {self.velocidad} km/h")

    def mostrar_info(self):
        print(f"--- Info Coche ---")
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")
        print(f"Color: {self.color} | Velocidad actual: {self.velocidad} km/h")


class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso de ${cantidad}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso de ${cantidad}")
        else:
            print("Saldo insuficiente o cantidad inválida.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo actual: ${self.saldo:.2f}")


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)

    def mostrar_info(self):
        area = self.calcular_area()
        perimetro = self.calcular_perimetro()
        print(f"--- Info Dimensiones ---")
        print(f"Ancho: {self.ancho} | Alto: {self.alto}")
        print(f"Área: {area} | Perímetro: {perimetro}")


    # Ejemplo
mi_coche = Coche("Toyota", "Yaris GR", "Blanco")
mi_coche.acelerar(50)
mi_coche.mostrar_info()

mi_cuenta = CuentaBancaria("Yuki Tsunoda")
mi_cuenta.depositar(500)
mi_cuenta.retirar(200)
mi_cuenta.mostrar_saldo()

mi_rect = Rectangulo(10, 5)
mi_rect.mostrar_info()