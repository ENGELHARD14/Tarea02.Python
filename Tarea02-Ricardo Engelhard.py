"""
Ejercicio 02
finanzas personales (ingresos y egresos)
hacer un programa python para consola que le permita al usuario:
1. iniciar un proyecto de finanzas personales con cuenta a 0.00
2. dar opcion para registrar un ingreso o un egreso
3. si es un ingreso sumarlo a la cuenta
4. si es un egreso restarlo a la cuenta
5. verficar que si es un egreso y la cuenta esta a 0.0 debe aparecer
    el monto en negativo.
6. poder generar un reporte de todos los ingresos
7. poder generar un reporte de todos lo egresos
8. poder generar un reporte de todas las transacciones (ingresos y egreso)
9. poder generar un reporte solo de el total de la cuenta
restricciones del ejercicio:
el proyecto finanzas debe ser una clase, un ingreso debe ser una clase
y un egreso debe ser una clase tambien.
"""
Cuenta = 0.00
Ingresos = 0.00
Egresos = 0.00
ListaIngresos = []
ListaEgresos = []


class Finanzas:
    while True:

        print("-" * 100)
        print("Escriba: '1' para realizar un Ingreso")
        print("Escriba: '2' para realizar un Retiro")
        print("Escriba: '3' para recibir el reporte de sus Ingresos")
        print("Escriba: '4' para recibir el reporte de sus Egresos")
        print(
            "Escriba: '5' para generar un reporte de todas las transacciones (ingresos y egreso)"
        )
        print("Escriba: '6' para generar un reporte de el monto TOTAL de la cuenta")
        print("Escriba: '0' para SALIR")
        Menu = int(input("------------> "))

        if Menu == 1:

            Ingresos = float(input("Ingrese el Monto a Ingresar: "))
            Cuenta += Ingresos
            ListaIngresos.append(Ingresos)
            print(f"La Cantidad de {Ingresos} ha sido añadida")

        elif Menu == 2:
            Egresos = float(input("Ingrese la cantidad a Retirar: "))
            if Cuenta < Egresos:
                print("Saldo Insuficiente")
            else:
                Cuenta -= Egresos
                ListaEgresos.append(Egresos)
                print(f"La cantidad de {Egresos} ha sido retirada de su Cuenta")

        elif Menu == 3:
            print("Su Lista de Ingresos es: ", [ListaIngresos])
            print("La Cantidad Total Ingresada es de ", sum(ListaIngresos))

        elif Menu == 4:
            print("Su Lista de Egresos es: ", [ListaEgresos])
            print("La Cantidad Total Egresos es de ", sum(ListaEgresos))

        elif Menu == 5:
            print("Su Lista de Ingresos es: ", [ListaIngresos])
            print("La Cantidad Total Ingresada es de ", sum(ListaIngresos))
            print("----------------------------------------------")
            print("Su Lista de Egresos es: ", [ListaEgresos])
            print("La Cantidad Total Egresos es de ", sum(ListaEgresos))

        elif Menu == 6:
            print(f"El monto actual de su Cuenta es de {Cuenta}")

        elif Menu == 0:
            print("Gracias por Utilizar el Programa")
            break
