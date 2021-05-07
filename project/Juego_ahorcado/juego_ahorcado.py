import random, os, sys
def render_screen():
    """Create initial banner for windows or linux.
    returns a string with banner in ascii code.
    """

    if sys.platform.startswith('linux'):
        template = """
        ************************************************

$$\   $$\                                                                 
$$ |  $$ |                                                                
$$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  $$$$$$$\  
$$$$$$$$ | \____$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ 
$$  __$$ | $$$$$$$ |$$ |  $$ |$$ /  $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  $$ |
$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$  __$$ |$$ |  $$ |
$$ |  $$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$ |$$ |  $$ |
\__|  \__| \_______|\__|  \__| \____$$ |\__| \__| \__| \_______|\__|  \__|
                              $$\   $$ |                                  
                              \$$$$$$  |                                  
                               \______/                                   
                        
                        by: Gabriel Rondón Barragán
 ----------------------
|press ctrl+c for exit|
 ----------------------
        =================================================   
        """
    elif sys.platform.startswith('win32'):
        template = """
        ************************************************
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░█░░░█░░█████░░██████░░██████░███████░░░██████░░░░██████░░░░░░
░░░░░█░░░█░░░░░░█░░█░░░░█░░█░░░░░░█░░█░░█░░░░░░░░█░░░░█░░░░█░░░░░░
░░░░░█░░░█░░░░░░█░░█░░░░█░░█░░░░░░█░░█░░█░░░░░░░░█░░░░█░░░░█░░░░░░
░░░░░█████░░█████░░█░░░░█░░██████░█░░█░░█░░░██████░░░░█░░░░█░░░░░░
░░░░░█░░░█░░█░░░█░░█░░░░█░░█░░░░█░█░░█░░█░░░█░░░░█░░░░█░░░░█░░░░░░
░░░░░█░░░█░░█░░░█░░█░░░░█░░█░░░░█░█░░█░░█░░░█░░░░█░░░░█░░░░█░░░░░░
░░░░░█░░░█░░██████░█░░░░█░░██████░█░░█░░█░░░████████░░█░░░░█░░░░░░

                        by: Gabriel Rondón Barragán
 ----------------------
|press ctrl+c for exit|
 ----------------------
        ================================================   
        """
    return template

def read():
    """read a file 
    no parameters
    returns text in file, if file doesn't existe create it.
    """
    try:
        with open("./data_es.txt","r",encoding="utf-8") as f: 
            palabras=[line for index, line in enumerate(f)]
        return palabras
    except (TypeError, NameError, SyntaxError, FileNotFoundError):
        print(f"Error: Can't find the file named 'data / no se pudo encontrar el archivo data.txt...\nWe are restoring the file, please wait... /Lo estamos creando Por favor espera...\nTry access again /intenta ingresar nuevamente")
        restore_file()
        print("File restored!, ¡Archivo creado!")


