board = ['1','2','3','4','5','6','7','8','9']
print(any([item.isdigit() for item in board]))

def show_board():
    print(f"""
    {board[0]} | {board[1]} | {board[2]}
    {board[3]} | {board[4]} | {board[5]}
    {board[6]} | {board[7]} | {board[8]}
    """)

def win_check(mark):
    if (board[0] == board[1] == board[2] == mark or
    board[3] == board[4] == board[5] == mark or
    board[6] == board[7] == board[8] == mark or
    board[0] == board[3] == board[6] == mark or
    board[1] == board[4] == board[7] == mark or
    board[2] == board[5] == board[8] == mark or
    board[0] == board[4] == board[8] == mark or
    board[2] == board[4] == board[6] == mark):
        print(f"The player who played with {mark} has won! Congrats!")
        return True
    else:
        return False

def player_1():
    show_board()
    player_1 = input("Select the position for x: ")
    while player_1 not in board:
        print("Select a position from the board")
        player_1 = input("Select the position for x: ")
    board[int(player_1) - 1] = 'x'

def player_2():
    show_board()
    player_2 = input("Select the position for o: ")
    while player_2 not in board:
        print("Select a position from the board")
        player_2 = input("Select the position for o: ")
    board[int(player_2) - 1] = 'o'

def check_draw():
    if any([item.isdigit() for item in board]) == False:
        game_has_finished = True
        print("The game has ended in a draw!")
        return True

game_has_finished = False
while not game_has_finished:
    player_1()
    if win_check('x'):
        game_has_finished = True
        show_board()
        print("Player 1 has won!")
    if check_draw():
        break
    if not game_has_finished:
        player_2()
        if win_check('o'):
            game_has_finished = True
            show_board()
            print("Player 2 has won!")