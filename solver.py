#program  that solves a sudoku puzzle for you
#bmp: solves a a precoded sudoku puzzle thats stored as a 2D list, prints everything out into terminal
#bike ver: adds a graphical component 
#car ver: can take a user inputted sudoku puzzle

#made by George Aoyagi
#solver goes to evey empty spot, and gives you a valid number
#if no vlaid number can't be found then it rewinds to the previous guest spot and tries to find another valid number for that spot
#the process continues and rewinds until puzzle is solved   


#sample sudoku puzzle as 2d list
sudoku = [[0,0,0,2,6,0,7,0,1], [6,8,0,0,7,0,0,9,0], [1,9,0,0,0,4,5,0,0],
          [8,2,0,1,0,0,0,4,0], [0,0,4,6,0,2,9,0,0], [0,5,0,0,0,3,0,2,8],
          [0,0,9,3,0,0,0,7,4], [0,4,0,0,5,0,0,3,6], [7,0,3,0,1,8,0,0,0]]
#answer to the sudoku for testing purposes
answer = [[4,3,5,2,6,9,7,8,1], [6,8,2,5,7,1,4,9,3], [1,9,7,8,3,4,5,6,2],
          [8,2,6,1,9,5,3,4,7], [3,7,4,6,8,2,9,1,5], [9,5,1,7,4,3,6,2,8],
          [5,1,9,3,2,6,8,7,4], [2,4,8,9,5,7,1,3,6], [7,6,3,4,1,8,2,5,9]]
#https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html

guesses = []

#text display for the sudoku puzzle
def display():
    for x in range(9):
        if x+1%3==0:
            for z in range(19):
                print("_")
        for y in range(9):
            print(sudoku[x][y] + " ")
            if y+1%3 == 0:
                print ("| ")

#check if a guess is valid in the current row
#param: int(current col)
#return: bool(True if valid)
def checkRow(columnNum, value):
    #loops through the entire column
    for x in range(9):
        if sudoku[columnNum][x] == value:
            return False
    return True

#check if the guess is valid in the curret column
#param: int(current row)
#return: bool(True if valid)
def checkCol(rowNum, value):
    #loops through entire row
    for x in range(9):
        if sudoku[x][rowNum] == value:
            return False
    return True
    

#check if the guess is valid in the current square by checking every value in the square except the specified coordinates
#param: int(current row), int(current col), int(guess)
#return: bool(True if valid)
def checkSquare(rowNum, colNum, value):
    #the while's should set the coordinates the square's bottom right coordinate
    tempRow = rowNum
    tempCol = colNum
    while tempRow+1%3 != 0:
        tempRow+=1
    while tempCol+1%3 != 0:
        tempCol+=1
    #loops through the entire square
    for a in range(tempRow, tempRow-2):
        for b in range(tempCol, tempCol-2):
            #dont check the the square that your trying to check for
            if a!=rowNum and b!=colNum:
                if sudoku[a][b] == value:
                    return False
    return True
    
    

#calls all the guess validity checks at once
#param: int(current row), int(current col), int(guess)
#return: bool (True if valid)
def check(rowNum, colNum, value):
    if checkRow(rowNum, value) and checkCol(colNum, value) and checkSquare(rowNum, colValue):
        return True
    else:
        return False

#finds a valid guess for an empty spot, if no valid spot can be found, back track to the last previous guessed num validate that one
#param: int(current row), int(current col), int(guess), list(list of currently guessed numbers)
#return: bool(succes of valid  spot)
def validate(row, col, guess):
    


#main function, when called it should solve the puzzle
#param: none
#arg: none
def solve():
   


