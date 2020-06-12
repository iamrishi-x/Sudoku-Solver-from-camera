"""
File    : sudoku_Algorithm.py
purpose : 1.Contain main algorithm
          Just used for temporary purpose after it i have to switch it to AI for
          sudoku solving
Author  : rishi bagul
Email   : rushibagul4444@gmail.com
Date    : 5 June 2020
"""
print("Sudoku algorithm ! by rishi bagul")
# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7],
# ]
def print_board(board):
    print('')
    flag = 1;flag1 = 0
    for i in board:
        if flag1 == 3:
            print('-'*34)
            flag1=0
        for val in i:
            if flag != 3:
                print(val,end="  ")
            else:
                print(val," |",end="  ")
                flag=0
            flag += 1
        flag1+=1
        print('')
    print('')
def check_for_empty(board):  #check for empty position
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None
def check_validation(board,val,position):
    #check for row
    for i in board[position[0]]:
        if i == val:
            return 0
    #check for col
    for i in range(len(board)):
        if board[i][position[1]] == val:
            return 0
    #check in local square
    box=[]
    temp=[]
    for i in range(len(board)):
        if i%3 == 0:
            temp=[]
            box.append(temp)
        temp.append(i)
    #box = [[0,1,2],[3,4,5],[6,7,8]]
    for i in box[position[0]//3]:
        for j in box[position[1]//3]:
            if board[i][j] == val:
                return 0
    return 1
def solve(board):   #main backtracking algorithm
    find = check_for_empty(board)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if check_validation(board,i,(row,col)):
            board[row][col] = i
            if solve(board) :
                return True
            board[row][col]=0
    return False
#
# print_board(board)
# if solve(board) :
#     print('#'*34+'\nSolved ans is : ')
#     print_board(board)
# else:
#     print_board("program is wrong")