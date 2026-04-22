# Mónica García
# EJERCICIO 6

# CONDICIONALES EN PYTHON
# SOLICITAMOS EL USUARIO SI LA COMPUTADORA ENCIENDE
encendido = input("¿La computadora enciende? (si/no) : ")

# SILICITAMOS SI ESCUCHA ALGUN PITIDO AL ENCENDER
pitido = input("¿Escuchas algún pitido al encender? (si/no) : ")

# SOLICITAMOS SI EL MONITOR MUESTRA IMAGEN
imagen = input("¿El monitor muestra imagen? (si/no)")

# EVALUAMOS SI LA COMPUTADORA NO ENCIENDE
if encendido == "no":
    print("Diagnostico: Verificar conexion electrica o fuente de poder")
# SI ENCIENDE
else:
    # EVALUAMOS SI HAY PITIDOS
    if pitido == "si":
        print("Diagnóstico: Problema de hardware detectado (memoria RAM, tarjeta madre)")
    else:
        # EVALUAMOS SI HAY IMAGEN
        if imagen == "no":
            print("Diagnóstico: revisar conexion del monitor o tarjeta de video")
        else:
            print("Diagnóstico: La computadora parece encender correctamente.")
