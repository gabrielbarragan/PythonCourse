def divisors(num):
    # sin list comprehensions
    divisors=[]
    for i in range(1,num+1):
        if num % i ==0:
            divisors.append(i)
    return divisors


def run():

    number=input("Ingresa un número:")
    #es un método de las cadenas de caracteres
    print(number.isnumeric())
    assert number.isnumeric(), "Debes ingresar un número y debe ser positivo"
    print(divisors(int(number)))
    print('Programa Terminado')




if __name__=='__main__':
    run()