# Mónica García
# EJERCICIO 7

# CONDICIONALES EN PYTHON
# SOLICITAMOS LOS AÑOS DE EXPERIENCIA
anios_experiencia = int(input("Introduce tus años de experiencia en programacion: "))

# SOLICITAMOS EL TIPO DE TECNOLOGIA PREFERIDA
tecnologia = input("¿Prefieres trabajar en (backend/frontend/fullstack)? ").lower()

# EVALUAMOS SI EL DESARROLLADOR ES SENIOR (5 AÑOS O MAS)
if anios_experiencia >= 5:
    senior = True
else:
    senior = False
# EVALUAMOS LA TECNOLOGIA Y LA EXPERIENCIA PARA ASIGNAR PROYECTO
if tecnologia == "backend" and senior:
    print("Proyecto asignado: Microservicios para banca digital.")
elif tecnologia == "frontend" and senior:
    print("Proyecto asignado: Plataforma de ventas en tiempo real")
elif tecnologia == "fullstack" and senior:
        print("Proyecto asignado: Sistema ERP completo.")
elif tecnologia == "backend" and not senior:
    print("Proyecto asignado: APIs básicas para e-commerce")
elif tecnologia == "frontend" and not senior:
    print("Proyecto asignado: Diseño de landing pages.")
elif tecnologia == "fullstack" and not senior:
    print ("Proyecto asignado: Modulo de autenticacion de usuarios.")
else:
    print("Error: Tecnologia ingresada no reconocida.")