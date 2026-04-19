# Jorge Soria Ortiz
edad = int(input("Edad: "))
tiene_credencial = input("¿Tienes credencial? (si/no): ")

if edad >= 18 and tiene_credencial == "si":
    print("Puedes entrar")
elif edad < 18 or tiene_credencial == "no":
    print("No puedes entrar")
