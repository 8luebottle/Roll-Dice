"""

Python Sideproject by. 8luebottle

Date : Oct 12, 2019
Project Name : Roll-Dice

"""
import random as r
import pprint

def main():
    min = 1
    max = 6

    def roll_dice():
        choice = input('Would you like to play? y/n\n')
        
        if choice.lower() == ('n' or 'no'):
            print('Bye, human')
        elif choice.lower() == ('y' or 'yes'):
            user     = r.randint(min, max)
            computer = r.randint(min, max)

            print(f"""******* Rolling the dice *******
                 You rolled a {user}
            computer rolled a {computer}""")

            if user > computer:
                print('You Win!')
            elif user < computer:
                print('You Lose!')
            else:
                print('High Five!')
        else:
            print('\nPlease input y or n')

    roll_dice()

main()
