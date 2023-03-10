import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    
    user_option = input('Ingresa tu opci贸n: ').lower()
    
    if not user_option in options:
        print ('Oh, esa opci贸n no es v谩lida')
        print('')
        return None, None
    
    computer_option = random.choice(options)
    
    print('Has elejido:', user_option.capitalize())
    print('El computador ha elejido:', computer_option.capitalize())

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if (user_option == computer_option):
        print('Empate 馃憖')
    elif (user_option == 'piedra'):
        if (computer_option == 'tijera'):
            print('Piedra gana a Tijera')
            print('隆Ganaste! 馃帀馃帀')
            user_wins += 1
        else:
            print('Papel gana a Piedra')
            print('El computador gan贸 馃捇馃帀')
            computer_wins += 1
    elif (user_option == 'papel'):
        if (computer_option == 'piedra'):
            print('Papel gana a Piedra')
            print('隆Ganaste! 馃帀馃帀')
            user_wins += 1
        else:
            print('Tijera gana a Papel')
            print('El computador gan贸 馃捇馃帀')
            computer_wins += 1
    elif (user_option == 'tijera'):
        if (computer_option == 'papel'):
            print('Tijera gana a Papel')
            print('隆Ganaste! 馃帀馃帀')
            user_wins += 1
        else:
            print('Piedra gana a Tijera')
            print('El computador gan贸 馃捇馃帀')
            computer_wins += 1

    return user_wins, computer_wins

def check_victory(user_wins, computer_wins):
    if user_wins == 2:
        print('Ganador: Usuario 馃懇馃懆 ')
        return False
        
    if computer_wins == 2:
        print('Ganador: Computador 馃捇')
        return False

    return True

def run_game():
    print('隆Piedra鉁?, Papel鉁? o Tijera鉁?!')
    print('')
    
    rounds = 1
    user_wins = 0
    computer_wins = 0
    on_going = True
    
    while on_going:
        print('*' * 10)
        print('RONDA', rounds)
        print('*' * 10)
    
        print('Marcador:')
        print('Victorias del usuario:', user_wins)
        print('Victorias del computador:', computer_wins)
    
        print('')
    
        user_option, computer_option = choose_options()

        if(user_option == None and computer_option == None):
            continue
    
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
    
        print('')

        on_going = check_victory(user_wins, computer_wins)
    
        rounds += 1

run_game()