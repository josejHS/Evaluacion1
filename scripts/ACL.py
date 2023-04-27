# Solicita al usuario el número de ACL
numero_acl = input("Ingrese el número de ACL: ")

# Convierte el número de ACL a un entero
numero_acl = int(numero_acl)

# Determina si el número de ACL IPv4 es una ACL Estándar, Extendida o no corresponde a una lista de acceso
if numero_acl >= 1 and numero_acl <= 99:
    print("El número de ACL " + str(numero_acl) + " es una ACL Estándar.")
elif numero_acl >= 100 and numero_acl <= 199:
    print("El número de ACL " + str(numero_acl) + " es una ACL Extendida.")
else:
    print("El número de ACL " + str(numero_acl) + " no corresponde a una lista de acceso.")

