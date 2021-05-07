import sys
def render_screen():
    HANGMAN=['''
 ||||||||||||||||||||||
   |||||||||||||||||''',
   '''
      |||||||||||
        |||||||
          |||''',
           '''
           |
           |
           |
           ''',
           ''' 
         |||||
         || ||
         |||||
           ''',
           '''
           |
        |||||||
       ||  |  ||
           ''',
           '''
           |
           |
           ''',
           '''
          |||
         || ||
       |||   |||
           ''']
    ahorcado=[' ']
    contador=len(ahorcado)+1
    for i in range(0,1):
        if contador<=6:
            ahorcado=ahorcado.append(HANGMAN[i])
        else:
            ahorcado=HANGMAN
    return ahorcado

def run():
    print(render_screen())


if __name__=='__main__':
    run()