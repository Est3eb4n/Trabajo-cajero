from time import sleep
#hacemos todo el proceso de pagar servicios asi como hacer el registro de los movimientos
def pago_servicio(cuentas, movimientos, localtime):

    print("Bienvenido")
    print("ingrese su documento")
    val_d = input("= ")
    print("ingrese su clave")
    val_c = input("= ")
    pg = input("""
(1) Pagar Servicio de Energia
(2) Pagar Servicio de Agua
(3) Pagar Servicio de Gas
""")

    if pg == "1" or pg == "2" or pg == "3":
        if pg == "1":
            servicio = "Energia"
        elif pg == "2":
            servicio = "Agua"
        elif pg == "3":
            servicio = "Gas"
        for cuenta in cuentas:
            if cuenta["cc"] == val_d and cuenta["clave"] == val_c:
                print(f"La cuenta a que va a ingresar el dinero es {cuenta['cta']}")
                print("Ingrese su referencia de pago")
                ref = input("= ")
                saldo =int(input(f"Ingrese el monto que desea pagar = $ "))
                #-----------------------------------------------------------------------
                if saldo <= 0:
                    print("no puedes pagar por un valor negativo o igual a cero")
                    break
                #-----------------------------------------------------------------------
                cuenta["saldo"] -= saldo
                #  buscamos los movimientos que corresponden y agregamos alli toda la informacion
                for movimiento in movimientos:
                    if cuenta["cta"] == movimiento["cta"]:
                        movimiento["movimientos"].append({
                        "tipo": "Pago de servicio",
                        "referencia": ref,
                        "descripcion": f"se pago el recibo de {servicio}",
                        "saldo": f"${cuenta['saldo']}",
                        "fecha": f"{localtime()}",
                        })
                        print(movimiento)
                    else:
                        print("cuenta no encontrada")
            else:
                return print("no se encontro la cuenta")
