# Piedra Papel Tijera
import random #importación de modulo de aleatoriedad

round_selection = int(input('Cuantos Rounds? '))
rounds = 0

while rounds < round_selection:
    selection = ('piedra','papel','tijera')

    user = input('Piedra, Papel o Tijera? => ')
    comp = random.choice(selection)

    user = user.lower()
    comp = comp.lower()

    user_w = 0
    comp_w = 0

    if user == 'piedra' or user == 'papel' or user == 'tijera':
        print('-- -- -- -- --')
        print('User Selection => ', user)
        print('Computer Selection => ', comp)
        rounds += 1
        print('-- -- -- -- --')

    print(f"Round {rounds}/{round_selection}")
    if user == comp:
        print('========================> Empate')
    elif user == 'piedra':
        if comp == 'tijera':
            print('========================> User gana')
            user_w += 1
        else:
            print('========================> CPU gana')
            comp_w +=1

    elif user == 'papel':
        if comp == 'piedra':
            print('========================> User gana')
            user_w += 1
        else:
            print('========================> CPU gana')
            comp_w +=1

    elif user == 'tijera':
        if comp == 'papel':
            print('========================> User gana')
            user_w += 1
        else:
            print('========================> CPU gana')
            comp_w +=1
    else:
        print('Invalid User Input')
        continue

if rounds == round_selection:
    if user_w > comp_w:
        print('Victoria de User')
    elif user_w < comp_w:
        print('Victoria CPU')
    else:
        print('EMPATE')