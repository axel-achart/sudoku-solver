# solver backtracking method



### True if we didn't find the value
### False if i find value

class Backtracking():
    def __init__(self, grid):
        self.grid = grid


    def read_grid_from_file(file_path):
        """Lire la grille depuis un fichier texte."""
        try:
            with open(file_path, "r") as f:
                grid = []
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    if len(line) != 9 or not line.isdigit():
                        raise ValueError(f"line {line_num} : must contain 9 numbers.")
                    grid.append([int(ch) for ch in line])
                if len(grid) != 9:
                    raise ValueError("the txt file must contains 9 line.")
            return grid
        except FileNotFoundError as e:
            raise FileNotFoundError(f"file not found : {file_path}") from e
        except ValueError as e:
            raise ValueError(f"error in file {file_path}: {e}") from e

    def display_grid(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.grid[i][j] if self.grid[i][j] != 0 else "0", end=" ")
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
            
file_path = r"cages\fourth.txt"
grids = Backtracking.read_grid_from_file(file_path)
grid = Backtracking(grids)

if grid.verification_grid(0):
    print('the sudoku is solved')
    grid.display_grid()
else:
    print("No solution found.")




