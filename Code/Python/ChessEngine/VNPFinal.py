#(c) Teddy Warner & Jack Hollingsworth - 2022

#This work may be reproduced, modified, distributed, performed, and displayed
#for any purpose, but must acknowledge Teddy Warner  & Jack Hollingsworth.
#Copyright is retained and must be preserved. The work is provided as is;
#no warranty is provided, and users accept all liability.

#download stockfish from https://stockfishchess.org/files/stockfish_15_win_x64_avx2.zip

from stockfish import Stockfish #pip install stockfish
import chess #pip install python-chess
import time
import serial
import re #pip install regex

global board; global fish
global legal; global legalMoves
global moveAdjusted; global badChars
global isMate; global morseDict
global morseMove; global port 
global stockfishPath

port = "COM10" #set bluetooth port

stockfishPath = "C:/Users/jackh/Downloads/stockfish_15_win_x64_avx2/stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe" #replace with the path to your Stockfish exe. Note - the path may only contain forward slashes, no backslashes.

morseDict = { 'a':'.-', 'b':'-...',
   'c':'-.-.', 'd':'-..', 'e':'.',
   'f':'..-.', 'g':'--.', 'h':'....',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..'} #morse dict for all chars in chess moves, other characters not needed here

board = chess.Board(); #create chess board object

badChars = ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"9", "0"] #chars that can't be in a legal chess move

morseMove = "" #placeholder for morse code move, filled later

fish = Stockfish(r"{0}".format(stockfishPath), 
depth=18, parameters={"Threads": 4, "Hash": 256, "UCI_LimitStrength": "false"}) #stockfish object declaration, can regulate strength
print("WDL Accepted " + str(fish.does_current_engine_version_have_wdl_option()))
print("Board State " + fish.get_board_visual()) #prints unicode image of current board state

ser = serial.Serial(port, 9600, timeout = 1) #open com port of hc-06 receiving, set to 9600 baud
print("serial opened")

def playGame(side):
    global legal; global legalMoves
    global board; global isMate; global morseMove; 
    mate = False #checkmate state declaration
    turns = 0; i = 0 #these could be the same, but easier to keep sep = SPAGHETTIOLI CODE MOMENT
    board = chess.Board(); #declare chess board object in pychess module, for checking legality of moves
    print("fish playing as " + side)
    if side == "white":
        while mate == False: #if game not over, play continues
            bestMove = fish.get_best_move(1000) #stockfish get best current move
            fish.make_moves_from_current_position([bestMove]); 
            chessMove = chess.Move.from_uci(bestMove) #create chessMove object in pychess, push it to board on next line
            board.push_san(bestMove) ##make move in pychess to keep up with stockfish game
            print("whitefish plays " + bestMove)
            morseMove = toMorse(bestMove) #call morse conversion of fish move
            sendMove(morseMove) #call to move sending function, arg is stockfish best move
            mate = board.is_checkmate() #returns state of checkmate
            print("Checkmate: " + str(mate)) #prints state of checkmate after every fish move
            if mate == True:
                print("checkmate, stockfish victory!")
                return
            turns += 1
            legalMoves = str(board.legal_moves) #convert list to string
            print("black move:") #request player move
            move = input()
            getPlayerMove(move)
            mate = board.is_checkmate() #check if player has won
            if mate == True:
               print("checkmate, player victory")
               return
            turns += 1
            print("board after " + str(turns) + " moves:")
            print(fish.get_board_visual(False)) #shows board from player perspective (white)
        print("")
        return #return to infinite loop
    if side == "black":
        legalMoves = str(board.legal_moves) #convert list to string
        while mate == False:
            print("white move:")
            move = input()
            getPlayerMove(move)
            mate = board.is_checkmate() #check if player has won
            if mate == True:
               print("checkmate, player victory")
               return
            bestMove = fish.get_best_move(1000) #stockfish get best current move
            fish.make_moves_from_current_position([bestMove]); 
            chessMove = chess.Move.from_uci(bestMove)
            board.push_san(bestMove)
            print("blackfish plays " + bestMove)
            morseMove = toMorse(bestMove) #get string of morse-converted move, not in use
            sendMove(morseMove) #send morse move via bluetooth
            mate = board.is_checkmate() #returns state of checkmate
            print("Checkmate: " + str(mate)) #prints state of checkmate after every fish move
            if mate == True:
                print("checkmate, stockfish victory!")
                return
            turns += 1
            print("board after " + str(turns) + " moves:")
            print(fish.get_board_visual()) #shows board from player perspective (black)
        print("")
        return #return to infinite loop

def getPlayerMove(move):
    global board; global moveAdjusted; global badChars; global morseMove
    noBadChars = True #reset no bad chars bool
    legal = False #reset illegal bool
    charCount = 0; numCount = 0
    for char in move: #check if badChars exist in move
        i = 0 #reset iterating var
        while i < len(badChars):
            badChar = badChars[i]
            if char == badChar:
                print(char + ' is ILLEGAL')
                noBadChars = False #set bool to reflect bad char
            if char.isalpha() == True:
                charCount += 1 #reflect that at least 1 char in string
            if char.isdigit() == True:
                numCount += 1 #reflect that at least one number in string
            i += 1
            #print(char + "is legal") #debug bad chars function
    if len(move) != 4 and len(move) != 5: #solve edge case where small string doesn't break other rules
        noBadChars = False;
    if charCount == 0 or numCount == 0:
        print("numbers: " + str(numCount))
        print("chars " + str(charCount))
        noBadChars = False #change bool to reflect bad formatting
    if noBadChars == True: #only creative move objects if correct formatting
        print(move + " is good format")
        myMove = chess.Move.from_uci(move) #create move object frmo current player move, used to check legality
        legal = board.is_legal(myMove) #checks legality of desired move
        print("Legal? " + str(legal))
    if legal and noBadChars: #move can only happen if legal and doesn't contain illegal chars
        fish.make_moves_from_current_position([move])#plays legal player move in STOCKFISH
        chessMove = chess.Move.from_uci(move) #load legal player move
        board.push_san(move) #send player move to board tracker
        print("player plays " + move)
        return #back to game loop
    else:
        print("illegal move, input new move:")
        newMove = input()
        getPlayerMove(newMove)
        return #back to game loop

def toMorse(move): #convert move to morse code
    ret = "" #empty morse conversion
    newConvert = "" #empty mid-conversion string
    for char in move:
        #print("converting " + char) #debug print
        newConvert = morseDict[char] #take key of char index in morse dict
        ret += newConvert + ' ' #add morse for new char to morse string
    print("Morse-Converted Move: " + ret)
    return ret

def sendMove(morse):
    morse = re.sub("[ ]", "9", morse)
    print(morse) #print morse move with spaces replaced with 9 - easier to parse on arduino side as empty bytes hard to work with
    for char in morse:
        tempChar = char.encode() #temporary placeholder set to current char in morse move
        ser.write(tempChar) #send individual character of final morse message encoded in utf-8
    print("sent move")
    return

while True: #enables playing of inifinite games, playGame() returns to here after checkmate, resets all local values
    isMate = False
    print("good chess speaks for itself, welcome to Von Niemann Probe")
    print("side of stockfish:") #request side of stockfish player
    fishSide = input() #which side is hans niemann on?
    playGame(fishSide) #initiate game with advantage player's side receiving "hints" based on other player's moves