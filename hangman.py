from words import palabras
import random 

print("Bienvenido al juego del ahorcado")

def get_valid_word(palabras):
    word = random.choice(palabras)

    #Escoger una palabra
    while '-' in word or ' ' in word:
        word = random.choice(palabras)

    return word

print(get_valid_word(palabras))

#hidden_word = set()
#recorre la palabra
#for letter in get_valid_word(palabras)
#print(letter)

#Una función que despliegue los guinos
#dependiendo del tamaño de la palabra
my_word =get_valid_word(palabras)
print(my_word + '\n', len(my_word))


#mi_palabra = get_valid_palabra(palabras)
#espacios_vacios = ' _ ' * len(mi_palabra)
#print(espacios_vacios)
var2 = len(my_word)
i = 0
d = ''
while i < var2:
    i = i + 1
    d = d + "-"
print(d)