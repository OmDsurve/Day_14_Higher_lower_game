# Display art

from art import logo, vs
from game_data import data
import random
print(logo)
score = 0


def format_data(account):
    """ takes the account data and returns into printable format"""
    account_name = account["name"]
    account_dcr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_dcr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    # Generate a game data from random account
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_a = random.choice(data)
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #  ask the user for a guess
    guess = input("Guess who has the more followers? A or B ").lower()
    # clear the screen
    print("\n"*40)
    print(logo)

    # check if user is correct

    # - get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # - use if statement if user is correct
    # give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right. Current score {score}")
    else:
        print(f"Sorry, that's wrong. Current score is {score} ")
        game_should_continue = False
