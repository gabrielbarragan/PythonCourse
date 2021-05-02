def run():
    #imprimir el cuadrado de los primeros 100 números naturales que no sean divisibles en 3
    #método 1
    squares=[]
    for i in range(0,101):
        if i%3 != 0:
            squares.append(i**2)
        else:
            pass
    # print(squares)
    #método 2
    squrs= [i**2 for i in range(0,101) if i%3 != 0]
    print(squrs)
if __name__=='__main__':
    run()