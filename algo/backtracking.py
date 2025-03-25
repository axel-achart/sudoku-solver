# solver backtracking method

grids = [
    [0,7,2,9,0,0,0,3,0],
    [0,0,1,0,0,6,0,8,0],
    [0,0,0,0,4,0,0,6,0],
    [9,6,0,0,0,4,1,0,8],
    [0,4,8,7,0,5,0,9,6],
    [0,0,5,6,0,8,0,0,3],
    [0,0,0,4,0,2,0,1,0],
    [8,5,0,0,6,0,3,2,7],
    [1,0,0,8,5,0,0,0,0]
]

### True if we didn't find the value
### False if i find value

class Backtracking():
    def __init__(self, grid):
        self.grid = grid

    def display_grid(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.grid[i][j] if self.grid[i][j] != 0 else ".", end=" ")
            print()
        print("\n")
   
## methods who verified if the number is in the line
    def line_value(self, value,line):
        for i in range(0,9):
            if self.grid[line][i] == value:
                return False
        return True

## methods who verified if the number is in the column           
    def column_value(self, value, column):
        for i in range(0,9):
            if self.grid[i][column] == value:
                return False
        return True
    
    def box_grid_value(self, value, line, column):

        _line = line - (line % 3)  
        _column = column - (column % 3)

        for i in range(_line, _line + 3):
            for j in range(_column, _column + 3): 
                if self.grid[i][j] == value:
                    return False
        return True
        
    def verification_grid(self, position=0):
        if position == 81:
            return True

        row, col = divmod(position, 9)

        if self.grid[row][col] != 0:
            return self.verification_grid(position + 1)

        for value in range(1, 10):
            print(self.display_grid())
            if (self.line_value(value, row) and
                self.column_value(value, col) and
                self.box_grid_value(value, row, col)):

                self.grid[row][col] = value
                if self.verification_grid(position + 1):
                    return True
                self.grid[row][col] = 0

        return False
            


grid = Backtracking(grids)

tab1 = grid.line_value(1, 0)
tab2 = grid.column_value(1, 0)
tab3 = grid.box_grid_value(1,2,3)
grid.display_grid()
if grid.verification_grid(0):
    print('the sudoku is solved')
    grid.display_grid()
else:
    print("No solution found.")




