import time
import os
import random
import sys

def menu():
    """[Menu inicial del juego, aca arranca el programa]
    """    

    os.system('cls')

    print('Menu: ')
    print('-----')
    print('1. Palabras Random(cualquier palabra).')
    print('2. Tematica Futbol(jugadores de futbol).')
    print('3. Tematica Comida(comidas xd).')
    print('4. Salir(no seas trolo man).')
    print('------------------------------')
    print()
    
    try:

        eleccion = int(input('Ingrese la opcion deseada: '))

        if eleccion < 1 or eleccion > 4:

            error()
    
    except ValueError:
        
        error()

    if eleccion != 4:

        return eleccion
    
    else:

        print()
        print('Fin del programa.')
        sys.exit()


def error():

    #Funcion utilizada en la funcion menu, para evitar errores de usuario
            
        print()
        print('Error! Ingrese una opcion valida (1,2,3 o 4)')
        print
        time.sleep(1)
        print('Reiniciando el programa, por favor espere!')
        print('...')
        time.sleep(0.5)
        print('..')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print()
        print('El programa se ha reiniciado con exito!')
        time.sleep(1)
        menu()


def word_generator(n):

    word_number = random.randint(0,19)

    words1 = [
        'celular','computadora','teclado','salud','acido','camion','auto','paciencia','pilas','cumbia','bala','goma','borrador','ejemplo',
        'tiburon','cocodrilo','vaca','calle','tatuaje','corona'
        ]

    words2 = [
        'messi','ronaldo','dybala','pogba','maradona','ndombele','ribery','pulisic','griezmann','coleman','ramos','degea','son',
        'reus','rodirugez','neymar','fati','vinicius','rodri','casillas'
    ]

    words3 = [
        'papa','bife','choclo','galleta','manteca','zanahoria','zapallo','palta','arroz','frutilla','manzana','banana','pera',
        'sandia','uvas','chocolate','pepino','pizza','kiwi','jamon'
    ]

    print(words1[word_number],words2[word_number],words3[word_number])

    if n == 1:

        return words1[word_number]
    
    elif n == 2:

        return words2[word_number]
    
    else:

        return words3[word_number]


def checkeo(word,letter):

    if letter in word:
                
        print(f'La letra {letter} se encontraba en la palabra!')
        time.sleep(1.5)

        return True
    
    else:

        print(f'La letra {letter} no se encontraba en la palabra!')
        time.sleep(1.5)

        return False


