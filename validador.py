def validar_contraseña(contraseña):
 
    longitud_minima = 8
    caracteres_especiales = "!@#$%^&*"
    
    
    if len(contraseña) < longitud_minima:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    
    
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False

   
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif caracter in caracteres_especiales:
            tiene_especial = True
    
 
    if not tiene_mayuscula:
        print("La contraseña debe tener al menos una letra mayúscula.")
    if not tiene_minuscula:
        print("La contraseña debe tener al menos una letra minúscula.")
    if not tiene_numero:
        print("La contraseña debe tener al menos un número.")
    if not tiene_especial:
        print("La contraseña debe tener al menos un carácter especial (!@#$%^&*).")
    

    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True
    else:
        return False


contraseña = input("Ingresa una contraseña: ")


if validar_contraseña(contraseña):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")