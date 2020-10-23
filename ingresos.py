class Ingresos:
    def __init__(self):
        self.ingresos = []

    def Ingresar(self, monto):
        ingreso = monto
        self.ingresos.append(ingreso)

    def MostrarI(self):
        for ingreso in self.ingresos:
            print("El monto ingresado es :" + ingreso)

    def ReporteIngresos(self):
        return self.ingresos
