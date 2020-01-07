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

#Number Node class, each node holds the value of a guess at a set of coordinates
class Node: 
    def __init__(self, row, col, value):    
        #values
        self.value = value
        self.row = row
        self.col = col
        self.next = None 
        self.prev = None  
   
#Doubley Linked List class 
class LinkedList: 
    def __init__(self):  
        self.head = None
        self.tail = None
        self.size = 0

#text display for the sudoku puzzle
def display():
    for x in range(9):
        if x%3==0:
            for z in range(23):
                print("_", end='')
            print('')
        for y in range(9):
            if y%3 == 0:
                print ("| ", end='')
            print(str(sudoku[x][y]) + " ", end='')
        print('')
    for z in range(23):
        print("_", end='')

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
    if checkRow(rowNum, value) and checkCol(colNum, value) and checkSquare(rowNum, colNum, value):
        return True
    else:
        return False

# #solves the puzzle by finds a valid guess for an empty spot, if no valid spot can be found, back track to the last previous guessed num validate that one
# #param: node(object for the currently guessed spot), linkedList(list of currently guessed numbers)
# #return: bool(succes of valid  spot)
# def solve(guess, guessed):
#     valid = False
#     for num in range(1,9):
#         if temp not in empty:
#             valid = check(temp)
#     if not valid:
#         guessed-=1
#         validate(empty[guessed].row, empty[guessed].col)
   

if __name__ == "__main__":
    toGuess = LinkedList()
    #sentinal node
    toGuess.head = Node (-1,-1,-1)
    toGuess.tail = toGuess.head
    #iterate through the puzzle to find all the spots to guess and adds them to the linked list
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                toGuess.tail.next = Node(row, col, 0)
                temp = toGuess.tail
                toGuess.tail = toGuess.tail.next
                toGuess.prev = temp
    # #test to see if I get all the spots  to guess correctly
    # temp = toGuess.head.next
    # while temp != None:
    #     print("row: "+ str(temp.row))
    #     print("col: "+ str(temp.col))
    #     print("")
    #     temp = temp.next


    print("""rules of Sudoku: Your goal is to fill the grid with numbers. Each spot must be a  number within 1-9.
             A guess is valid if all 3 of the following things are satisfied: 
                1) there is no identical number within the sub square 
                2) there is no identical number in the same row 
                3) there is now identical number in the same column""")
    display()
    print('')
    solved = False
    while not solved:
        # answer = input("Do you give up and want it solved for you? (press y for yes, anything else for no): ")
        # if answer == 'y':
        #     solve()
        #     solved = True
        #checks if the user's guess is valid
        valid = False
        while not valid:
            row = input("Enter a guess (in order of row, then column, then value): ")
            if int(row)>9 or int(row)<1:
                print("Invalid Row Number")
                continue
            col = input()
            if int(col)>9 or int(col)<1:
                print("Invalid Column number")
                continue
            value = input()
            if int(value)>9 or int(value)<1:
                print("invalid Value")
        
            valid = True
        

        if sudoku == answer:
            solved = True


