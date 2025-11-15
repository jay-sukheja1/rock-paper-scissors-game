import random

def get_choices():
    options = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Enter a choice (rock, paper, scissors): ").lower() 
        
        if player_choice in options:
            break
        else:
            print("Invalid choice. Please enter rock, paper, or scissors")
            
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}") 
    
    if player == computer:
        return "It's a tie!"
    
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You won!"
    
    else:
        return "You lost!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)
