# Mónica García
# EJERCICIO 4

# SOLICITAMOS LA ESTATURA DEL VISITANTE
estatura = float(input("Introduce tu estatura en metros:"))

if estatura >= 1.30:
    print("Puedes subir solo a la montaña rusa")
elif estatura >= 1.20:
    print("Puedes subir con un acompañante adulto")
else:
    print("No puedes subir a la montaña rusa")