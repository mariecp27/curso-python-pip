import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    
    user_option = input('Ingresa tu opción: ').lower()
    
    if not user_option in options:
        print ('Oh, esa opción no es válida')
        print('')
        return None, None
    
    computer_option = random.choice(options)
    
    print('Has elejido:', user_option.capitalize())
    print('El computador ha elejido:', computer_option.capitalize())

    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if (user_option == computer_option):
        print('Empate 👀')
    elif (user_option == 'piedra'):
        if (computer_option == 'tijera'):
            print('Piedra gana a Tijera')
            print('¡Ganaste! 🎉🎉')
            user_wins += 1
        else:
            print('Papel gana a Piedra')
            print('El computador ganó 💻🎉')
            computer_wins += 1
    elif (user_option == 'papel'):
        if (computer_option == 'piedra'):
            print('Papel gana a Piedra')
            print('¡Ganaste! 🎉🎉')
            user_wins += 1
        else:
            print('Tijera gana a Papel')
            print('El computador ganó 💻🎉')
            computer_wins += 1
    elif (user_option == 'tijera'):
        if (computer_option == 'papel'):
            print('Tijera gana a Papel')
            print('¡Ganaste! 🎉🎉')
            user_wins += 1
        else:
            print('Piedra gana a Tijera')
            print('El computador ganó 💻🎉')
            computer_wins += 1

    return user_wins, computer_wins

def check_victory(user_wins, computer_wins):
    if user_wins == 2:
        print('Ganador: Usuario 👩👨 ')
        return False
        
    if computer_wins == 2:
        print('Ganador: Computador 💻')
        return False

    return True

def run_game():
    print('¡Piedra✊, Papel✋ o Tijera✌!')
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