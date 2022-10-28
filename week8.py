import random

import time

start=time.time()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score


class ComputerPlayer(Player):
    pass


class Die:

    def __init(self):
        self.face_value = 1 
    
    def set_face_value(self, value):
        self.face_value = value
    
    def get_face_value(self):
        return self.face_value
    
    def roll(self):
        a = random.randint(1,6)
        return a
        
class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.die = Die()
        self.turn = True
        self.temp_score = 0
        
    def play_game(self):
        t=0
        if type(player1).__name__== "Player":
            while True and time.time()-start < 60:
            
                if self.turn == True:
                    print("\nYour turn")
                    print("\n1. Roll")
                    print("2. Hold\n")
                    option = int(input("choose option: "))
                    if option == 1:
                        value = self.die.roll()
                        print("\nyour rolled a "+str(value))
                        if value == 1:
                            self.temp_score = 0
                            self.turn = False
                        else:
                            self.temp_score += value
                    elif option == 2:
                        current_score = player1.get_score()
                        player1.set_score(current_score + self.temp_score)
                        self.temp_score = 0
                        self.turn = False
                    else:
                        print("Enter valid option")
                
                    if player1.get_score() + self.temp_score >= 100:
                        print('Your score is 100')
                        print(player1.get_name()+" wins")
                        break
                    print("Your turn score is "+str(self.temp_score))
                    print("Your total score is "+str(player1.get_score()))
                    if player1.get_score() >= 100:
                        t=1
                        print(player1.get_name()+" wins")
                        break
                else:
                    print("\nBot turn")
                    time.sleep(1)
                    value = self.die.roll()
                    print("\nIt rolled a "+str(value))
                    if value == 1:
                        self.temp_score = 0
                        self.turn = True
                    else:
                        self.temp_score += value
                    if self.temp_score >=19 or self.temp_score>=100-player2.get_score():
                        current_score = player2.get_score()
                        player2.set_score(current_score + self.temp_score)
                        self.temp_score = 0
                        self.turn = True
                
                
                    print("Bot turn score is "+str(self.temp_score))
                    print("Bot total score is "+str(player2.get_score()))
                    if player2.get_score() >= 100:
                        t=1
                        print(player2.get_name()+" wins")
                        break
            
        else:
            print("\nBot turn")
            value = self.die.roll()
            print("\nIt rolled a "+str(value))
            if value == 1:
                self.temp_score = 0
                self.turn = False
            else:
                self.temp_score += value
            
                
            print("Bot turn score is "+str(self.temp_score))
            print("Bot total score is "+str(player1.get_score()))
            while True and time.time()-start < 60:
               
                if self.turn == True:
                    print("\nBot turn")
                    time.sleep(1)
                    value = self.die.roll()
                    print("\nIt rolled a "+str(value))
                    if value == 1:
                        self.temp_score = 0
                        self.turn = False
                    else:
                        self.temp_score += value
                    if self.temp_score >=19 or self.temp_score>=100-player1.get_score() :
                        current_score = player1.get_score()
                        player1.set_score(current_score + self.temp_score)
                        self.temp_score = 0
                        self.turn = False
                
                
                    print("Bot turn score is "+str(self.temp_score))
                    print("Bot total score is "+str(player1.get_score()))
                    if player1.get_score() >= 100:
                        t=1
                        print(player1.get_name()+" wins")
                        break
                else:
                    print("\nYour turn")
                    print("\n1. Roll")
                    print("2. Hold\n")
                    option = int(input("choose option: "))
                    if option == 1:
                        value = self.die.roll()
                        print("\nyour rolled a "+str(value))
                        if value == 1:
                            self.temp_score = 0
                            self.turn = True
                        else:
                            self.temp_score += value
                    elif option == 2:
                        current_score = player2.get_score()
                        player2.set_score(current_score + self.temp_score)
                        self.temp_score = 0
                        self.turn = True
                    else:
                        print("Enter valid option")
                
                    if player2.get_score() + self.temp_score >= 100:
                        print('Your score is 100')
                        print(player1.get_name()+" wins")
                        break
                    print("Your turn score is "+str(self.temp_score))
                    print("Your total score is "+str(player2.get_score()))
                    if player2.get_score() >= 100:
                        t=1
                        print(player2.get_name()+" wins")
                        break
        if t==0: 
            print("One minute is over")
            if player1.get_score()>player2.get_score():
                print(player1.get_name()+" wins")
            else:
                print(player2.get_name()+"wins")
            
        
                        
            
            
    
if __name__ == "__main__":
    player= input("Enter player number you want to be 1 or 2 ")
    if player=="1":
        player1=Player("You")
        player2=ComputerPlayer("Bot")
    else :
        player2=Player("You")
        player1=ComputerPlayer("Bot")
    
    
    
    
    game = Game(player1, player2)
    game.play_game()

