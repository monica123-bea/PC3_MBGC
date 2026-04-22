# Mónica García
# EJERCICIO 10

# SOLICITAMOS EL NOMBRE DEL EMPLEADO
nombre = input("Introduce tu nombre: ")

# SOLICITAMOS LA CANTIDAD DE PROYECTOS COMPLETADOS
proyectos = int(input("¿Cuantos proyectos completaste este año?"))

# SOLICITAMOS LA CANTIDAD DE CURSOS COMPLETADOS
cursos = int(input("¿Cuantos cursos de formacion completaste este año? "))

# SOLICITAMOS SI RECIBIO ALGUN RECONOCIMIENTO
reconocimiento = input("¿Recibiste un reconocimiento oficial? (si/no): ") . lower()

# EVALUAMOS SI CUMPLE CON LOS REQUISITOS DEL BONO MÁXIMO
if proyectos >= 5 and cursos >= 3 and reconocimiento == "si":
    print (nombre, ", ¡Felicidades! Eres elegible para el bono máximo. ")
# EVALUAMOS SI CUMPLE PARA UN BONO ESTANDAR
elif proyectos >= 3 and cursos >= 2:
    print (nombre, ", Eres elegible para un bono estándar.")
# EVALUAMOS SI AL MENOS COMPLETO UN PROYECTO
elif proyectos >= 1:
    print (nombre, ", Recibirás un bono de participación.")
# SI NO CUMPLE CON NINGUNO
else:
    print(nombre, ", No calificas para bono este año. ¡Ánimo para la próxima!")