def restore_file():
    palabras=['velociraptor', 'ganar', 'golpear', 'caramelos', 'espeso', 'esposo', 'ancho', 'lavanderia', 'babear', 'twitter', 'prisionera', 'indiferentemente', 'imaginar', 'reconocer', 'zodiaco', 'popular', 'sentado', 'seco', 'calcio', 'bomba', 'humano', 'grabador', 'pintura', 'cucaracha', 'abrazadera', 'espiral', 'embarazo', 'cueva', 'remolacha', 'satelite', 'bache', 'desenvolver', 'reprobar', 'dirigir', 'bateria', 'calzado', 'aplastar', 'moverse', 'murmurar', 'cancha', 'reina', 'claustrofobia', 'farmacia', 'ventana', 'estallido', 'terraza', 'desnudarse', 'retorcer', 'perfume', 'coleccion', 'torre', 'rata', 'vestuario', 'microondas', 'operacion', 'dichoso', 'aparatos', 'historiador', 'boleto', 'provincia', 'hormiga', 'flecha', 'lanzallamas', 'observatorio', 'ventilador', 'holanda', 'escenario', 'fotografiar', 'sismo', 'roto', 'fregadero', 'trineo', 'nuez', 'aletear', 'sintonizar', 'desviar', 'mayordomo', 'rianchuelo', 'museo', 'restaurante', 'mangas', 'magnetico', 'probar', 'regar', 'pelo', 'cuero', 'ascendiente', 'tanga', 'dinamarca', 'mariquita', 'circuito', 'veredicto', 'sinusitis', 'blusa', 'calendario', 'atracar', 'barranco', 'peste', 'asustar', 'untar', 'embudo', 'chicos', 'mantel', 'escribir', 'respirador', 'micro', 'cerebro', 'lastimar', 'colectivo', 'almendra', 'derecha', 'alarma', 'memoria', 'gente', 'punta', 'aperitivo', 'archivo', 'existente', 'capitulo', 'prima', 'desaparecido', 'sabor', 'estimar', 'arcano', 'vibora', 'capturado', 'lesion', 'auxiliar', 'desercion', 'completamente', 'doble', 'ayuda', 'mejor', 'labios', 'ardiente', 'alfabetico', 'cocinero', 'grunidos', 'sanguijuela', 'rojo', 'trebol', 'palanca', 'mando', 'vuelta', 'caracol', 'pueblo', 'besos', 'mision', 'fachada', 'destello', 'hiedra', 'ausencia', 'jefe', 'arma', 'fuego', 'perro', 'piezas', 'desesperacion', 'traicion', 'final', 'erupcion', 'absolucion', 'perezoso', 'surgir', 'franqueza', 'ahogo', 'diabolico', 'algunos', 'grava', 'abrazo', 'oriental', 'papi', 'emboscada', 'bolso', 'horrendo', 'aspero', 'subterraneo', 'secuestrado', 'coartada', 'imperio', 'enigma', 'ladron', 'homicidio', 'cena', 'piramides', 'atmosfera', 'caballos', 'caracteristica', 'carnicero', 'chocar', 'canela', 'cangilon', 'cincel', 'destruir', 'asombroso', 'brutalmente', 'grande', 'usable', 'sabiduria', 'cena', 'cuna', 'lamer', 'libertinaje', 'leyenda', 'picadillo', 'colina', 'bicicleta', 'zumbido', 'nudillos', 'continuo', 'faraon', 'granito', 'destileria', 'verdugo', 'traficante', 'temeroso', 'toro', 'desolado', 'repeticion', 'llave', 'gigantesco', 'flotar', 'dominante', 'duque', 'collar', 'chiflado', 'moda', 'robotico', 'exacto', 'corpulento', 'angustia', 'parachoque', 'atras', 'posicion', 'eliminacion', 'grabar', 'cera', 'huerta', 'bosque', 'medio', 'camino', 'corral', 'futuro', 'nuevo', 'animalista', 'devastacion', 'dulce', 'dinosaurio', 'locura', 'piedra', 'terror', 'cierto', 'arcilla', 'emitir', 'ciudad', 'nudo', 'caida', 'heroico', 'ataud', 'vida', 'definitivo', 'pobre', 'embriagante', 'pistola', 'rapido', 'natural', 'arriesgado', 'descripcion', 'terminar', 'sabotaje', 'escarcha', 'gases', 'lacrimogeno', 'rapido', 'tormenta', 'nieve', 'personal', 'sistema', 'objeto', 'feudal', 'talon', 'crema', 'cafe', 'estrella', 'explosion', 'guitarra', 'plastico', 'navaja', 'martillo', 'libros', 'lapiz', 'lapicera', 'aluminio', 'embarcacion', 'letra', 'agujeta', 'libreria', 'sonido', 'universidad', 'rueda', 'llaves', 'camisa', 'papa', 'sillon', 'felicidad', 'catre', 'teclado', 'servilleta', 'escuela', 'pantalla', 'codo', 'tenedor', 'estadistica', 'mapa', 'agua', 'mensaje', 'lima', 'cohete', 'edificio', 'cesped', 'presidencia', 'hojas', 'parlante', 'colegio', 'granizo', 'pestana', 'lampara', 'mano', 'monitor', 'flor', 'musica', 'hombre', 'tornillo', 'habitacion', 'velero', 'abuela', 'abuelo', 'palo', 'templo', 'lentes', 'boligrafo', 'plato', 'nube', 'gobierno', 'botella', 'castillo', 'enano', 'casa', 'libro', 'persona', 'planeta', 'televisor', 'guantes', 'metal', 'telefono', 'proyector', 'mono', 'remera', 'muela', 'petroleo', 'percha', 'remate', 'debate', 'anillo', 'cuaderno', 'ruido', 'pared', 'taladro', 'herramienta', 'cartas', 'chocolate', 'anteojos', 'impresora', 'living', 'luces', 'zapato', 'lluvia', 'corbata', 'periodico', 'diente', 'planta', 'chupetin', 'buzo', 'oficina', 'persiana', 'puerta', 'silla', 'ensalada', 'pradera', 'zoologico', 'candidato', 'deporte', 'recipiente', 'diarios', 'fotografia', 'hierro', 'refugio', 'pantalon', 'barco', 'carne', 'tecla', 'humedad', 'departamento', 'celular', 'tristeza', 'hipopotamo', 'sofa', 'cama', 'arbol', 'mesada', 'campera', 'discurso', 'auto', 'cinturon', 'rucula', 'famoso', 'madera', 'lentejas', 'piso', 'maletin', 'reloj', 'diputado', 'cuchillo', 'desodorante', 'candado', 'montanas', 'computadora', 'radio', 'mono', 'cuadro', 'calor', 'partido', 'teatro', 'fiesta', 'bala', 'auriculares']
    with open("./data_es.txt","w",encoding="utf-8") as f:
        for palabra in palabras:
            f.write(palabra)
            f.write("\n")
    
