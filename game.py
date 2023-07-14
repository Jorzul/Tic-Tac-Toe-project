import random

n = int(3)
a = [[" " for col in range(n)] for row in range(n)]


def print_board():

    print("--------------------")
    for i in range(0, n):
        j = int(0)
        print(" | ", a[i][j], " | ", a[i][j + 1], " | ", a[i][j + 2], " | ")
        print("--------------------")


def winning_player_with_O():
    winning = bool(True)

    for i in range(0, n):
        winning = True
        for j in range(0, n):
            if a[i][j] == " " or a[i][j] == "X":
                winning = False
        if winning:
            return 1

    for i in range(0, n):
        winning = True
        for j in range(0, n):
            if a[j][i] == " " or a[j][i] == "X":
                winning = False
        if winning:
            return 1

    for i in range(0, n):
        winning = True
        if a[i][i] == " " or a[i][i] == "X":
            winning = False
    if winning:
        return 1

    return 0


def winning_player_with_X():

    for i in range(0, n):
        winning = True
        for j in range(0, n):
            if a[i][j] == " " or a[i][j] == "O":
                winning = False
        if winning:
            return 1

    for i in range(0, n):
        winning = True
        for j in range(0, n):
            if a[j][i] == " " or a[j][i] == "O":
                winning = False
        if winning:
            return 1

    winning = True
    for i in range(0, n):
        if a[i][i] == " " or a[i][i] == "O":
            winning = False
    if winning:
        return 1

    winning = True
    for i in range(0, n):
        if a[i][n-1-i] == " " or a[i][n-1-i] == "O":
            winning = False
    if winning:
        return 1

    return 0


def place_on_board(sign):
    print("What are the coordinates you would like to place?")

    while True:
        row = int(input("Row: "))
        column = int(input("Column: "))

        if row >= n or column >= n:
            print("Try again!")
        elif row < 0 or column < 0:
            print("Try again!")
        elif a[row][column] != " ":
            print("Try again!")
        else:
            a[row][column] = sign
            break


def place_random_on_board(sign):
    while True:
        row = random.randint(0, n)
        column = random.randint(0, n)

        if row >= n or column >= n:
            pass
        elif row < 0 or column < 0:
            pass
        elif a[row][column] != " ":
            pass
        else:
            a[row][column] = sign
            break


def board_full():

    for i in range(0, n):
        for j in range(0, n):
            if a[i][j] == " ":
                return 0

    return 1


def menu():

    print("How would you like to play the game?")
    print("1. Player vs Bot")
    print("2. Player vs Player")
    option = int(input(">"))

    if option == 2:

        player_1 = bool(True)
        while True:

            print_board()

            if board_full():
                print("Game over!")
                return 0

            if winning_player_with_X() == 1:
                print("Player 1 won!")
                return 0

            if winning_player_with_O() == 1:
                print("Player 2 won!")
                return 0

            if player_1:
                place_on_board("X")
                player_1 = False
            else:
                place_on_board("O")
                player_1 = True

    if option == 1:

        player_1 = bool(True)
        while True:

            print_board()

            if winning_player_with_X() == 1:
                print("Player 1 won!")
                return 0

            if winning_player_with_O() == 1:
                print("Player 2 won!")
                return 0

            if player_1 == 1:
                place_on_board("X")
                player_1 = False
            elif player_1 == 0:
                place_random_on_board("O")
                player_1 = True


menu()
