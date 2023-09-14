import os

def initializename(whatplayer : str):
    '''This lets the player choose their name for the upcoming game'''
    right_input = False
    while right_input == False:
        playername = input(f"{whatplayer}, what is your name?")
        if type(playername) == str:
            checkinput = False
            while checkinput == False:    
                check1 = input(f"Do you want your name to be {playername}? Enter 'y' to continue or 'n' to choose again.")
                if check1 == "y":
                    right_input = True
                    checkinput = True
                elif check1 == "n":
                    checkinput = True
                    continue
                else:
                    print("This was not the right input. Enter 'y' to continue or 'n' to choose again.")
                    continue
        else:
            print("Invalid choice")
    return playername

def initializeplayer(playername1, playername2):
    right_input = False
    while right_input == False:
        playersymbol1 = input(f"{playername1}, do you want to play with 'x' or 'o'?")
        if playersymbol1 == "x" or playersymbol1 == "o":
            right_input = True
        else:
            print("Invalid choice")
    if playersymbol1 == "o":
        playersymbol2 = "x"
    elif playersymbol1 == "x":
        playersymbol2 = "o"
    print(f"{playername1}, you are playing with {playersymbol1}")
    print(f"{playername2}, you are playing with {playersymbol2}")
    return playersymbol1, playersymbol2


def initializeboard(boardchoice):
    startboard = {coordinate: "empty" for coordinate in boardchoice}
    return startboard, boardchoice


def printboard(startboard: dict, symbolpl1: str, symbolpl2: str, playername1, playername2):
    row = []
    gameboard = []
    tile = [position for position, state in startboard.items()]
    for idx, state in startboard.items():  # assigns tile and board state for all 9 tile in a board
        if state == "empty":
            row.append(f"| {idx} |")
        elif state == playername1:
            row.append(f"| {symbolpl1} |")
        elif state == playername2:
            row.append(f"| {symbolpl2} |")
        if len(row) == 3:
            # if len(gameboard) == 0:
            #     startnumber = f" {tile[0]} "
            #     endnumber = f" {tile[2]} "
            # elif len(gameboard) == 1:
            #     startnumber = f" {tile[3]} "
            #     endnumber = f" {tile[5]} "
            # elif len(gameboard) == 2:
            #     startnumber = f" {tile[6]} "
            #     endnumber = f" {tile[8]} "
            gameboard.append(row[0] + row[1] + row[2])
            row = []
    #print(f".         {tile[1]}")
    print("---------------")
    print(*gameboard, sep="\n")
    print("---------------")
    #print(f".         {tile[7]}")
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


def maketurn(activeplayer: str, input: str, startboard: dict, playername1, playername2):
    if activeplayer == playername1:
        startboard[input] = playername1
    elif activeplayer == playername2:
        startboard[input] = playername2
    return startboard


def turn_order(currentplayer: str, turncount: int, playername1, playername2):
    turncount += 1
    if currentplayer == playername1:
        currentplayer = playername2
    elif currentplayer == playername2:
        currentplayer = playername1
    return currentplayer, turncount


def winning_check(boardstate: dict, playersymbol1: str, playersymbol2: str, boardchoice : list,playername1, playername2):
    winning = False
    winner = ""
    boardchoice = [position for position, state in boardstate.items()]
    win_conditions = [[boardchoice[0], boardchoice[1], boardchoice[2]], [boardchoice[3], boardchoice[4], boardchoice[5]], [boardchoice[6], boardchoice[7], boardchoice[8]], [boardchoice[0], boardchoice[3], boardchoice[6]], [
        boardchoice[1], boardchoice[4], boardchoice[7]], [boardchoice[2], boardchoice[5], boardchoice[8]], [boardchoice[0], boardchoice[4], boardchoice[8]], [boardchoice[2], boardchoice[5], boardchoice[6]]]
    for wincondition in win_conditions:
        if boardstate[wincondition[0]] == boardstate[wincondition[1]] and boardstate[wincondition[1]] == boardstate[wincondition[2]]:
            if boardstate[wincondition[0]] == playername1:
                printboard(boardstate, playersymbol1, playersymbol2,playername1,playername2)
                print(f"{playername1} won with {playersymbol1}")
                winning = True
                winner = playername1
                break
            elif boardstate[wincondition[0]] == playername2:
                printboard(boardstate, playersymbol1, playersymbol2,playername1,playername2)
                print(f"{playername2} won with {playersymbol2}")
                winning = True
                winner = playername2
                break
    return winning, winner


