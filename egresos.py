class Egresos:
    def __init__(self):
        self.egresos = []

    def Egresoar(self, monto):
        egreso = (monto)
        self.egresos.append(egreso)

    def MostrarE(self):
        for egreso in self.egresos:
            print("Su monto Egresado es: " + egreso)

    def ReporteEgresos(self):
        return self.egresos