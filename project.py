import random

def main():
    current = ''
    board = board_init()
    current_player(current)
    mode = int(input("Enter 1 for Play with computer or 2 for players mode: "))
    if mode == 1:
        computer = True
    else:
        computer = False
    play_game(board,current,computer)



def print_board(board,current):
    # print the board with 3*3 grid
     print(f"{current} player turn")
     print()
     print('   0   1   2')
     print("  -----------")
     for i, row in enumerate(board):
        print(f"{i}  {' | '.join(row)}")
        print("  -----------")
     print()


def current_player(current):
    # swith the current player
    if current == 'X':
        current = 'O'
        return current
    else:
        current = 'X'
        return current



def check_winner(board,current):
    # check the winner and return the winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == current:
            return current
        elif board[0][i] == board[1][i] == board[2][i] == current:
            return current
    if board[0][0] == board[1][1] == board[2][2] == current:
        return current
    elif board[0][2] == board[1][1] == board[2][0] == current:
        return current




def play_game(board,current,computer):
    while True:
        if check_winner(board,current) == current:
            print_board(board , current)
            print(f"{current} player won")
            return 1
        current =  current_player(current)
        while True:
            print_board(board,current)
            try :
                if computer and current == 'O':
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if board[row][col] == '-':
                        board[row][col] = current
                        break
                else:
                    col = int(input("Enter the column number: "))
                    row = int(input("Enter the row number: "))
                print()
                if board[row][col] == '-' and current == 'X':
                    board[row][col] = 'X'
                    break
                elif board[row][col] == '-' and current == 'O':
                    board[row][col] = 'O'
                    break
                else :
                    print("Invalid Input")
            except:
                print("Invalid Move")
                pass



def board_init():
    board = []
    for i in range(3):
        board.append([])
        for _ in range(3):
            board[i].append('-')
    return board




if __name__ == "__main__":
    main()