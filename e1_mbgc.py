# Mónica García
# EJERCICIO 1

# SOLICITAMOS LA TEMPERATURA AL USUARIO
temperatura = float(input("Introduce la temperatura actual en grados Celsius: "))

if temperatura > 35:
    print("Alerta: Calor extremo: ")
elif temperatura >= 26:
    print("Hace calor")
elif temperatura >= 16:
    print("Clima agradable")
elif temperatura >= 6:
    print("Hace frio")
else:
    print("ALERTA: frio extremo")