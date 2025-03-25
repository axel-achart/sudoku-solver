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

### True si valeur non trouve
### False si valeur trouvée

class Backtracking():
    def __init__(self, grid):
        self.grid = grid

    def line_value(self, value,line):
        for i in range(0,9):
            if self.grid[line][i] == value:
                return False
        return True
                
    def column_value(self, value, column):
        for i in range(0,9):
            if self.grid[i][column] == value:
                return False
        return True
    
    def box_grid_value(self, value, line, column):
        _line = line - (line%3)
        _column = column - (column%3)

        for i in range(_line, _column):
            for j in range(_line, _column): 
                if self.grid[i][j] == value:
                    return False
        return True
        
    
            


grid = Backtracking(grids)

tab1 = grid.line_value(1, 0)
tab2 = grid.column_value(1, 0)
tab3 = grid.box_grid_value(1,2,3)
print(tab3)


##grid.column_value(2)