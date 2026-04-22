# Mónica García
# EJERCICIO 9

# SOLICITAMOS EL AREA DEL PROBLEMA
area = input("¿En qué área es el problema? (software/hardware/red): ").lower()

# SOLICITAMOS LA GRAVEDAD DE PROBLEMA
gravedad = input("¿Qué tan grave es el problema? (alta/media/baja): "). lower()

# CLASIFICAMOS EL TICKET
if area == "software" and gravedad == "alta":
    print("Ticket: Prioridad critica. Escalar a desarrolladores senior. ")
elif area == "software" and gravedad == "media":
    print("Ticket: Prioridad alta. Resolver en menos de 24 horas.")
elif area == "hardware" and gravedad == "alta":
    print("Ticket: Prioridad crítica. Enviar equipo de reparación.")
elif area == "hardware" and gravedad == "media":
    print("Ticket: Prioridad alta. Evaluación remota.")
elif area == "red" and gravedad == "alta":
    print("Ticket: Prioridad critica. Escalar a administradores de red.")
elif area == "red" and gravedad == "media":print("Ticket: Prioridad alta. Diagnóstico inmediato.")
else:
    print ("Ticket: Prioridad normal. Programar revision en 48 horas.")