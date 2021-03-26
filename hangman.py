from words import palabras
import random
from colorama import init, Fore
init(autoreset=True)


def get_valid_word():
    word = random.choice(palabras)
    return word.upper()
    
#intento fallido
#for i in [31,32,33,34,35,36]:
 #   print('\033[{i}m' + "Texto color rojo")


print(Fore.RED + get_valid_word())
mi_palabra = get_valid_word()
print(mi_palabra)
espacios_vacios = ' _ ' * len(mi_palabra)
print(espacios_vacios)
print('\033[31m' + "Texto color rojo")

def jugar(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 5
    print("Comenzemos a jugar!!!")
    print(desplegar_monito(tries))#Despliega el monito al principio
    print(word_completion)#Muestra en lo que cabe de la palabra
    print("\n")
    while not guessed and tries > 0:
        guess = input("Introduce una palabra o letra a adivinar: ").upper()
        #adivina una letra en especifico
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Tu adivinaste la letra ", guess)
            elif guess not in word:
                print(guess, " No esta en la palabra.")
                tries = tries - 1
                guessed_letters.append(guess)
            else:
                print("Muy bien, ", guess, "esta en la palabra")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        #compara toda la palabraaaaaa
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Adivinaste la palabra, ", guess)
            elif guess != word:
                print(guess, " no es la palabra.")
                tries = tries - 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("No es valido.")
        print(desplegar_monito(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Felicidades, ya tienes la palabra, salvaste al mendigo")
    else:
        print("Sorry, ya no tienes intentos, pero la palabra era " + word + " , suerte para la siguiente.")
    return word
#La neta profe, no pude poner el monito en el otro archivo porque me daba error, pero aquí lo dejo xd
def desplegar_monito(tries):
    stages = [ """
                    ---------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      / \
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      /
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |     
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      \|/
                    |       
                    |      
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      
                    |       
                    |      
                """,
                """
                    ---------
                    |       |
                    |       
                    |      
                    |      
                    |      
                """
    ]
    return stages[tries]

#Inicializa el juego
def main():
    word = get_valid_word()
    jugar(word)
    while input("Quieres jugar de nuevo? (Y/N) ").upper() == "Y":
        word = get_valid_word
        jugar(word)


if __name__ == "__main__":
    main()
#hidden_word = set()
#recorre la palabra
#for letter in get_valid_word(palabras)
#print(letter)

#Una función que despliegue los guinos
#dependiendo del tamaño de la palabra
#my_word =get_valid_word()
#print(my_word + '\n', len(my_word))


#mi_palabra = get_valid_palabra(palabras)
#espacios_vacios = ' _ ' * len(mi_palabra)
#print(espacios_vacios)
#my_word = get_valid_word
#var2 = len(my_word)
#i = 0
#d = ''
#while i < var2:
  #  i = i + 1
  #  d = d + "-"
#print(d)