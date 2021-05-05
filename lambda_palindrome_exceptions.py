name=input("Ingrese un nombre para validar si es un palindromo: ")
palindrome= lambda nombre: nombre.lower()==nombre[::-1].lower()



try:
    print(palindrome(name))
except TypeError:
    print('Solo se pueden validar strings')
except AttributeError:
    print('Solo se pueden validar cadenas de textos sin números')  
