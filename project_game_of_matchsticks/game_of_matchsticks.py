"""
COMP.CS.100 Programming 1
Tran Sy Minh, minh.s.tran@tuni.fi, student id 050359358
Project 1: Create a modern computer version of 'game of matchsticks'. The idea of 
the game was to lay 21 (match)sticks on the table between two players and then the 
players would take turns to pick 1–3 sticks from the pile. The player who was forced 
to take the last stick lost the game.
"""

def main():
    num_of_sticks = 21
    current_player = 1
    win = False
    print("Game of sticks")

    while not win:
        turn = int(input(f"Player {current_player} enter how many sticks to remove: "))

        if turn > 3 or turn < 1:
            print("Must remove between 1-3 sticks!")
            continue
        num_of_sticks -= turn

        if num_of_sticks <= 0:
            win = True
            print(f"Player {current_player} lost the game!")
        else:
            print(f"There are {num_of_sticks} sticks left")       
            if current_player == 1:
                current_player += 1
            else:
                current_player -= 1
    
if __name__ == "__main__":
    main()