def starttictactoe():
    boardchoice = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    takenturns = []
    turncount = 0
    playername1, playername2 = initializename("Player 1"),initializename("Player 2")
    if playername1 == playername2:
        playername2 = playername2+"2"
    currentplayer = playername1
    playersymbol1, playersymbol2 = initializeplayer(playername1, playername2)
    startboard, boardcoordinates = initializeboard(boardchoice)
    winning = False
    while winning == False:
        os.system('clear')
        printboard(startboard, playersymbol1, playersymbol2, playername1, playername2)
        startchoice, takenturns = choice_of_player(
            boardcoordinates, takenturns, currentplayer)
        startboard = maketurn(currentplayer, startchoice, startboard, playername1,playername2)
        currentplayer, turncount = turn_order(currentplayer, turncount,playername1,playername2)
        if turncount >= 5 and turncount <= 9:
            winning, winner = winning_check(startboard, playersymbol1, playersymbol2, boardchoice, playername1, playername2)
            if turncount == 9 and winner == "":
                print("This is a draw")
                break
    return winner, playername1, playername2, boardchoice

def continuetictactoe(winner, playername1, playername2, boardchoice):
    takenturns = []
    turncount = 0
    if winner == playername1:
        currentplayer = playername2
    elif winner == playername2:
        currentplayer = playername1
    else:
        currentplayer = playername1
    playersymbol1, playersymbol2 = initializeplayer(playername1, playername2)
    startboard, boardcoordinates = initializeboard(boardchoice)
    winning = False
    while winning == False:
        os.system('clear')
        printboard(startboard, playersymbol1, playersymbol2, playername1, playername2)
        startchoice, takenturns = choice_of_player(
            boardcoordinates, takenturns, currentplayer)
        startboard = maketurn(currentplayer, startchoice, startboard, playername1,playername2)
        currentplayer, turncount = turn_order(currentplayer, turncount,playername1,playername2)
        if turncount >= 5 and turncount <= 9:
            winning, winner = winning_check(startboard, playersymbol1, playersymbol2, boardchoice, playername1, playername2)
            if turncount == 9 and winner == "":
                print("This is a draw")
                break
    return winner

def checkwinners(winners : list,playername1, playername2, outcomeplayer1 = [], outcomeplayer2 = []):
    if len(winners) > 0:
        if winners[len(winners)-1] == playername1:
            outcomeplayer1.append("win")
            outcomeplayer2.append("loss")
        elif winners[len(winners)-1] == playername2:
            outcomeplayer2.append("win")
            outcomeplayer1.append("loss")
    else:
        outcomeplayer1.append("draw")
        outcomeplayer2.append("draw")
    print(f"{playername1} you have:" , *outcomeplayer1, sep=" ")
    print(f"{playername2} you have:" , *outcomeplayer2, sep=" ")
    return outcomeplayer1, outcomeplayer2

def bestof3():
    winners = []
    winner, playername1, playername2, boardchoice = starttictactoe()
    winners.append(winner)
    outcomeplayer1, outcomeplayer2 = checkwinners(winners, playername1, playername2)
    while len(outcomeplayer1) < 3:
        winner = continuetictactoe(winner, playername1, playername2, boardchoice)
        winners.append(winner)
        outcomeplayer1, outcomeplayer2 = checkwinners(winners, playername1, playername2,outcomeplayer1,outcomeplayer2)
    if winners.count(playername1) > winners.count(playername2):
        print(f"{playername1} has won with {winners.count(playername1)} wins")
    else:
        print(f"{playername2} has won {winners.count(playername2)} wins")

if __name__ == "__main__":
    bestof3()
