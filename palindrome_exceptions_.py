def palindrome(name):
    try:
        if len(name)==0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return name.lower() == name[::-1].lower()
    except ValueError as VE:
        print(VE)
        return False

name=input("Ingrese un nombre para validar si es un palindromo: ")
try:
    print(palindrome(name))
except TypeError:
    print('Solo se pueden validar strings')
except AttributeError:
    print('Solo se pueden validar cadenas de textos sin números')  
