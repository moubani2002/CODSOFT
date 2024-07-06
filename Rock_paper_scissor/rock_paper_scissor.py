#codsoft task - 4:
#Rock Paper Scissor game

import random

def main():
    while True:
        print("___Let's play Rock Paper Scissor___")
        print("Enter yor choice between 0, 1, 2....while 0 for rock, 1 for paper, 2 for scissor: ")
        user = int(input())
        computer = random.randint(0,2)

        if user == computer:
            print("It's a tie!")
    
        elif(user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
            print("Congratulations!! you win!!")

        elif(user !=0 and user != 1 and user != 2):
            print("Invalid input!!")

        else:
            print("Computer wins!!")

        print("Do you want to play again? (yes/no)")
        play_again = input().strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ =="__main__":
    main()
