    # Tic - Tac - Toe
    #### Video Demo:  https://youtu.be/46-T2yNw29A
    #### Description:
    This is a Python programme that plays Tic-Tac-Toe. The game can be played with another player or against the computer. The computer chooses its movements at random in computer mode.

    The programme begins by using the board_init() function to create an empty 3x3 board. The user is then prompted to select the game mode (with another person or with the computer). The computer variable is set to True or False based on the user's selection. The computer variable is used to determine whether a player or computer needs to take a turn. If it was a computer, a random function was used to make a random move where the board was initialised with '-' and make it the current symbol. I used the defalt symbol for the letter 'O'. because I believed it would be better that way than mixing and giving another sumbol that couldn't be mixed up.

    The play_game() function contains the main game loop. It will continue until there is a winner or the board is full. The current player is switched using the current_player() function in each cycle. If the computer is the current player, a random move is made.

    Otherwise, the player is prompted to input the row and column numbers of their move. If the move is invalid (i.e., the cell is already occupied), an error notice is given, and the player is requested to enter a proper move.

    In each cycle, the check_winner() function is run to see if there is a winner. If there is, the method returns the winner's symbol (X or O), then the game loop is ended.

    Finally, the print_board() function is invoked to print the board's final state as well as the winner's name (if one exists).

    Test - suite

    The check_winner() method is tested, and it decides the winner of the Tic Tac Toe game depending on the present state of the board. It runs many situations in which X and O are the winners and expects the function to return the proper winner.

    The test_play_game() function validates the play_game() function, which mimics game play by taking the board, the player's turn, and a boolean flag indicating whether or not to display the board. It runs many situations and expects the function to deliver the correct answer.

    The current_player() method, which yields the current player's turn, is tested by the test_current_player() function. It runs through various scenarios, expecting the function to return the correct player.

    The board_init() method, which initialises the board to an empty state, is tested by the test_board_init() function. It runs a certain scenario and anticipates the function returning the correct board.

    The print_board() function, which prints the current state of the board, is tested by the test_print_board() function. It runs a certain scenario and anticipates the function returning None.

    Overall, the programme is a rudimentary implementation of the Tic-Tac-Toe game that can be used as a starting point for more complex implementations.

    To Run it just run the python and project name
    if you want to play with computer press one else press 2 for against 2.

    Thank you.
