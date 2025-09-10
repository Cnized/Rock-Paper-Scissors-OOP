''' Author: Cnized (Kian Kheiri N.)
    Date: 2025-09-09
    description: A simple Rock-Paper-Scissors game implementation in Python.
    '''

import random
class RockPaperScissors:
    '''A class to represent the Rock-Paper-Scissors game.'''
    
    def __init__(self):
        '''Initializes the game with player name, choices, and score.
        '''
        self.choices = ['rock', 'paper', 'scissors']
        self.name = input('Enter your name: (Choose wisely, you can\'t change it during the game) ')
        self.scr: int = 0 
        
    def player_choice(self):
        ''' Method to get the player's choice.
        :return: _user_input: _description_ 
        :rtype: str
        '''
        while True:
            user_input: str = input(f'Enter a Valid choice: ( {self.choices} ) ').lower()
            if user_input in self.choices:
                return user_input
            print('Invalid Input, Try again.')

    def computer_choice(self):
        ''' Method to get the computer's random choice.'''
        return random.choice(self.choices)
    
    def add_scores(self):
        '''Method to add scores when the player wins.

        :return: _description_
        :rtype: int
        '''
        self.scr += 10
        return self.scr
    
    def dec_scores(self):
        '''Method to decrease scores when the player loses.
        
        :return: _description_
        :rtype: int'''
        if self.scr > 0 :
            self.scr -= 5
            return self.scr
        else:
            return self.scr
    
    def set_winner(self, user: str, computer: str):
        '''Method to determine the winner based on user and computer choices.
        :param user: the user's choice
        :param computer: the computer's choice
        :return: The result of the game
        '''
        if user == computer:
            return f'Draw !! score: {self.scr}'
        elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or ( user == 'paper' and computer == 'rock'):
            return f'{self.name} is the Winner! \n score: {self.add_scores()} '
        else:
            return f'Computer is the winner! \n score: {self.dec_scores()}'
    
    
    def play(self):
        '''Method to play the game.
        - Gets user and computer choices
        - Determines and prints the result
        '''
        user = self.player_choice()
        computer = self.computer_choice()
        print(f'User choice: {user}, Computer choice: {computer}')
        result = self.set_winner(user, computer)
        print(result)
    

if __name__ == '__main__':
    game = RockPaperScissors()
    while True:
        game.play()
        print('-------------------')
        print('Do you want to play again? (Press any key to continue, \'no\' to quit.')
        if input().lower() == 'no':
            break