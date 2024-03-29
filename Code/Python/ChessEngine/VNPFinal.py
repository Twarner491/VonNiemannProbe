# (c) Teddy Warner & Jack Hollingsworth - 2022

# This work may be reproduced, modified, distributed, performed, and displayed
# for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
# Copyright is retained and must be preserved. The work is provided as is;
# no warranty is provided, and users accept all liability.

# Contributors - 
# - Solanaceae

# download stockfish from https://stockfishchess.org/files/stockfish_15_win_x64_avx2.zip

from stockfish import Stockfish  # pip install stockfish
import chess  # pip install python-chess
import serial # pip install pyserial
import re  # pip install regex

global board; 
global fish
global legal; 
global legalMoves
global moveAdjusted; 
global badChars
global isMate; 
global morseDict
global morseMove; 
global port 
global stockfishPath

port = "COM3"  # set bluetooth port

# replace with the path to your Stockfish exe. Note - the path may only contain forward slashes, no backslashes.
stockfishPath = "C:/Users/twarn/Downloads/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe"

morseDict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
}  # morse dict for all chars in chess moves, other characters not needed here

board = chess.Board()  #create chess board object

badChars = [
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "9",
    "0",
]  # chars that can't be in a legal chess move

morseMove = ""  # placeholder for morse code move, filled later

fish = Stockfish(
    r"{0}".format(stockfishPath),
    depth=18,
    parameters={"Threads": 4, "Hash": 256, "UCI_LimitStrength": "false"},
)  
# stockfish object declaration, can regulate strength
print(f"WDL Accepted {str(fish.does_current_engine_version_have_wdl_option())}")
print(f"Board State {fish.get_board_visual()}")

# open com port of hc-06 receiving, set to 9600 baud
ser = serial.Serial(port, 9600, timeout=1)
print("serial opened")


def playGame(side):
    global legal
    global legalMoves
    global board
    global isMate
    global morseMove
    mate = False  # checkmate state declaration
    turns = 0
    i = 0  # these could be the same, but easier to keep sep = SPAGHETTIOLI CODE MOMENT
    board = chess.Board()
    print(f"fish playing as {side}")
    if side == "white":
        while not mate:  # if game not over, play continues
            # stockfish get best current move
            bestMove = fish.get_best_move(1000)
            fish.make_moves_from_current_position([bestMove])
            # create chessMove object in pychess, push it to board on next line
            chessMove = chess.Move.from_uci(bestMove)
            # make move in pychess to keep up with stockfish game
            board.push_san(bestMove)
            print(f"whitefish plays {bestMove}")
            morseMove = toMorse(bestMove)  # call morse conversion of fish move
            # call to move sending function, arg is stockfish best move
            sendMove(morseMove)
            mate = board.is_checkmate()  # returns state of checkmate
            print(f"Checkmate: {str(mate)}")
            
            if mate == True:
                print("checkmate, stockfish victory!")
                return
            
            turns += 1
            legalMoves = str(board.legal_moves)  # convert list to string
            move = input("black move:")  # request player move
            getPlayerMove(move)
            mate = board.is_checkmate()  # check if player has won
            if mate == True:
                print("checkmate, player victory")
                return
            turns += 1
            print(f"board after {turns} moves:")
            # shows board from player perspective (white)
            print(fish.get_board_visual(False))
        print("")
        return  # return to infinite loop
    
    if side == "black":
        legalMoves = str(board.legal_moves)  # convert list to string
        
        while mate == False:
            print("white move:")
            move = input()
            getPlayerMove(move)
            mate = board.is_checkmate()  # check if player has won
            
            if mate == True:
                print("checkmate, player victory")
                return
            
            # stockfish get best current move
            bestMove = fish.get_best_move(1000)
            fish.make_moves_from_current_position([bestMove])
            chessMove = chess.Move.from_uci(bestMove)
            board.push_san(bestMove)
            print(f"blackfish plays {bestMove}")
            # get string of morse-converted move, not in use
            morseMove = toMorse(bestMove)
            sendMove(morseMove)  # send morse move via bluetooth
            mate = board.is_checkmate()  # returns state of checkmate
            print(f"Checkmate: {str(mate)}")
            
            if mate == True:
                print("checkmate, stockfish victory!")
                return
            
            turns += 1
            print(f"board after {turns} moves:")
            # shows board from player perspective (black)
            print(fish.get_board_visual())
        print("")
        return  # return to infinite loop


def getPlayerMove(move):
    global board
    global moveAdjusted
    global badChars
    global morseMove
    
    noBadChars = True  # reset no bad chars bool
    legal = False  # reset illegal bool
    charCount = 0
    numCount = 0
    
    for char in move:  # check if badChars exist in move
        i = 0  # reset iterating var
        while i < len(badChars):
            badChar = badChars[i]
            if char == badChar:
                print(f"{char} is ILLEGAL")
                noBadChars = False  # set bool to reflect bad char
            if char.isalpha() == True:
                charCount += 1  # reflect that at least 1 char in string
            if char.isdigit() == True:
                numCount += 1  # reflect that at least one number in string
            i += 1
            # print(char + "is legal") #debug bad chars function
    # solve edge case where small string doesn't break other rules
    
    if len(move) not in [4, 5]:
        noBadChars = False
        
    if charCount == 0 or numCount == 0:
        print(f"numbers: {str(numCount)}")
        print(f"chars {str(charCount)}")
        noBadChars = False  # change bool to reflect bad formatting
        
    if noBadChars == True:  # only creative move objects if correct formatting
        print(f"{move} is good format")
        # create move object frmo current player move, used to check legality
        myMove = chess.Move.from_uci(move)
        legal = board.is_legal(myMove)  # checks legality of desired move
        print(f"Legal? {str(legal)}")
        
    if legal and noBadChars:  # move can only happen if legal and doesn't contain illegal chars
        # plays legal player move in STOCKFISH
        fish.make_moves_from_current_position([move])
        chessMove = chess.Move.from_uci(move)  # load legal player move
        board.push_san(move)  # send player move to board tracker
        print(f"player plays {move}")
    else:
        newMove = input("Illegal move, input new move: ")
        getPlayerMove(newMove)
        
    return  # back to game loop


def toMorse(move):  # convert move to morse code
    ret = ""  # empty morse conversion
    newConvert = ""  # empty mid-conversion string
    for char in move:
        # print("converting " + char) #debug print
        newConvert = morseDict[char]  # take key of char index in morse dict
        ret += f"{newConvert} "
    print(f"Morse-Converted Move: {ret}")
    return ret


def sendMove(morse):
    morse = re.sub("[ ]", "9", morse)
    print(morse)  # print morse move with spaces replaced with 9 - easier to parse on arduino side as empty bytes hard to work with
    
    for char in morse:
        tempChar = char.encode()  # temporary placeholder set to current char in morse move
        # send individual character of final morse message encoded in utf-8
        ser.write(tempChar)
    print("sent move")
    return


isMate = False
while True:  # enables playing of inifinite games, playGame() returns to here after checkmate, resets all local values
    print("Good chess speaks for itself, welcome to Von Niemann Probe")
    fishSide = input("Side of stockfish: ")  # which side is hans niemann on?
    # initiate game with advantage player's side receiving "hints" based on other player's moves
    playGame(fishSide)
