# Mónica García
# EJERCICIO 8

# SOLICITAMOS LA CONTRASEÑA
contraseña = input("Introduce una contraseña para evaluación: ")

# CALCULAMOS LA LONGITUD DE LA CONTRASEÑA
longitud = len(contraseña)

# VERIFICAMOS SI CONTIENE NÚMEROS
contiene_numeros = any(char.isdigit() for char in contraseña)

# VERIFICAMOS SI CONTIENE MAYUSCULAS
contiene_mayusculas = any(char.isupper() for char in contraseña)

# EVALUAMOS LA SEGURIDAD DE LA CONTRASEÑA
if longitud >= 12 and contiene_numeros and contiene_mayusculas:
    print("Contraseña fuerte. ")
elif longitud >= 8 and (contiene_numeros or contiene_mayusculas):
    print("Contraseña moderada. Recomendado mejorar. ")
else:
    print("Contraseña debil. Cambiar inmediatamente. ")

# MOSTRAMOS DATALLES
print("Longitud de la contraseña", longitud)
print("¿Contiene numeros?", contiene_numeros)
print("¿Contiene mayusculas?", contiene_mayusculas)