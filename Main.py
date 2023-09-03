# Piedra Papel Tijera
import random #importación de modulo de aleatoriedad

round_selection = int(input('Cuantos Rounds? '))
rounds = 0

user_w = 0
comp_w = 0

while rounds < round_selection:

    if user_w > round_selection/2 or comp_w > round_selection/2: # Prediction
        rounds == round_selection
        break

    selection = ('piedra','papel','tijera')

    print('....................................................................................')
    print(f'SCORE: User: {user_w} --- --- CPU: {comp_w}  || Round: {rounds}/{round_selection}')
    user = input('Piedra - Papel - Tijera ===> ')
    comp = random.choice(selection)

    user = user.lower()
    comp = comp.lower()

    if user == 'piedra' or user == 'papel' or user == 'tijera':
        print('...........Results...........')
        print('-- User => ', user.upper())
        print('-- CPU => ', comp.upper())
        rounds += 1

    if user == comp:
        print('==========================================================> Empate')
    elif user == 'piedra':
        if comp == 'tijera':
            print('==========================================================> User gana')
            user_w += 1
        else:
            print('===========================================================> CPU gana')
            comp_w +=1

    elif user == 'papel':
        if comp == 'piedra':
            print('==========================================================> User gana')
            user_w += 1
        else:
            print('==========================================================> CPU gana')
            comp_w +=1

    elif user == 'tijera':
        if comp == 'papel':
            print('==========================================================> User gana')
            user_w += 1
        else:
            print('==========================================================> CPU gana')
            comp_w +=1
    else:
        print('Invalid User Input')
        continue

print('----------------------------------------------------------------------------------------')
print(' ')

if rounds == round_selection:
    if user_w > comp_w:
        print('<=======================> Victoria de User <=======================> ')
    elif comp_w > user_w:
        print('<=======================> Victoria CPU <=======================> ')
    else:
        print('<=================================================> EMPATE <=================================================> ')

print(' ')
print('----------------------------------------------------------------------------------------')
