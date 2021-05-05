import random
def read():

    with open("././project/ahorcado/data.txt","r",encoding="utf-8") as f: 
        palabras=[line for index, line in enumerate(f)]
    return palabras

def choose_word():
    words=read()
    aleatorio=random.randint(0,170)
    choose=words[aleatorio].replace("\n","")
    print(choose)
    return choose

def incoming_word():
    letter_input=input('Por favor dime una letra: ')
    return letter_input

def validar_letra(word):
    letter=incoming_word()
    a,b='áéíóú','aeiou'
    sintilde=str.maketrans(a,b)
    word=word.translate(sintilde)
    word_blank=''
    for i in word:
        if i != letter:
            i='_ '
            word_blank+=i
        else:
            word_blank+=f'{i} '
    print(word_blank)
    
    # if letter in word:
    #     search= word.index(letter)
    #     print(search)
    #     posiciones=[i for i in range(0,len(word)) if letter==word[i]]
    #     print(posiciones)
    #     for i in posiciones:
    #         pass
    #         # print(letter)        
    # else:
    #     print('algo falló')
    

def validar_palabra():
    pass
def reescribir_palabra(letra):
    pass

def run():
    validar_letra(choose_word())


if __name__ == '__main__':
    run()