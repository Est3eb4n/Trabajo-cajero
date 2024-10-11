
from time import sleep
# funcion para hacer retiros ademas de que tambien guardamos toda la info de los movimientos
def debito(cuentas,movimientos,localtime):
    print("Bienvenido")
    print("ingrese su documento")
    val_d = input("= ")
    print("ingrese su clave")
    val_c = input("= ")

    for cuenta in cuentas:
            if cuenta["cc"] == val_d and cuenta["clave"] == val_c:
                print(f"La cuenta a que va a ingresar el dinero es {cuenta['cta']}")
                saldo =int(input(f"Ingrese el monto que dese ingresar = $ "))
                #-----------------------------------------------------------------------
                if cuenta["saldo"] < saldo:
                     print("no tienes suficientes fondos para este retiro")
                     break
                elif saldo <= 0:
                     print("no puedes retirar un valor negativo o igual a cero")
                     break
                #-----------------------------------------------------------------------
                cuenta["saldo"] -= saldo
                for movimiento in movimientos:
                    if cuenta["cta"] == movimiento["cta"]:
                        movimiento["movimientos"].append({
                        "tipo": "retiro",
                        "referencia": "",
                        "descripcion": f"se ha retirado ${saldo}",
                        "saldo": f"${cuenta['saldo']}",
                        "fecha": f"{localtime()}",
                        })
                        print(movimiento)
                    else:
                        print("cuenta no encontrada")
            else:
                return print("no se encontro la cuenta")
