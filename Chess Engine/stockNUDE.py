#barebones backup for playing stockfish, no legality, no morse, no anything: DON'T EDIT

from stockfish import Stockfish
import chess
import time

global fish; global legal; global legalMoves
global moveAdjusted; global isMate;

def playGame(side):
    global legal; global isMate;
    mate = False #checkmate state declaration
    turns = 0; i = 0 #these could be the same, but easier to keep sep = SPAGHETTIOLI CODE MOMENT
    print("fish playing as " + side)
    if side == "white":
        while mate == False: #if game not over, play continues
            bestMove = fish.get_best_move(1000) #stockfish get best current move
            fish.make_moves_from_current_position([bestMove]); 
            print("whitefish plays " + bestMove)
            if mate == True:
                print("checkmate, stockfish victory!")
                return
            turns += 1
            print("black move:") #request player move
            move = input()
            getPlayerMove(move)
            turns += 1
            print("board after " + str(turns) + " moves:")
            print(fish.get_board_visual(False)) #shows board from player perspective (white)
        print("checkmate, stockfish victory")
        return #return to infinite loop
    if side == "black":
        while mate == False:
            print("white move:")
            move = input()
            getPlayerMove(move)
            bestMove = fish.get_best_move(1000) #stockfish get best current move
            fish.make_moves_from_current_position([bestMove]); 
            print("blackfish plays " + bestMove)
            print("Checkmate: " + str(mate)) #prints state of checkmate after every fish move
            if mate == True:
                print("checkmate, stockfish victory!")
                return
            turns += 1
            print("board after " + str(turns) + " moves:")
            print(fish.get_board_visual()) #shows board from player perspective (black)
        print("checkmate, stockfish victory!")
        print("")
        return #return to infinite loop



def getPlayerMove(move):
    global legalMoves; global board; global moveAdjusted; global badChars; 
    global morseMove
    moveAdjusted = move[2:] #take last two chars of move, what appears in chess module string
    pieceToMove = str(fish.get_what_is_on_square(move[0:2])) #find which piece wants to move
    fish.make_moves_from_current_position([move])#plays legal player move in STOCKFISH

fish = Stockfish(r"C:\Users\jackh\Downloads\stockfish_15_win_x64_avx2\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")
print("WDL Accepted " + str(fish.does_current_engine_version_have_wdl_option()))
print("Board State " + fish.get_board_visual())

while True: #enables playing of inifinite games, playGame() returns to here after checkmate
    isMate = False
    print("good chess speaks for itself, welcome to Von Niemann Probe")
    print("side of stockfish:") #request side of stockfish player
    fishSide = input() #laptop user input
    playGame(fishSide)
    



