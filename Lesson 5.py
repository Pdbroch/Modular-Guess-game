from Functions import top_scores, play_game, checkfileexists

checkfileexists("score_list.txt")

while True:
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?")

    if selection.upper() == "A":
        play_game("score_list.txt")
    elif selection.upper() == "B":
        top_scores("score_list.txt")
    elif selection.upper() == "C":
        break
    else:
        print("Error. Invalid input.")