def display():

    wrong = 0
    wrong_letters = []
    used_letters = []

    end = False

    word = word_generator(menu())
    encrypted_word = '-' * len(word)
    
    IMAGES = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    while end == False:

        if wrong == 0:

            print(IMAGES[0])
            print()
            print(encrypted_word)
            print()
            print(f'Letras usadas: {used_letters}')
            print()
            letter = input('Ingrese la letra que desea probar: ')
            print()

            while letter in used_letters:

                print('Error! esta letra se encuentra entre las ya utilizadas, intenta con otra!')
                print()
                letter = input('Ingrese la letra que desea probar: ')

            used_letters.append(letter)
            print()
            answer = checkeo(word,letter)

            if answer == False:

                wrong += 1
                wrong_letters.append(letter)
            
            else:

                #indexing the word
                for i in range(len(word)):

                    if word[i] == letter:
                        
                        encrypted_list = list(encrypted_word)
                        encrypted_list[i] = letter

                        encrypted_word = "".join(encrypted_list)

            if encrypted_word == word:

                end = True
                print()
                print('Felicitaciones, has encontrado la palabra!')
                print(f'Palabra: {word}')
                print()
            
        if wrong == 1:

            print(IMAGES[1])
            print()
            print(encrypted_word)
            print()
            print(f'Letras usadas: {used_letters}')
            print()
            letter = input('Ingrese la letra que desea probar: ')
            print()

            while letter in used_letters:

                print('Error! esta letra se encuentra entre las ya utilizadas, intenta con otra!')
                print()
                letter = input('Ingrese la letra que desea probar: ')

            used_letters.append(letter)
            print()
            answer = checkeo(word,letter)

            if answer == False:

                wrong += 1
                wrong_letters.append(letter)
            
            else:

                #indexing the word
                for i in range(len(word)):

                    if word[i] == letter:
                        
                        encrypted_list = list(encrypted_word)
                        encrypted_list[i] = letter

                        encrypted_word = "".join(encrypted_list)

            if encrypted_word == word:

                end = True
                print()
                print('Felicitaciones, has encontrado la palabra!')
                print(f'Palabra: {word}')
                print()

        if wrong == 2:

            print(IMAGES[2])
            print()
            print(encrypted_word)
            print()
            print(f'Letras usadas: {used_letters}')
            print()
            letter = input('Ingrese la letra que desea probar: ')
            print()

            while letter in used_letters:

                print('Error! esta letra se encuentra entre las ya utilizadas, intenta con otra!')
                print()
                letter = input('Ingrese la letra que desea probar: ')

            used_letters.append(letter)
            print()
            answer = checkeo(word,letter)

            if answer == False:

                wrong += 1
                wrong_letters.append(letter)
            
            else:

                #indexing the word
                for i in range(len(word)):

                    if word[i] == letter:
                        
                        encrypted_list = list(encrypted_word)
                        encrypted_list[i] = letter

                        encrypted_word = "".join(encrypted_list)

            if encrypted_word == word:

                end = True
                print()
                print('Felicitaciones, has encontrado la palabra!')
                print(f'Palabra: {word}')
                print()
                     
        if wrong == 3:

            print(IMAGES[3])
            print()
            print(encrypted_word)
            print()
            print(f'Letras usadas: {used_letters}')
            print()
            letter = input('Ingrese la letra que desea probar: ')
            print()

            while letter in used_letters:

                print('Error! esta letra se encuentra entre las ya utilizadas, intenta con otra!')
                print()
                letter = input('Ingrese la letra que desea probar: ')

            used_letters.append(letter)
            print()
            answer = checkeo(word,letter)

            if answer == False:

                wrong += 1
                wrong_letters.append(letter)
            
            else:

                #indexing the word
                for i in range(len(word)):

                    if word[i] == letter:
                        
                        encrypted_list = list(encrypted_word)
                        encrypted_list[i] = letter

                        encrypted_word = "".join(encrypted_list)

            if encrypted_word == word:

                end = True
                print()
                print('Felicitaciones, has encontrado la palabra!')
                print(f'Palabra: {word}')
                print()
        
        if wrong == 4:

            print(IMAGES[4])
            print()
            print(encrypted_word)
            print()
            print(f'Letras usadas: {used_letters}')
            print()
            letter = input('Ingrese la letra que desea probar: ')
            print()

            while letter in used_letters:

                print('Error! esta letra se encuentra entre las ya utilizadas, intenta con otra!')
                print()
                letter = input('Ingrese la letra que desea probar: ')

            used_letters.append(letter)
            print()
            answer = checkeo(word,letter)

            if answer == False:

                wrong += 1
                wrong_letters.append(letter)
            
            else:

                #indexing the word
                for i in range(len(word)):

                    if word[i] == letter:
                        
                        encrypted_list = list(encrypted_word)
                        encrypted_list[i] = letter

                        encrypted_word = "".join(encrypted_list)

            if encrypted_word == word:

                end = True
                print()
                print('Felicitaciones, has encontrado la palabra!')
                print(f'Palabra: {word}')
                print()
        
        if wrong == 5:

            print(IMAGES[5])
            print()
            print(encrypted_word)
            print()
            print(f'Letras usadas: {used_letters}')
            print()
            letter = input('Ingrese la letra que desea probar: ')
            print()

            while letter in used_letters:

                print('Error! esta letra se encuentra entre las ya utilizadas, intenta con otra!')
                print()
                letter = input('Ingrese la letra que desea probar: ')

            used_letters.append(letter)
            print()
            answer = checkeo(word,letter)

            if answer == False:

                wrong += 1
                wrong_letters.append(letter)
            
            else:

                #indexing the word
                for i in range(len(word)):

                    if word[i] == letter:
                        
                        encrypted_list = list(encrypted_word)
                        encrypted_list[i] = letter

                        encrypted_word = "".join(encrypted_list)

            if encrypted_word == word:

                end = True
                print()
                print('Felicitaciones, has encontrado la palabra!')
                print(f'Palabra: {word}')
                print()

        if wrong == 6:

            print(IMAGES[6])
            print()
            print(encrypted_word)
            print()
            print(f'Letras usadas: {used_letters}')
            print()
            letter = input('Ingrese la letra que desea probar: ')
            print()

            while letter in used_letters:

                print('Error! esta letra se encuentra entre las ya utilizadas, intenta con otra!')
                print()
                letter = input('Ingrese la letra que desea probar: ')

            used_letters.append(letter)
            print()
            answer = checkeo(word,letter)

            if answer == False:

                wrong += 1
                wrong_letters.append(letter)
            
            else:

                #indexing the word
                for i in range(len(word)):

                    if word[i] == letter:
                        
                        encrypted_list = list(encrypted_word)
                        encrypted_list[i] = letter

                        encrypted_word = "".join(encrypted_list)

            if encrypted_word == word:

                end = True
                print()
                print('Felicitaciones, has encontrado la palabra!')
                print(f'Palabra: {word}')
                print()
            
            else:

                end = True
                print()
                print('No has encontrado la palabra :(')
                print(f'La palabra era {word}')

#Bloque principal

display()