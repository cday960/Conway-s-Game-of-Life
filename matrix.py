import random
#from termcolor import colored

# Matrix class, contains a randomized matrix of 0s and 1s, width, and height.
class Matrix():
    def __init__(self, width: int, height: int) -> None:
        self.m = [[0 for _ in range(width)] for _ in range(height)]
        self.width = len(self.m[0])
        self.height = len(self.m)
        randomMatrix(self.m)


# Prints the matrix
def printMatrix(matrix: int, r=None, c=None) -> None:
    for i, row in enumerate(matrix.m):
        for j, col in enumerate(row):
            # if (i, j) == (r, c):
            #     print(colored(col, 'green', attrs=['bold', 'underline']), end=" ")
            # else:
            #     print(col, end=" ")
            print(col, end=" ")
        print()

    
# Randomizes the matrix
def randomMatrix(matrix: Matrix) -> None:
    pool = [0 for _ in range(5)]
    pool.append(1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = pool[random.randint(0, len(pool)-1)]


# Prints the neighbors of a given coordinate in a matrix
def printNeighbors(m: Matrix, row: int, col: int) -> None:
    for i in range(row-1, row+2):
        print([m.m[i][x] for x in range(col-1, col+2) if i<m.height and x<m.width])


# Counts the neighbors of a given coordinate in a matrix
def countNeighbors(mat: Matrix, row: int, col: int) -> int:
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i<0 or i>mat.width-1 or j<0 or j>mat.height-1 or (i==row and j==col):
                continue
            elif mat.m[i][j] == 1:
                count += 1
    return(count)


# Returns a new matrix with the next generation of cells
def nextGeneration(matrix: Matrix) -> Matrix:
    newMatrix = []
    for row in range(matrix.width):
        newMatrix.append([])
        for col in range(matrix.height):
            count = countNeighbors(matrix, row, col)
            if matrix.m[row][col] == 1:
                if count < 2 or count > 3:
                    newMatrix[row].append(0)
                elif count >=2 and count <= 3:
                    newMatrix[row].append(1)
            else:
                if count == 3:
                    newMatrix[row].append(1)
                elif count != 3:
                    newMatrix[row].append(0)
    return(newMatrix)
  
#region      
# if __name__ == "__main__":
#     life = Matrix(width=8, height=8)
#     #region debugging
#     # target = (4, 8)
#     # print(colored("Life:", color='magenta', attrs=['bold', 'underline']))
#     # printMatrix(life, target[0], target[1])
    
#     # print(colored("Number of neighors:", color="magenta", attrs=['bold', 'underline']), end=" ")
#     # print(countNeighbors(life, target[0], target[1]))
    
#     # print(colored("Neighbors:", color='magenta', attrs=['bold', 'underline']))
#     # printNeighbors(life, target[0], target[1])
#     #endregion
#     printMatrix(life)
    
#     print(f"\nnext gen test:\n")
#     life.m = nextGeneration(life)
#     printMatrix(life)
#endregion