from typing import Optional
from support import *


def play_game() -> None:
	pass

def num_hours() -> float:
    """
    Returns the hours that the programmer spent on the code

    Parameters:
        None
    
    Returns: 
        The number of hours spent to write this code
    """
    return float(12.5)

def create_empty_board(board_size: int) -> float:
    """ 
    Creates a squared board with the required board_size 

    Parameters: 
        board_size: The desired lenght of the board (in units)

    Returns: 
        The board as a list of strings

    Pre-conditions: 
        The board size must be between 3 and 9 inclusive
    """
    board = []
    if board_size >= 2 and board_size < 10:
        for i in range(board_size):
            board.append(str(EMPTY_SQUARE*board_size))
        return board
    
    else:
        print("The number must be between 3 and 9")

def get_square(board: list[str], position:tuple[int,int]) -> str:
    """
    Returns the character/status of a cell in board

    Parameters:
        board: The board in the form of a list
        position: The coordinate to be retrieved
    
    Returns:
        The string/character corresponding to that cell

    Pre-conditions:
        The coordinates must exist within the board
    """   
    return board[position[0]][position[1]]

def change_square(board: list[str], position: tuple[int, int], new_square: str) -> None:
    """
    Changes a character in the player's board

    Parameters:
        board: The board in the form of a list
        position: The position to be changed
        new_square: The new character for that cell
    
    Returns:
        Mutates the board specified

    Pre-conditions:
        The position must be a 2 integers tuple
    """
    row = list(board[position[0]])
    row[position[1]] = new_square
    new_row = ""

    for i in row:
        new_row += i
    board[position[0]] = new_row
    
def coordinate_to_position(coordinate: str) -> tuple:
    """
    Converts a 'string-number' coordinate to a two-integer tuple position

    Parameters:
        coordinate: a 'string-number' coordinate

    Returns:
        A tuple (#,#) with two integers
    
    Pre-conditions:
        The coordinate must be 2 characters long string
        The first character must be a letter and the second a number
    """
    coordinate_map = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I": 8}
    column = coordinate[0]
    return(int(coordinate[1]) - 1, coordinate_map.get(column))

def can_place_ship(board: list[str], ship: list[tuple[int,int]]) -> bool:
    """
    Evaluates and determines if it is possible to put a ship in a board

    Parameters:
        board: the board to be evaluated
        ship: the coordinates of the ship to be evaluated
    
    Returns:
        True if it is possible to put the ship or false otherwise

    Pre-conditions:
        All the positions must exist in the board
    """
    for unit in ship:
        if board[unit[0]][unit[1]] != "~":
            return False
        else:
            return True

def place_ship(board: list[str], ship: list[tuple[int,int]]) -> None:
    """
    Change the empty-type characters on the board for active ships charaters
    
    Parameters:
        board: the board to be modified
        ship: the positions of the ship to be replaced as a list of tuples

    Returns:
        mutates the board for active ships where selected
    
    Pre-conditions: 
        The desired coordinates must be empty according to the function 'can_place_ship'
    """
    if can_place_ship(board, ship) == True:
        for ships in ship:
            change_square(board, ships, ACTIVE_SHIP_SQUARE)


def attack(board: list[str], position: tuple[int, int]) -> None:
    """
    Evaluates if there is a ship in a coordinate and
    change it to a dead ship character

    Parameters:
        board: the enemy's board to attack
        position: the position to try attacking (as a tuple)

    Returns:
        Mutates the enemy's board to a dead ship where a active ship was before

    Pre-conditions:
        The position must exist in the board
    """
    if board[position[0]][position[1]] == ACTIVE_SHIP_SQUARE:
        change_square(board, position, DEAD_SHIP_SQUARE)
    elif board[position[0]][position[1]] == EMPTY_SQUARE:
        change_square(board, position, MISS_SQUARE)

def display_board(board: list[str], show_ships: bool) -> None:
    """
    Creates a user-friendly way of reading the game and its status
    Displays or not the active ships

    Parameters:
        board: the board to be displayed
        show_ships: True or False depending if we want to show the active ships
    
    Returns:
        Prints a indice row and every line of the board in a new line
        If show_ships is false, it hide the active ships
    """
    row_index = 1
    #prints the upper x-axis of the game board
    print(" /ABCDEFGHI"[0:(len(board)+2)])
    for row in board:
        temporal_row = ""
        for square in row:
            
            if show_ships == False and square == ACTIVE_SHIP_SQUARE:
                #creates a fake row to hide the active ships
                square = "~"
                temporal_row += square
            else:
                temporal_row += square  

        #prints the y-axis index plus the real or fake row          
        print(str(row_index) + "|"+ temporal_row)
        row_index += 1

