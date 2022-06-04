
from ast import MatchStar


MATCHSTICKS = 15 # Number of total mitch sticks in the game.    
GAMEROUND = 1 # number of times the game has played.
player1_score =0
player2_score=0

player_1 = input('The FIRST player,tell me your name...')
player_2 = input('The SECOND player,tell me your name...')

for item in range(5):   
    while MATCHSTICKS >= 5:
        if GAMEROUND % 2 == 0: player_name = player_2
        else : player_name = player_1 

        num = int(input('Please Take some Match Sticks Between 1 to 4 (Turn: {0} / NOM: {1}): '
                        .format(player_name,MATCHSTICKS))) # input from player.
        MATCHSTICKS -= num
        GAMEROUND += 1
    
    # find winner                        
    if GAMEROUND % 2==0 and MATCHSTICKS % 2 == 0:
        print(F'{player_2} is WIN!')
        player2_score += 1
    else:
        print(F'{player_1} is WIN!')
        player1_score += 1        

    MATCHSTICKS = 15 # Reset repository for a new round
    GAMEROUND = 1 # reset game round
    print('try againfor a new round ...')
    
print(F'{player_1} Score is: ',player1_score + 'VS' + F'{player_2} Score is: ',player2_score)