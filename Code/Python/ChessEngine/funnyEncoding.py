#(c) Teddy Warner & Jack Hollingsworth - 2022

#This work may be reproduced, modified, distributed, performed, and displayed
#for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
#Copyright is retained and must be preserved. The work is provided as is;
#no warranty is provided, and users accept all liability.

#download stockfish from https://stockfishchess.org/files/stockfish_15_win_x64_avx2.zip

#this script doesn't use morse code
#number of buzzes is letter or number for each char in letter/number/letter/number move sequence

from stockfish import Stockfish #pip install stockfish
import chess #pip install python-chess
import serial
import re #pip install regex

global board
global fish
global legal
global legalMoves
global moveAdjusted
global badChars
global isMate
global morseDict
global morseMove
global port
global stockfishPath


def play_game(side):
    global board
    fish = chess.engine.SimpleEngine.popen_uci("stockfish")
    mate = False  # checkmate state declaration
    turns = 0
    board = chess.Board()

    print(f"fish playing as {side}")
    if side == "white":
        while not mate:  # if game not over, play continues
            # stockfish get best current move
            best_move = fish.play(board, chess.engine.Limit(time=1.0)).move
            board.push(best_move)  # make move in pychess to keep up with stockfish game
            print(f"whitefish plays {best_move}")
            mate = board.is_checkmate()  # returns state of checkmate
            print(f"Checkmate: {mate}")
            if mate:
                print("checkmate, stockfish victory!")
                break
            turns += 1
            # request player move
            print("black move:")
            move = input()
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move")
                continue
            mate = board.is_checkmate()  # check if player has won
            if mate:
                print("checkmate, player victory")
                break
            turns += 1
            # shows board from player perspective (white)
            print(f"board after {turns} moves:")
            print(board)

        print("")
        fish.quit()  # close Stockfish engine
        return  # return to infinite loop

    if side == "black":
        while not mate:
            # request player move
            print("white move:")
            move = input()
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move")
                continue
            mate = board.is_checkmate()  # check if player has won
            if mate:
                print("checkmate, player victory")
                break
            # stockfish get best current move
            best_move = fish.play(board, chess.engine.Limit(time=1.0)).move
            board.push(best_move)
            print(f"blackfish plays {best_move}")
            mate = board.is_checkmate()  # returns state of checkmate
            print(f"Checkmate: {mate}")
            if mate:
                print("checkmate, stockfish victory!")
                break
            turns += 1
            # shows board from player perspective (black)
            print(f"board after {turns} moves:")
            print(board)

        print("")
        fish.quit()  # close Stockfish engine
        return  # return to infinite loop

def get_player_move(move):
    global board, moveAdjusted, badChars, morseMove
    
    no_bad_chars = True #reset flag for bad characters
    legal = False #reset flag for illegal move
    char_count = 0
    num_count = 0
    
    # Check for bad characters in the move string
    for char in move:
        if char in badChars:
            print(f'{char} is ILLEGAL')
            no_bad_chars = False
        if char.isalpha():
            char_count += 1
        if char.isdigit():
            num_count += 1
    
    # Check if move string has correct formatting
    if len(move) not in [4, 5]:
        no_bad_chars = False
    if char_count == 0 or num_count == 0:
        print(f"numbers: {num_count}")
        print(f"chars {char_count}")
        no_bad_chars = False
        
    # Create move object and check legality if move string is correctly formatted
    if no_bad_chars:
        print(f"{move} is in good format")
        my_move = chess.Move.from_uci(move)
        legal = board.is_legal(my_move)
        print(f"Legal? {legal}")
    
    # Play the move if it's legal and correctly formatted, otherwise prompt for a new move
    if legal and no_bad_chars:
        fish.make_moves_from_current_position([move])
        chess_move = chess.Move.from_uci(move)
        board.push_san(move)
        print(f"player plays {move}")
    else:
        print("illegal move, input new move:")
        new_move = input()
        get_player_move(new_move)

def to_morse(move): #convert move to morse code
    ret = "" #empty morse conversion
    newConvert = "" #empty mid-conversion string
    
    for char in move:
        #print("converting " + char) #debug print
        newConvert = morseDict[char] #take key of char index in morse dict
        ret += f'{newConvert} '
        
    print(f"Morse-Converted Move: {ret}")
    return ret

def send_move(morse, ser):
    # Replace spaces in morse code with '9'
    morse = re.sub("[ ]", "9", morse)

    # Print the modified morse code for debugging
    print(f"Sending morse code: {morse}")

    # Encode each character in the morse code as UTF-8 and send it to the serial device
    for char in morse:
        encoded_char = char.encode('utf-8')
        ser.write(encoded_char)

    # Print a message indicating that the move has been sent
    print("Move sent")


# set Bluetooth port
port = "COM10"

# replace with the path to your Stockfish executable file
stockfishPath = "C:/Users/jackh/Downloads/stockfish_15_win_x64_avx2/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe"

# Morse code dictionary for all characters in chess moves
morseDict = {
    'a': '.',
    'b': '..',
    'c': '...',
    'd': '....',
    'e': '.....',
    'f': '......',
    'g': '.......',
    'h': '........',
    '1': '.',
    '2': '..',
    '3': '...',
    '4': '....',
    '5': '.....',
    '6': '......',
    '7': '.......',
    '8': '........'
}

# create a new chess board
board = chess.Board()

# characters that can't be in a legal chess move
badChars = ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "9", "0"]

# placeholder for Morse code move, filled later
morseMove = ""

# create a Stockfish engine object
fish = Stockfish(stockfishPath, depth=18, parameters={"Threads": 4, "Hash": 256, "UCI_LimitStrength": "false"})

# check if the engine version supports WDL option
print(f"WDL Accepted: {str(fish.does_current_engine_version_have_wdl_option())}")

# print the board state
print(f"Board State: {fish.get_board_visual()}")

# open the serial port for HC-06 receiving, set to 9600 baud
ser = serial.Serial(port, 9600, timeout=1)

# print message indicating the serial port is opened
print("Serial opened")

# set the flag for checkmate status
isMate = False

# play an infinite number of games
while True:
    # print message indicating the start of the game
    print("Good chess speaks for itself, welcome to Von Niemann Probe")
    # ask the player for the side of Stockfish
    fishSide = input("Which side is Hans Niemann on? ")
    # initiate the game with the advantage player's side receiving hints based on the other player's moves
    play_game(fishSide)
