from stockfish import Stockfish
import chess
import time

global board; global fish
global legal; global legalMoves
global moveAdjusted; global badChars
global isMate; global morseDict
global morseMove

morseDict = { 'a':'.-', 'b':'-...',
   'c':'-.-.', 'd':'-..', 'e':'.',
   'f':'..-.', 'g':'--.', 'h':'....',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..'} #morse dict for all chars in chess moves

board = chess.Board(); #create chess board object
badChars = ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
"9", "0"] #chars that can't be in a legal chess move
morseMove = "" #placeholder for morse code move, filled later

def playGame(side):
    global legal; global legalMoves
    global board; global isMate; global morseMove; 
    mate = False #checkmate state declaration
    turns = 0; i = 0 #these could be the same, but easier to keep sep = SPAGHETTIOLI CODE MOMENT
    board = chess.Board(); #declare chess board object in chess module
    print("fish playing as " + side)
    if side == "white":
        while mate == False: #if game not over, play continues
            bestMove = fish.get_best_move(1000) #stockfish get best current move
            fish.make_moves_from_current_position([bestMove]); 
            chessMove = chess.Move.from_uci(bestMove)
            board.push_san(bestMove)
            print("whitefish plays " + bestMove)
            morseMove = toMorse(bestMove) #call morse conversion of fish move
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
            turns += 1
            print("board after " + str(turns) + " moves:")
            print(fish.get_board_visual(False)) #shows board from player perspective (white)
        print("checkmate, stockfish victory")
        return #return to infinite loop
    if side == "black":
        legalMoves = str(board.legal_moves) #convert list to string
        while mate == False:
            print("white move:")
            move = input()
            getPlayerMove(move)
            bestMove = fish.get_best_move(1000) #stockfish get best current move
            fish.make_moves_from_current_position([bestMove]); 
            chessMove = chess.Move.from_uci(bestMove)
            board.push_san(bestMove)
            print("blackfish plays " + bestMove)
            morseMove = toMorse(bestMove) #get string of morse-converted move, not in use
            mate = board.is_checkmate() #returns state of checkmate
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
    legalMoves = str(legalMoves); legal = False
    legalMoves = legalMoves.replace("x", "") #remove all x's from legal move list
    print(legalMoves); newMove = ""; playerMove = ()
    for char in move: #check if badChars exist in move
        i = 0 #reset iterating var
        while i < len(badChars):
            badChar = badChars[i]
            if char == badChar:
                print(char + ' is ILLEGAL')
                print("outside chess bounds, input other move:")
                moveAdjusted = ""
                newMove = input()
                getPlayerMove(newMove)
                return #back to game, move already been done
            #print(char + " is not " + badChars[i]) #for debugging illegal char detection
            i += 1
        #print(char + ' is legal')
    moveAdjusted = move[2:] #take last two chars of move, what appears in chess module string
    pieceToMove = str(fish.get_what_is_on_square(move[0:2])) #find which piece wants to move
    print(pieceToMove) #print piece that is moving
    if pieceToMove == "None": #ask for new move if origin square is empty
        print("nothing on square " + moveAdjusted + ", new move?")
        newMove = input()
    pieceAdjusted = translatePiece(pieceToMove) #gets move as it exists in LegalMoves list
    if str(pieceAdjusted) in str(legalMoves):
        legal = True
    else:
        legal = False
    print("Legal? " + str(legal))
    if legal == True:
        fish.make_moves_from_current_position([move])#plays legal player move in STOCKFISH
        print("move registered in stockfish")
        chessMove = chess.Move.from_uci(move) #load legal player move
        board.push_san(move) #send player move to board tracker
        print("player plays " + move)
        legal = False
        return
    else:
        print("illegal move, input other move:")
        playerMove = input()
        getPlayerMove(playerMove)
        return #back to game, move already done

def translatePiece(pieceID): #bug: bad pawn calls with final pos that other pieces have crahses
    ret = '' #empty return string
    global moveAdjusted
    if "PAWN" in pieceID: #check if piece name in name of piece that want to move
        ret = moveAdjusted #just desired coordinate, as pawn doesn't have any identifying letter
        print("Move Desired: " + ret) #prints desired move
        return ret #returns desired move
    elif "KNIGHT" in pieceID:
        ret = "N" + moveAdjusted
        print("Move Desired: " + ret)
        return ret
    elif "ROOK" in pieceID:
        ret = "R" + moveAdjusted
        print("Move Desired: " + ret)
        return ret
    elif "QUEEN" in pieceID:
        ret = "Q" + moveAdjusted
        print("Move Desired: " + ret)
        return ret
    elif "KING" in pieceID:
        ret = "K" + moveAdjusted
        print("Move Desired: " + ret)
        return ret
    elif "BISHOP" in pieceID:
        ret = "B" + moveAdjusted
        print("Move Desired " + ret)
        return ret

def toMorse(move): #convert move to morse code
    ret = "" #empty morse conversion
    newConvert = "" #empty mid-conversion string
    for char in move:
        #print("converting " + char) #debug print
        newConvert = morseDict[char] #take key of char index in morse dict
        ret += newConvert + ' ' #add morse for new char to morse string
    print("Morse-Converted Move: " + ret)
    return ret
      
fish = Stockfish(r"C:\Users\jackh\Downloads\stockfish_15_win_x64_avx2\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")
print("WDL Accepted " + str(fish.does_current_engine_version_have_wdl_option()))
print("Board State " + fish.get_board_visual())

while True: #enables playing of inifinite games, playGame() returns to here after checkmate
    isMate = False
    print("good chess speaks for itself, welcome to Von Niemann Probe")
    print("side of stockfish:") #request side of stockfish player
    fishSide = input() #laptop user input
    playGame(fishSide)
    



