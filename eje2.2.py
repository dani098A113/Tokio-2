total_factura = float(input("Por favor, ingresa el total de la factura: "))

if total_factura < 10000:
    print("Sin comisión.")
else:
    comision = total_factura * 0.05
    total_con_comision = total_factura + comision
    print(f"El total de la factura con comisión es: {total_con_comision} (5% de comisión incluida).")
