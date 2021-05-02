def run():
    #imprimir el cuadrado de los primeros 100 números naturales
    #método 1
    squares=[]
    for i in range(0,101):
        squares.append(i**2)
    print(squares)
    print('--------------------------------------')
    #método 2
    natural_nums= [numero**2 for numero in range(0,101)]
    print (natural_nums)

    if squares==natural_nums:
        print(id(squares))
        print(id(natural_nums))
        print('iguales')
    else:
        print('diferentes')


if __name__=='__main__':
    run()