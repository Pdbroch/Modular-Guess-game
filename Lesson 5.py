from Functions import top_scores, play_game, get_score_list


while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection.upper() == "A":
        play_game()
    elif selection.upper() == "B":
        top_scores()
    elif selection.upper() == "C":
        break
    else:
        print("Error. Invalid input.")