def get_player_hp(board: list[str]) -> int:
    """
    Count the active ships and returns that as the lives of the player
    
    Parameters:
        Board: The board of the player to be checked
        
    Returns:
        The lifes remaining/active of the player as a integer
    """
    life = 0
    for row in board:
        for cell in row:
            if ACTIVE_SHIP_SQUARE == cell:
                life += 1
    return int(life)

def print_life(board: list[str], player: str) -> None:
    """
    Prints in a explanatory sentence the remaining lives of the player
    
    Parameters:
        board: to use on get_player_hp
        player: the player whose lives correspond to
    
    Returns:
        The informative message printed
    """
    if get_player_hp(board) == 1:
        print(player + ": " + str(get_player_hp(board)) + " life remaining")
    else: 
        print(player + ": " + str(get_player_hp(board)) + " lives remaining")

def display_game(p1_board: list[str], p2_board: list[str], show_ships: bool) -> None:
    """
    Displays the life of the player and both players boards
    
    Parameters:
        p1_board: the board of the first player
        p2_board: the board of the second player
        show_ships: a true or false if the ships want to be displayed or not
    
    Returns:
        Print the life status of the players and its boards 
    """

    #Player 1 game
    print_life(p1_board, "PLAYER 1")
    display_board(p1_board, show_ships)

    #Player 2 game
    print_life(p2_board, "PLAYER 2")
    display_board(p2_board, show_ships)

def is_valid_coordinate(coordinate: str, board_size: int)-> tuple[bool, str]:
    """
    Checks if a coordinate given by the user is valid or not
    
    Parameters:
        coordinate: A string containing the desired coordinate
        board_size: the size of the board to be checked
    Returns:
        If the coordinate is valid, a True statement for further validation
        contrary, a False statement and a message of the error
    """
    if len(coordinate) != 2:
        return (False, INVALID_COORDINATE_LENGTH)
    
    elif coordinate[0] not in "ABCDEFGHI"[:(board_size)]:
        return (False, INVALID_COORDINATE_LETTER)
    
    elif (coordinate[1]) not in str(list(range(1,board_size+1))):
        return (False, INVALID_COORDINATE_NUMBER)  
          
    else:
        return (True, "") 
    
def is_valid_coordinate_sequence(coordinate_sequence: str, ship_length: int, board_size: int) -> tuple[bool, str]:
    """
    Checks if the ship coordinates input by the user are valid or not
    
    Parameters:
        coordinate_sequence: the user's desired coordinates to place the ship
        ship_length: the expected length of the ship provided by the user
        board_size: the board size to check validity of coordinates
        
    Returns:
        If valid, a True statement for further validation
        otherwise, a False statement and a message of the error
    """
    coordinates = coordinate_sequence.split(",")

    if len(coordinates) == ship_length:
        for coordinate in coordinates:
            if is_valid_coordinate(coordinate, board_size)[0] == False:
                return (is_valid_coordinate(coordinate, board_size))           
        return(True, "")
    
    else:
        return(False, INVALID_COORDINATE_SEQUENCE_LENGTH)
    
def build_ship(coordinate_sequence:str) -> list[tuple[int,int]]:
    """
    Convert a full string chain with coordinates to a list of tuples positions

    Parameters: 
        coordinate_sequence: a text with the desired ship coordinates
    
    Returns:
        The positions that the ship occupy in the board

    Pre-conditions:
        The desired coordinates must be valid
    """
    coordinates = coordinate_sequence.split(",")
    real_coordinates = []

    for coordinate in coordinates:
        real_coordinates.append(coordinate_to_position(coordinate))
    return real_coordinates    
   
