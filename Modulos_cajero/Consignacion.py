

def consignacion(cuentas,movimientos,localtime):
    
    print ("Ingrece su nùmero de cuenta o numero de documento ")
    cc = input("= ")
    for dinero in cuentas:
      if dinero["cc"] == cc or dinero["cta"] == cc:
       print(f"La cuenta a que va a ingresar el dinero es {dinero['cta']}")
       saldo =int(input(f"Ingrese el monto que dese ingresar = $ "))
       #---------------------------------------------------------------------
       if dinero["saldo"] < saldo:
          print("no tienes suficientes fondos para este retiro")
          break
       elif saldo <= 0:
          print("no puedes retirar un valor negativo o igual a cero")
          break
       #-----------------------------------------------------------------------
       dinero["saldo"] += saldo
       for movimiento in movimientos:
         if dinero["cta"] == movimiento["cta"]:
            movimiento["movimientos"].append({
              "tipo": "consignacion",
              "referencia": "",
              "descripcion": f"se ha consignado ${saldo}",
              "saldo": f"${dinero['saldo']}",
              "fecha": f"{localtime()}",
            })
         print(movimiento)
      else:
        print("cuenta no encontrada")