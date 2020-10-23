class Ingresos:
    def __init__(self):
        self.ingreso = []

    def IngresarMonto(self, Ingreso):
        NuevoIngreso = Ingreso
        self.ingreso.append((NuevoIngreso))

    def VerIngreso(self):
        for NuevoIngreso in self.ingreso:
            print("Ha ingresado: " + ingreso)

    def ObtenerIngresos(self):
        return self.ingreso

"""class Egresos:
    def __init__(self):
        self.egreso = []

    def EgresarMonto(self, monto):
        NuevoEgreso = monto
        self.egreso.append(egreso)

    def VerEgreso(self):
        for NuevoEgreso in self.egreso:
            print("Su monto Egresado es: " + egreso)

    def ObtenerEgreso(self):
        return self.egreso
    

class Finanzas:
    def __init__(self,monto):
        self.monto = monto
    
    def Total(self):
        ingreso = ingreso.ObtenerIngresos()
        egreso = egreso.ObtenerEgreso()
        Total = self.monto(ingreso-egreso)
        for Ingresos in ingreso:
            Ingresos+= ingreso 
    
        for Egresos in egreso:
            Egresos+= egreso
        
        return Total
        
    def Ingreso(self, monto):
        Ingresos.IngresarMonto(monto)
    
    def Egreso(self,mont):
        Egresos.EgresarMonto(monto)
    def         """