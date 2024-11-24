#Tic Tac Toe
#Author : Danniboy07

import random

board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
unused_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game = True


def display_board(board):
    for row in range(3):
        for item in range(3):
            print(board[row][item], end = '')
            if item != 2:
                print('|', end = '')
        print()
        if row != 2:
            print('-'*5)
            

def bot_move(board, unused_board):
    if len(unused_board) == 0:
        return board, unused_board
    choice = random.choice(unused_board)
    row, item = board_index(choice)
    board[row][item] = 'O'
    unused_board.remove(choice)
    return board, unused_board


def board_index(choice):
    row = (choice-1) // 3
    item = (choice-1) % 3
    return row, item


def check_win(board):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for combo in wins:
        row, item = board_index(combo[0])
        owner = str(board[row][item])
        for choice in combo:
            row, item = board_index(choice)
            value = board[row][item]
            if owner != str(value):
                break
        else:
            print(owner, "WON!")
            return owner
        
print("This is the layout of the Puzzle, please enter the number appropriate to the box you want to fill in")   
display_board(board)


while game:
    
    try:
        choice = int(input("Where would you fill your X in: "))
    except:
        print("Please Enter a Valid number from 1 to 9")
        continue
    if choice > 9 or choice < 1:
        print("Please Enter a Valid number from 1 to 9")
        continue
    if choice not in unused_board:
        print("Please enter an unused number")
        continue
    unused_board.remove(choice)
    row, item = board_index(choice)
    board[row][item] = 'X'
    
    print('Loading Bot Command...')
   
    board, unused_board = bot_move(board, unused_board)
    display_board(board)
    winner = check_win(board)
    if winner == 'X':
        print('Congrats!')
        game = False
    elif winner == 'O':
        print('Try Again')
        game = False
    elif len(unused_board) == 0:
        print("It's a Draw!")
        game = False
    
    
    
    

    