
MATCHSTICKS = 15 # Number of total mitch sticks in the game.    
GAMEROUND = 0 # number of times the game has played.
player_1 = input('The FIRST player,tell me your name...')
player_2 = input('The SECOND player,tell me your name...')

while MATCHSTICKS >= 5:
    num = int(input('Please Take some Match Sticks Between 1 to 4 (NOM: {}): '
                    .format(MATCHSTICKS))) # input from player.
    MATCHSTICKS -= num
    GAMEROUND += 1
                        
win_message = '{} is Win'    
check =  lambda player : print(win_message.format(player_1) if (GAMEROUND % 2==0 and MATCHSTICKS % 2 == 0) 
                               else print(win_message.format(player_2)))
winner = check(GAMEROUND)
