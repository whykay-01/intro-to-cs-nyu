
# 1. import module & define constant variables
# 1 a) import time (to use time.sleep(1))
# 1 b) import os (to use os.system("clear"))
# 1 c) import random (to use random.randint(0, ??))
# 1 d) create constant variables for NUM_ROWS, NUM_COLS and NUM_X
import random
import os
import time

NUM_ROWS = 10
NUM_COLS = 10
NUM_X = 5
board = []

# 2. create the board and fill it with '.'s
for row in range(NUM_ROWS):
    row_list = []
    for col in range(NUM_COLS):
        row_list.append(".")
    board.append(row_list)

# 3. assign 5 random X's to the board
# 3 a) make sure they are at unique locations
for n in range(NUM_X):
    random_row = random.randint(0, NUM_ROWS-1)
    random_col = random.randint(0, NUM_COLS-1)
    while board[random_row][random_col] == "X":
        random_row = random.randint(0, NUM_ROWS-1)
        random_col = random.randint(0, NUM_COLS-1)
    board[random_row][random_col] = "X"

# 4. print the board
os.system("clear")
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(board[row][col], end=" ")
    print()

run = True
# 5. move X's down by 1 cell (repeat until all X's reach the bottom)
# for n in range(NUM_ROWS-1):
while run == True:
    run = False
    for row in range(NUM_ROWS-2, -1, -1):
        for col in range(NUM_COLS):
            if board[row][col] == "X" and board[row+1][col] != "X":
                board[row][col] = "."
                board[row+1][col] = "X"
                run = True

    # 6. sleep for 1 second, clear the screen and print the board again
    time.sleep(0.5)
    os.system("clear")
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            print(board[row][col], end=" ")
        print()
