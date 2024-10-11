#aqui hacemos el conteo de todos los movimientos y los mostramos

def mov(cuentas,movimientos):
    numeroCuenta = input("dijite el numero de su cuenta ")
    clave = input("dijite la contraseña de su cuenta ")
    for cuenta in cuentas:
        if cuenta["cc"] == numeroCuenta and cuenta["clave"] == clave:
            for movimiento in movimientos:
                if movimiento["cta"] == cuenta["cta"]:
                    print(movimiento["movimientos"])
        else:
            print("codigo incorrecto")
