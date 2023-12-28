import random
choices = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    user_choice=input("Enter your choice,Rock paper or Scissors? ").lower()
    if user_choice in choices:
        return user_choice
    else:
        return "invalid choice.Please try again"

    def winner(user_choice,computer_choice):
        if user_choice==computer_choice:
            return"It is a tie!"
        elif(user_choice=="rock" and computer_choice=="Scissors") or\
             (user_choice=="scissors" and computer_choice=="paper") or\
             (user_choice=="paper" and computer_choice"rock"):
             return "You win!"
        else:
                return "computer win!"

def game_play():
    print("let's play!")
    while True: 
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        print("You chose:{user_choice}")
        print("computer chose:{computer_choice}") 
        result="winner"(user_choice,computer_value)
        print(result)
        play_again=input("do you want to play again?) (y/n):").lower()
        if play_again !="y":
            break
