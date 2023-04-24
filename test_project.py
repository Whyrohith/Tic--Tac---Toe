from project import check_winner , current_player , print_board , board_init ,play_game
import io
import sys
import pytest


def main():
    test_print_board()
    test_current_player()
    test_check_winner()
    test_play_game()
    test_board_init()



def test_print_board():
    board = [['-','-','O'],['-','O','X'],['O','-','X']]
    assert print_board(board ,'X') == None


def test_current_player():
    assert(current_player('X')) == 'O'
    assert(current_player('O')) == 'X'

def test_check_winner():
    board = [['X','-','O'],['X','O','-'],['X','O','-']]
    assert(check_winner(board,'X')) == 'X'
    board = [['X','-','O'],['-','X','O'],['X','O','O']]
    assert(check_winner(board,'O')) == 'O'
    board = [['X','-','O'],['-','X','O'],['-','O','X']]
    assert(check_winner(board,'X')) == 'X'
    board = [['-','-','O'],['-','O','X'],['O','-','X']]
    assert(check_winner(board,'O')) == 'O'

def test_play_game():
    board = [['X','-','O'],['X','O','X'],['X','-','X']]
    assert play_game(board,'X',False) == 1
    board = [['-','-','O'],['X','O','O'],['X','-','O']]
    assert play_game(board,'O',False) == 1


def test_board_init():
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    assert (board_init()) == board



if __name__ == "__main__":
    main()