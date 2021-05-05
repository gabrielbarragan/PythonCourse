def divisors(num):
    #sin list comprehensions
    # divisors=[]
    # for i in range(1,num+1):
    #     if num % i ==0:
    #         divisors.append(i)
    # return divisors

    #con list comprehensions
    try:
        if num<=0:
            raise ValueError('Debes ingresar solo números positivos')
        else:
            divis=[i for i in range(1,num+1) if num % i == 0]
            return divis
    except ValueError as VE:
        print(VE)
        return f'{num} no es un número positivo'

def run():
    try:
        number=int(input("Ingresa un número:"))
        print(divisors(number))
        print('Programa Terminado')
    except ValueError:
        print('Debes ingresar un número')



if __name__=='__main__':
    run()