def setup_board(board_size: int, ship_sizes: list[int]) -> list[str]:
    """
    Creates the board and prompt the player for desired ship coordinates
    If the coordinates are valid, creates the ships in the player's board

    Parameters:
        board_size: the desired size of the board to create
        ship_sizes: the sizes of the ships use on the game
    
    Returns:
        The board with ships positioned to be used on the game
    """
    board = create_empty_board(board_size)

    for size in ship_sizes:
        ship_allocated = False
        while (ship_allocated == False):
            display_board(board, True)
            
            #Prompt the user for the ship coordinates
            coordinate_sequence = input("Enter a comma separated list of " + str(size) +  " coordinates: ")
            
            #Checks the validity of the coordinates
            if (is_valid_coordinate_sequence(coordinate_sequence,size,board_size)[0]) == True:   
                if can_place_ship(board, build_ship(coordinate_sequence)) == True:

                    #Allocates the ships
                    place_ship(board,build_ship(coordinate_sequence))
                    ship_allocated = True
                else:
                    print(INVALID_SHIP_PLACEMENT)

            #Inform the user of invalid coordinates
            elif (is_valid_coordinate_sequence(coordinate_sequence,size,board_size)[0]) == False:
                print(is_valid_coordinate_sequence(coordinate_sequence,size,board_size)[1])
    return board
  
def get_winner(p1_board: list[str], p2_board: list[str])-> Optional[str]:
    """
    Checks if any player has active ships remaining

    Parameters:
        p1_board: the board of the first player to check over
        p2_board: the board of the second player to check over
 
    Returns:
        If winner, a string "Player 1" or "Player 2" depending on the winner
    """
    if get_player_hp(p1_board) == 0:
        return (PLAYER_TWO) 
    elif get_player_hp(p2_board) == 0:
        return (PLAYER_ONE) 

def make_attack(target_board):
    """
    Attemps to attack the enemy's board
    If succesful, it will turn an active ship to a dead ship
    If not, it will raise a miss square
    
    Parameters: 
        target_board: the enemy's board to attack
    
    Returns:
        Changes the character/status of a cell in the enemy's board
    """
    attack_made = False
    while (attack_made == False):
        coordinate_to_attack = input("Enter a coordinate to attack: ")
    
        if is_valid_coordinate(coordinate_to_attack,len(target_board))[0] == True:
            position = coordinate_to_position(coordinate_to_attack)
            attack(target_board, position)
            attack_made = True

        elif is_valid_coordinate(coordinate_to_attack,len(target_board))[0] == False:
            print(is_valid_coordinate(coordinate_to_attack,len(target_board))[1])
        
    
def play_game():
    """
    Prompt the user for a board size and ship_sizes
    Prompt the user for the ship coordinates
    Users can attack each other until there is a winner
    When a winner, it displays the winner and finish the game

    Parameters: 
        None, all the values are given by the players
    
    Returns:
        None, only executes the logic of the game
    """
    #Set up of board
    board_size = int(input("Enter board size: "))
    ship_sizes = (input("Enter ships sizes: ")).split(",")
    int_ship_sizes = []
    for size in ship_sizes:
        int_ship_sizes.append(int(size))

    #Set up of ships
    print("--------------------")
    print("PLAYER 1 SHIP PLACEMENT:")
    player_one_board = setup_board(board_size, int_ship_sizes)
    print("PLAYER 2 SHIP PLACEMENT:")
    player_two_board = setup_board(board_size, int_ship_sizes)
    
    #starts the main loop of the game
    winner = False
    while winner == False:
        print("\n-------Next_Turn--------")
        display_game(player_one_board, player_two_board, False)

        #Player 1 attack turn
        print("\nPLAYER 1's turn!")
        make_attack(player_two_board)

        #Check if player 1 is the winner
        if get_winner(player_one_board,player_two_board) == PLAYER_ONE:
            print("\n=========\nGAME OVER\n=========")
            print("PLAYER 1 won!")
            winner = True
            break

        print("\n-------Next_Turn--------")
        display_game(player_one_board, player_two_board, False)

        #Player 2 attack turn
        print("\nPLAYER 2's turn!")
        make_attack(player_one_board)

        #Check if player 2 is the winner
        if get_winner(player_one_board,player_two_board) == PLAYER_TWO:
            print("\n=========\nGAME OVER\n=========")
            print("PLAYER 2 won!")
            winner = True

    #display the final state of the game        
    display_game(player_one_board, player_two_board, True)

if __name__ == "__main__":
    play_game()