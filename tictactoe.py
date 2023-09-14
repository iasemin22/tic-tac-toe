def initializeplayer():
    right_input = False
    while right_input == False:
        playersymbol1 = input("Player 1, do you want to play with 'x' or 'o'?")
        if playersymbol1 == "x" or playersymbol1 == "o":
            right_input = True
        else:
            print("Invalid choice")
    if playersymbol1 == "o":
        playersymbol2 = "x"
    elif playersymbol1 == "x":
        playersymbol2 = "o"
    print(f"Player 1, you are playing with {playersymbol1}")
    print(f"Player 2, you are playing with {playersymbol2}")
    return playersymbol1, playersymbol2


def initializeboard():
    boardcoordinates = ["1a", "2a", "3a", "1b", "2b", "3b", "1c", "2c", "3c"]
    startboard = {coordinate: "empty" for coordinate in boardcoordinates}
    return startboard, boardcoordinates


def printboard(startboard: dict, symbolpl1: str, symbolpl2: str):
    row = []
    gameboard = []
    for tile, state in startboard.items():  # assigns tile and board state for all 9 tile in a board
        if state == "empty":
            row.append("|   |")
        elif state == "Player 1":
            row.append(f"| {symbolpl1} |")
        elif state == "Player 2":
            row.append(f"| {symbolpl2} |")
        if len(row) == 3:
            if len(gameboard) == 0:
                number = " a "
            elif len(gameboard) == 1:
                number = " b "
            elif len(gameboard) == 2:
                number = " c "
            gameboard.append(number + row[0] + row[1] + row[2])
            row = []
    print(".    1    2    3")
    print(*gameboard, sep="\n")
    pass


def choice_of_player(coordinates: list, takenturn: list, currentplayer: str):
    possiblemoves = [
        points for points in coordinates if points not in takenturn]
    right_input = False
    while right_input == False:
        player_input = input(
            f"{currentplayer}, its your turn. The possible choices are "+str(possiblemoves))
        if possiblemoves.count(player_input) > 0:
            right_input = True
        else:
            print("Invalid choice")
    takenturn.append(player_input)
    return player_input, takenturn


def maketurn(activeplayer: str, input: str, startboard: dict):
    if activeplayer == "Player 1":
        startboard[input] = "Player 1"
    elif activeplayer == "Player 2":
        startboard[input] = "Player 2"
    return startboard


def turn_order(currentplayer: str, turncount: int):
    turncount += 1
    if currentplayer == "Player 1":
        currentplayer = "Player 2"
    elif currentplayer == "Player 2":
        currentplayer = "Player 1"
    return currentplayer, turncount


def winning_check(boardstate: dict, playersymbol1: str, playersymbol2: str):
    winning = False
    win_conditions = [["1a", "1b", "1c"], ["2a", "2b", "2c"], ["3a", "3b", "3c"], ["1a", "2a", "3a"], [
        "1b", "2b", "3b"], ["1c", "2c", "3c"], ["1a", "2b", "3c"], ["1c", "2b", "3a"]]
    for wincondition in win_conditions:
        if boardstate[wincondition[0]] == boardstate[wincondition[1]] and boardstate[wincondition[1]] == boardstate[wincondition[2]]:
            if boardstate[wincondition[0]] == "Player 1":
                printboard(boardstate, playersymbol1, playersymbol2)
                print(f"Player 1 won with {playersymbol1}")
                winning = True
            elif boardstate[wincondition[0]] == "Player 2":
                printboard(boardstate, playersymbol1, playersymbol2)
                print(f"Player 2 won with {playersymbol2}")
                winning = True
            break
    return winning


def starttictactoe():
    takenturns = []
    turncount = 0
    currentplayer = "Player 1"
    playersymbol1, playersymbol2 = initializeplayer()
    startboard, boardcoordinates = initializeboard()
    winning = False
    while winning == False:
        printboard(startboard, playersymbol1, playersymbol2)
        startchoice, takenturns = choice_of_player(
            boardcoordinates, takenturns, currentplayer)
        startboard = maketurn(currentplayer, startchoice, startboard)
        currentplayer, turncount = turn_order(currentplayer, turncount)
        if turncount >= 5 and turncount < 9:
            winning = winning_check(startboard, playersymbol1, playersymbol2)
        elif turncount == 9:
            print("This is a draw")
            break


starttictactoe()
