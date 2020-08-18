#import numpy
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def valid(brd,num,pos):
    # here num is the number we wanna check if it exists or not in that row/column/box
    # pos[0]=x , pos[1]=y values  for find empty function
    # check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i]==num and pos[1]!=i :
            return False
    #check column
    for i in range(len(brd[0])):
        if brd[i][pos[1]]==num and pos[0]!=i :
            return False
    #check small box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3+3):
            if brd[i][j]==num and (i,j) != pos:
                return False

    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def print_board(brd):
    for i in range(len(brd)):
        if i%3==0 and i!=0:
            print("----------------------")

        for j in range(len(brd[0])):
            if j%3==0 and j!=0:
                print("|", end="")

            if j==8:
                print(brd[i][j])
            else :   
                print(str(brd[i][j]) + " ", end="")

#print_board(board)

def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None


print_board(board)
solve(board)
print("___________________")
print_board(board)
