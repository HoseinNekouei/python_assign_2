class player():
    
    # Constructor method
    def __init__(self, name1, name2, matchstiks,gameround, player_score_1, player_score_2):
        self.player1 = name1
        self.player2 = name2
        self.matchsticks = matchstiks
        self.gameround = gameround
        self.player_score_1 = player_score_1
        self.player_score_2 = player_score_2
         
    # The Method that find player name in each round            
    def find_player_name(self,gameround):
        if gameround % 2 == 0:
            player_name = self.player2 # set the name of player on the second player if round of game was even! 
        else : 
            player_name = self.player1 # set the name of player on the first player if round of game was odd!     
        return player_name            
    
    # The method that determines the winning player
    def find_winner(self):
        for item in range(5):
            print('Start the round ...')                    
            print(f"Level: {item+1}") # print Counter of round of game
            
            while self.matchsticks >= 5:
                # call methon with number 0 for init for game round.
                player_name = self.find_player_name(self.gameround) 
                # The number of matches to be selected each time
                NUM = int(input(f'Choose Between 1 to 4 (Turn You: {player_name} / NOM: {self.matchsticks}): ')) 
                self.matchsticks -= NUM
                self.gameround += 1
            else:
                print('Game Over!')
                self.score_calc(player_name) 

    # The method that calculates scores    
    def score_calc(self,player_name):        
        if self.matchsticks % 2 == 0: # find winner and update the player scores
            player_name = self.find_player_name(self.gameround) # whoever has a turn wins!
            print(F'{player_name} WON!')
            self.player_score_2 += 1
            myList[1]=f'\n{self.player2}:{self.player_score_2}'
        else:
            print(F'{player_name} WON!') # The Last Player to win!
            self.player_score_1 += 1
            myList[0]=f'\n{self.player1}:{self.player_score_1}'
        
        self.matchsticks = 15 # Reset reposotory of matchstiks
        self.save_score(myList) # Call the save_score method to save the player score for each level  

    # The method that stores players' points                  
    def save_score(self, score): 
        # Write the players score in a file
        with open('e:\\workspace\\python\\git\\python_assign_2\\gamescore.txt','w') as scoreWrite:
            scoreWrite.writelines(score)
    
player_1 = input('Tell me your name... <First Player> ') # Get the name of first player
player_2 = input('Tell me your name... <Second Player> ') # Get the name of second player

myList = [f'{player_1}: 0', f'\n{player_2}: 0'] # create a list to prepare for saving in the file
PLAYER_SCORE_1=PLAYER_SCORE_2 = 0 # Set the initial value for the two player
MATCHSTICKS = 15 # Set the number of total mitch sticks in the game.    
GAMEROUND = 1 # The first init

player_obj = player(player_1,player_2, MATCHSTICKS, GAMEROUND, PLAYER_SCORE_1, PLAYER_SCORE_2)
player_obj.find_winner()