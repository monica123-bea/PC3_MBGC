# Mónica García
# EJERCICIO 3

# SOLICITAMOS EL MONTO DE COMPRA
compra = float(input("Introduce el total de tu compra en quetzales:"))

if compra > 500:
    descuento = compra * 0.20
elif compra >= 300:
    descuento = compra * 0.15
elif compra >= 100:
    descuento = compra * 0.10
else:
    descuento = 0

total_pagar = compra - descuento

print("Total antes del descuento: Q", compra)
print("Descuento aplicado: Q", descuento)
print("Total a pagar: Q", total_pagar)
