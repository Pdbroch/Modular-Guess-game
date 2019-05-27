import random
import json
import datetime
import operator
import os

def play_game(file_path):
    attempts = 0
    secret = random.randint(1, 30)
    current_time = datetime.datetime.now()
    incorrect_guess = []
    with open(file_path, "r") as score_file:
        score_list = json.loads(score_file.read())
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            print("You've guessed it - congratulations! It's number " + str(secret))
            name = input("Attempts needed: " + str(attempts) + ". Please input your name: ")
            print("You guessed the following numbers: " + str(incorrect_guess) + " which were inccorect.")
            score_list.append({"name": name, "attempts": attempts, "answer": secret, "incguess": str(incorrect_guess),
                               "date": str(datetime.datetime.now())})
            score_list.sort(key=operator.itemgetter("attempts"))
            with open(file_path, "w") as score_file:
                score_file.write(json.dumps(score_list))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
            incorrect_guess.extend([guess])
        elif guess < secret:
            print("Your guess is not correct... try something bigger")
            incorrect_guess.extend([guess])


def top_scores(file_path):
    with open(file_path, "r") as score_file:
        score_list = json.loads(score_file.read())
    print("Top Scores")
    for score_dict in score_list[:3]:
        print(str(score_dict["name"]) + ", " + str(score_dict["attempts"]) + " attempts, secret number: " + str(
            score_dict["answer"]) + ", incorrect guesses:" + str(score_dict["incguess"]) + ", date: " + score_dict.get(
            "date"))


def checkfileexists(file_path):
    ret = True
    try:
        # Open file object.
        file_object = open(file_path, 'r')
        # Check if file is empty if empty creates list
        if os.path.getsize(file_path) == 0:
            list = []
            with open(file_path, "w") as score_file:
                score_file.write(json.dumps(list))
    # If file does not exist makes one with empty list
    except FileNotFoundError:
        ret = False
        list = []
        file_object = open(file_path, 'w')
        file_object.write(json.dumps(list))

    return ret