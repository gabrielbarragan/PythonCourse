def run():
    # mi_dict={}
    # for i in range (1,101):
    #     mi_dict[str(i)]=i**3
    # print(mi_dict)

    #dictionary comprenhensions
    new_dict={str(i):i**3 for i in range(0,101) if i%3 != 0}
    print(new_dict)

if __name__=='__main__':
    run()