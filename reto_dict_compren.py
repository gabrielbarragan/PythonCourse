def run():

    new_dict={f'{i}':i**(1/2) for i in range(0,1001)}
    print(new_dict)

if __name__=='__main__':
    run()