def run():
    my_list=[1, "hello", True, 4.5]
    my_dict={
     'firstname':'Facundo',
     'lastname':'García'
    }

    super_list=[
        {'firstname':'Facundo','lastname':'García'},
        {'firstname':'Juan','lastname':'García'},
        {'firstname':'Yolanda','lastname':'García'},
        {'firstname':'Mercedes','lastname':'García'}
    ]
    super_dict= {
        'natura_lnums':[1, 2, 3, 4, 5],
        'integer_nums':[-1,-2,0,4,2],
        'floating_nums':[2.3, 4.5, -20.3, 0.2]
    }
    
    for key, value in super_dict.items():
        print(key,"- ",value)
    for valor in super_list:
        for group, val in valor.items():
            print(f'{group} {val}')

if __name__== '__main__':
    run()