"""

Python Sideproject by. 8luebottle

Date : Oct 12, 2019
Project Name : Roll-Dice

"""
import random as r
import pprint

def main():
    #Random min & max
    min = 1
    max = 6

    def roll_dice():
        #Counter
        win       = 0
        lose      = 0
        high_five = 0
           
        while True:
            choice = input('Would you like to play? y/n\n')
            print(f"""
            [SCORES]
            Win:        {win} time(s)        
            Lose:       {lose} time(s)        
            High five:  {high_five} time(s)        
            """)

            if choice.lower() == ('n' or 'no'):
                print('Bye, human')
                break
            elif choice.lower() == ('y' or 'yes'):
                user     = r.randint(min, max)
                computer = r.randint(min, max)

                print(f"""******* Rolling the dice *******
                     You rolled a {user}
                computer rolled a {computer}""")

                if user > computer:
                    win = win + 1
                    print('You Win!')

                elif user < computer:
                    lose = lose + 1
                    print('You Lose!')
                else:
                    high_five = high_five + 1
                    print('High Five!')
            else:
                print('\nPlease input y or n')
        
    roll_dice()

main()
