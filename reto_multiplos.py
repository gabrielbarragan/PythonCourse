def run():
    #crear todos los multiplos de 4 que a su vez son multiplos de 6 y de 9 hasta 5 cifras
    mult= [i for i in range(1,100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]
    print(mult)
if __name__=='__main__':
    run()