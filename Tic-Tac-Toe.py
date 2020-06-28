import random
import time

board = """[ ] [ ] [ ]
[ ] [ ] [ ]
[ ] [ ] [ ]"""

possible_plays = {"Top Left": 1, "Top Middle": 5, "Top Right": 9,
                  "Center Left": 13, "Center Middle": 17, "Center Right": 21,
                  "Bottom Left": 25, "Bottom Middle": 29, "Bottom Right": 33}

computer_options = [1, 5, 9, 13, 17, 21, 25, 29, 33]
already_guessed = []


def remove_options_from_computer_options():
    for item in computer_options:
        if item in already_guessed:
            computer_options.remove(item)
        else:
            pass


def computer_function():
    global board
    computer_turn = random.choice(computer_options)
    already_guessed.append(computer_turn)
    board_list = list(board)
    board_list[computer_turn] = computer_marker
    board = "".join(board_list)
    return computer_turn, board


def player_function():
    global board
    board_list = list(board)
    board_list[possible_plays.get(player_turn)] = player_marker
    board = "".join(board_list)
    player_function_result = already_guessed.append(possible_plays.get(player_turn))
    return player_function_result, board


def check_win_conditions():
    player_winner = False
    computer_winner = False
    winning_triples = [
        (1, 5, 9),
        (13, 17, 21),
        (25, 29, 33),
        (1, 13, 21),
        (5, 17, 29),
        (9, 21, 33),
        (1, 17, 33),
        (9, 17, 25)
    ]
    for triple in winning_triples:
        if all(board[i] == player_marker for i in triple):
            player_winner = True
        elif all(board[i] == computer_marker for i in triple):
            computer_winner = True
        else:
            pass
    return player_winner, computer_winner


print("You are playing Tic Tac Toe!\nChoose your marker (X or O), and select the spot on the board!")
time.sleep(2)
print("Choose: Top Right, Bottom Left, Center Left, Bottom Middle, etc.")
time.sleep(1.5)
print(board)

while True:
    player_marker = input("Will you play X or O? ").upper()
    if player_marker == "X":
        computer_marker = "O"
        break
    elif player_marker == "O":
        computer_marker = "X"
        break
    else:
        print("Enter a valid input")
        continue

while True:
    player_turn = input("Choose the spot to place your marker:  ").split(" ")
    word_list = [word.capitalize() for word in player_turn]
    player_turn = " ".join(word_list)

    if possible_plays.get(player_turn) in already_guessed:
        print("That spot is already taken!")
        continue
    elif player_turn not in possible_plays:
        print("Invalid input")
        continue
    else:
        print(f"{player_function()[1]}\n")
        remove_options_from_computer_options()

    player_winner = check_win_conditions()[0]
    if player_winner:
        time.sleep(1.5)
        print("You win! Great job")
        break
    else:
        pass

    time.sleep(1.5)
    print(f"Computer's turn:\n{computer_function()[1]}\n")
    time.sleep(1.5)

    computer_winner = check_win_conditions()[1]
    if computer_winner:
        print("You lose. Better luck next time!")
        break
    else:
        pass

    continue




