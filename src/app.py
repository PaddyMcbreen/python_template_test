import sqlite3
import random
import subprocess
from database import init_db, save_score

# Give scripts required permissions:
subprocess.run(["chmod +x ./scripts/permissions.sh"], shell=True)
subprocess.run(["./scripts/permissions.sh"], shell=True)

DATABASE = 'scores.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def get_scores():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scores")
    scores = cursor.fetchall()
    conn.close()
    return scores

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    while True:
        guess = int(input("Enter your guess: "))
        print("You have chosen", guess)
        print("-------------------------------------------------")
        attempts += 1

        if guess < number_to_guess:
            print(guess,"is too low! Try again.")
            print("-------------------------------------------------")

        elif guess > number_to_guess:
            print(guess,"is too high! Try again.")
            print("-------------------------------------------------")

        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            save_score(attempts)
            
            print("-------------------------------------------------")
            again = str(input("Would you like to play again?: (y/n) ")).strip().lower()
            print("-------------------------------------------------")

            if again == "y":
                print("Great! Here we go again")
                subprocess.run(["./scripts/again_app.sh"], shell=True)

            else:
                print("Thats too bad! Bye now")
                print("-------------------------------------------------")
                print("Here is your score: ")

                scores = get_scores()
                for score in scores:
                    print(f"Player ID: {score[0]}, Attempts: {score[1]}")
                    print("-------------------------------------------------")
                    
            break

# -------------------------
if __name__ == '__main__':
    init_db()
    play_game()