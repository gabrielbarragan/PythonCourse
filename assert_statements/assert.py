def palindrome(name):
    assert len(name) > 0, "No se puede ingresar una cadena vacía"
    return name == name[::-1]  

print(palindrome("")) 
