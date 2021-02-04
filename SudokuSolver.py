"""
#Sample Problem
sudoku = [[0,2,0,1,5,4,3,9,6],
          [9,6,5,3,2,7,1,4,8],
          [3,4,1,6,8,9,7,5,2],
          [5,9,3,4,6,0,2,0,1],
          [5,0,2,5,1,3,6,0,9],
          [6,1,0,9,0,2,4,3,5],
          [0,0,6,3,3,5,9,1,4],
          [1,5,4,7,9,6,8,2,3],
          [2,3,9,8,4,1,5,6,7]]
"""


sudoku = [[0 for j in range(9)] for i in range(9)]

#Print the Sudoku
def printSudo():
    global sudoku
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-----------------------')
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + ' ', end='')
    return
    
          
#Check the possibilty of num to be placed at [r][c] position
def checkPlace(r,c,num):
    global sudoku
    for i in range(9):
        if sudoku[r][i] == num:
            return False
    for i in range(9):
        if sudoku[i][c] == num:
            return False
    x = (c//3)*3
    y = (r//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[y+i][x+j] == num:
                return False
    return True

#Solve the Sudoku
def solve():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1,10):
                    if checkPlace(i, j, num):
                        sudoku[i][j] = num
                        solve()
                        sudoku[i][j] = 0
                return
    print("\nThe solution is :\n")
    printSudo()
    exit()

#Input the Problem
def inSudo():
    global sudoku
    print("Enter the Sudoku Grid (Row Wise)(0 for blank cell)\n")
    for i in range(9):
        for j in range(9):
            element = int(input(f"Element for row {i + 1} and column {j + 1} : \t"))
            sudoku[i][j] = element if element >= 0 and element < 10 else 0
        print('\nEnd of Row ' + str(i + 1) + '\n')


#Main Program
inSudo()
print('The problem is :\n')
printSudo()
solve()
