# Piedra Papel Tijera
import random #importación de modulo de aleatoriedad
rounds = 0

while rounds < 3:
    selection = ('piedra','papel','tijera')

    user = input('Piedra, Papel o Tijera? => ')
    comp = random.choice(selection)

    user = user.lower()
    comp = comp.lower()

    if user == 'piedra' or user == 'papel' or user == 'tijera':
        print('-- -- -- -- --')
        print('User Selection => ', user)
        print('Computer Selection => ', comp)
        rounds += 1
        print('-- -- -- -- --')

    if user == comp:
        print('Empate')
    elif user == 'piedra':
        if comp == 'tijera':
            print('User gana')
        else:
            print('CPU gana')

    elif user == 'papel':
        if comp == 'piedra':
            print('User gana')
        else:
            print('CPU gana')

    elif user == 'tijera':
        if comp == 'papel':
            print('User gana')
        else:
            print('CPU gana')
    else:
        print('Invalid User Input')
        break