def choose_word():
    """choose a word in a file
    no parameters
    returns a word in ramdom line of file
    """
    words=read()
    aleatorio=random.randint(0,435)
    choose=words[aleatorio].replace("\n","")
    print(choose)
    return choose

def incoming_word():
    """launches an input for the user to enter a letter
    no parameters
    returns a input letter
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
    """find a letter in a word and transform special characters into vowels
    word is a string, letter is a string
    returns a list with the positions of letters in word
    """
    a,b='áéíóú','aeiou'
    sintilde=str.maketrans(a,b)
    word=word.translate(sintilde)
    if letra in word:
        search= word.index(letra)
        posiciones=[i for i in range(0,len(word)) if letra==word[i]]
    else:
        posiciones=[]
    return posiciones

def validar_letra(letra,word_blank,posiciones):
    """places the indicated letter in the desired position within a list
    word is a string, letter is a string
    returns a list with letters located in word
    """
    for i in posiciones:
        word_blank[i]=letra
    return word_blank           

def validar_palabra(word):
    """validate if the word was found 
    word is a string
    returns a True if wasn´t found or False if was found
    """
    if word.count("_")!=0:
        return True
    else:
        return False
def reescribir_palabra(list_letter):
    """rewrite word in screen with letter found 
    list_letter is a string
    returns a word in string
    """
    word=""
    for letter in list_letter:
        word+=f'{letter} '
    return word
def points_system(coincidencias,puntaje):
    """add a point for each hit
    coincidencia is a list
    return puntaje
    """
    if len(coincidencias)>=1:
                puntaje+=1
    else:
        puntaje-=1
        pass
    return puntaje
def run():
    read()
    try:
        palabra=choose_word()
        word_list=create_blank(palabra)
        puntaje=0
        try: os.system("clear")
        except:
            os.system("cls")
        while validar_palabra(word_list):
            print(render_screen())
            print(f'Tu puntaje es:                    {puntaje}')
            print(f'                              {reescribir_palabra(word_list)}')
            letra=incoming_word()
            posiciones=encontrando_letra(letra, palabra)
            puntaje=points_system(posiciones,puntaje)
            word_list=validar_letra(letra,word_list,posiciones)
            os.system("clear")
            # print(reescribir_palabra(word_list))
            
        print(render_screen())
        print(f'\nTu puntaje fue:                     {puntaje}')
        print(f'                              {reescribir_palabra(word_list)}') 

    except KeyboardInterrupt:
        os.system("clear")
        print(render_screen())
        print(reescribir_palabra(word_list))
        print('\n\nAbandonaste el juego, ¡suerte!')
        print(f'\nTu puntaje fue {puntaje}')

    

if __name__ == '__main__':
    run()