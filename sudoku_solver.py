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

import sys

sudoku = [[0 for _ in range(9)] for _ in range(9)]


# Print the Sudoku
def print_sudo():
    """
    Function to Print Sudoku
    """
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


# Check the possibilty of num to be placed at [row][col] position
def check_place(row, col, num):
    """
    Function to check validtion of a number in a cell
    """
    for i in range(9):
        if sudoku[row][i] == num:
            return False
    for i in range(9):
        if sudoku[i][col] == num:
            return False
    grid_c = (col//3)*3
    grid_r = (row//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[grid_r+i][grid_c+j] == num:
                return False
    return True


# Solve the Sudoku
def solve():
    """
    Function to solve the Sudoku
    """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for num in range(1, 10):
                    if check_place(i, j, num):
                        sudoku[i][j] = num
                        solve()
                        sudoku[i][j] = 0
                return
    print("\nThe solution is :\n")
    print_sudo()
    sys.exit()


# Input the Problem
def in_sudo():
    """
    Function to input the Sudoku problem
    """
    print("Enter the Sudoku Grid (Row Wise)(0 for blank cell)\n")
    for i in range(9):
        for j in range(9):
            element = int(
                input(f"Element for row {i + 1} and column {j + 1} : \t"))
            sudoku[i][j] = element if 0 <= element < 10 else 0
        print('\nEnd of Row ' + str(i + 1) + '\n')


# Main Program
in_sudo()
print('The problem is :\n')
print_sudo()
solve()
