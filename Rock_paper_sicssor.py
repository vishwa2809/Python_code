def winner(player1_nm,player1,player2_nm, player2):
    if player1 == player2:
        return "both are same!tie"
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        return f"Congratulations {player1_nm}! You are the winner."
    else:
        return f"Congratulations {player2_nm}! You are the winner."

def play_game():
    player1_nm=input(str("enter your name"))
    player2_nm=input(str("enter your name"))
    
    choices = ['rock', 'paper', 'scissors']
    while True:
        player1_choice = input("{player1}, enter(rock/paper/scissors): ").lower()
        if player1_choice not in choices:
            print("Invalid")
            continue
        
        player2_choice = input("{player2}, enter(rock/paper/scissors): ").lower()
        if player2_choice not in choices:
            print("Invalid ")
            continue

        print(f"{player1_nm} chose {player1_choice}")
        print(f"{player2_nm} chose {player2_choice}")

        result = winner(player1_nm,player1_choice,player2_nm, player2_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
    
