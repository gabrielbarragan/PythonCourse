import random, os
def render_screen():
            template = """
        ============================================
**  **    ***    **   **  *******   **      **    ***    **   **  
**  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
******   *****   **** **  **  ***   ****  ****   *****   **** **  
**  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
**  **  **   **  **  ***  *******   **  **  **  **   **  **  ***  
        ============================================

        """
            return template
def read():
    """read a file 
    no parameters
    returns text in file
    """
    with open("././project/ahorcado/data.txt","r",encoding="utf-8") as f: 
        palabras=[line for index, line in enumerate(f)]
    return palabras

def choose_word():
    """choose a word in a file
    no parameters
    returns a word in ramdom line of file
    """
    words=read()
    aleatorio=random.randint(0,170)
    choose=words[aleatorio].replace("\n","")
    print(choose)
    return choose

def incoming_word():
    """receive a letter from user 
    no parameters
    returns a letter input by user
    """

    letter_input=input('Por favor dime una letra: ')
    return letter_input

def create_blank(word):
    """create a list with characters '_' del tamaño de word
    word is a string
    returns a list del tamaño de word con el caracter '_'
    """
    word_blank=['_' for i in range(0,len(word))]
    word_h=''
    for i in word_blank:
        word_h+=f'{i} '
    return word_blank

def encontrando_letra(letra,word):
    a,b='áéíóú','aeiou'
    sintilde=str.maketrans(a,b)
    word=word.translate(sintilde)
    if letra in word:
        search= word.index(letra)
        posiciones=[i for i in range(0,len(word)) if letra==word[i]]
    else:
        posiciones=[]
    return posiciones

def validar_letra(letra,word_blank,word,posiciones):
    for i in posiciones:
        word_blank[i]=letra
    return word_blank           

def validar_palabra(word):
    if word.count("_")!=0:
        return True
    else:
        return False


def reescribir_palabra(list_letter):
    word=""
    for letter in list_letter:
        word+=f'{letter} '
    return word

def run():

    try:
        palabra=choose_word()
        word_list=create_blank(palabra)
        puntaje=0
        os.system("clear")
        while validar_palabra(word_list):
            print(render_screen())
            print(reescribir_palabra(word_list))
            letra=incoming_word()
            posiciones=encontrando_letra(letra, palabra)
            if len(posiciones)>=1 and len(posiciones) <=2:
                puntaje+=2
            elif len(posiciones) >= 3:
                puntaje+=3
            else:
                pass
            word_list=validar_letra(letra,word_list,palabra,posiciones)
            os.system("clear")
            # print(reescribir_palabra(word_list))
            # print(puntaje)
        print(render_screen())
        print(reescribir_palabra(word_list))
        print(f'\nTu puntaje fue {puntaje}')
    except KeyboardInterrupt:
        os.system("clear")
        print(render_screen())
        print(reescribir_palabra(word_list))
        print('\n\nAbandonaste el juego, ¡suerte!')
        print(f'\nTu puntaje fue {puntaje}')

    

if __name__ == '__main__':
    run()