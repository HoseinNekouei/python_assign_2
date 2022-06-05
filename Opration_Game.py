#Create by Hosein Nekouei

MATCHSTICKS = 15 # Number of total mitch sticks in the game.    
GAMEROUND = 1 # number of times the game has played.
player1_score =0
player2_score=0

player_1 = input('The FIRST player,tell me your name...')
player_2 = input('The SECOND player,tell me your name...')

for item in range(5):   
    
    print(F"Round: {GAMEROUND}") # Counter of Round
    while MATCHSTICKS >= 5:
        if GAMEROUND % 2 == 0: player_name = player_2
        else : player_name = player_1 

        num = int(input('Please Take some Match Sticks Between 1 to 4 (Turn: {0} / NOM: {1}): '
                        .format(player_name,MATCHSTICKS))) # input from player.
        MATCHSTICKS -= num
        GAMEROUND += 1
    
    myList = [F'{player_1}:{player1_score}', F'\n{player_2}:{player2_score}'] # create a list to prepare for saving in the file

    # find winner and update the player scores
    if MATCHSTICKS % 2 == 0:
        #winner
        if GAMEROUND % 2==0:
            print(F'{player_2} WON!')
            player2_score += 1
            myList[1]=F'\n{player_2}:{player2_score}'
        else:
            print(F'{player_1} WON!')
            player1_score += 1        
            myList[0]=F'{player_1}:{player1_score}'
    else:
        #loser
        if GAMEROUND % 2 !=0:
            print(F'{player_2} WON!')
            player2_score += 1
            myList[1]=F'\n{player_2}:{player2_score}'
        else:
            print(F'{player_1} WON!')
            player1_score += 1        
            myList[0]=F'{player_1}:{player1_score}'
            

    # Write the players score in a file
    with open('e:\\workspace\\python\\git\\python_assign_2\\gamescore.txt','w') as scoreWrite:
        scoreWrite.writelines(myList)
        
    MATCHSTICKS = 15 # Reset repository for a new round
    GAMEROUND = 1 # reset game round
    print('Try again for a new round ...') if item < 4 else print('Game Over!')
    
with open('e:\\workspace\\python\\git\\python_assign_2\\gamescore.txt','r') as scoreRead:
    playerScoreFile = scoreRead.readlines()
    for item in playerScoreFile:
        print(item)