

import random



def display_board(board):
    print('\n'*100)
    print('     |     |')
    print('  '+ board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  '+ board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  '+ board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: do you want to assign X or O?').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(b, mark):

    for i in range(1,4):
        if b[i] == b[i+3] == b[i+6]==mark: return True #all the columns are being checked
    for i in range(1,8,3):
        if b[i] == b[i+1] == b[i+2]==mark: return True #all the rows are being checked
    for i in range(1,4,2):
        if i == 1:
            if b[i] == b[i+4] == b[i+8]==mark: return True #first diagonal (1,5,9) is being checked
        else:
            if b[i] == b[i+2] == b[i+2]==mark: return True #second diagonal (7,5,3) is being checked
    return False

def choose_first():
    
    if random.randint(0,1) == 0:
        return 'player 2'
    else:
        return 'player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for item in range(1,10):
        if space_check(board,item):
            return False
    return True

def player_choice(board):
        next_position = 0
        
        while next_position not in range(1,10) or space_check(board,next_position)!=True:
            
            next_position = int(input("Enter a position between 1-9::"))

        return next_position

def replay():
 
    return input("Do you want to play more or not ENTER YES OR NO::").upper().startswith('Y')

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()

    print(turn + ' will go first')

    play_game = input("Ready to play the game? y or n::")

    if(play_game == 'y'):
        game_on = True
    else:
        game_on  = False
    
    while game_on:

        if turn == 'player 1':
            #show the board
            display_board(the_board)
            print(turn + "'s turn-->")
            #choose position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player 1 has won')
                game_on = False
            else:
                if(full_board_check(the_board)):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = "player 2"
        #Player 1 Turn
        else:
            #show the board
            display_board(the_board)
            print(turn + "'s tunr-->")
            #choose position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            #check if they won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player 2 has won')
                game_on = False
            else:
                if(full_board_check(the_board)):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = "player 1"
    if not replay():
        break