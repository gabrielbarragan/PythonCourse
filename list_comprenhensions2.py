def run():
    fruits = ['papaya', 'banano', 'fresa', 'mora', 'limón']

    newfruits = ['naranja' if fruit == 'banano' else fruit for fruit in fruits]

    print(newfruits)
if __name__=='__main__':
    run()