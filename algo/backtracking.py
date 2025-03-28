class Backtracking:

    def __init__(self, grid, interface=None):
        self.grid = grid
        self.interface = interface

    def solve(self, position=0):

        if position == 81:
            return True
        row, col = divmod(position, 9)
        if self.grid[row][col] != 0:
            return self.solve(position + 1)
        for value in range(1, 10):
            if self.is_valid(value, row, col):
                self.grid[row][col] = value
                if self.interface:
                    self.interface.update_grid()
                if self.solve(position + 1):
                    return True
                self.grid[row][col] = 0
                if self.interface:
                    self.interface.update_grid()
        return False

    def is_valid(self, value, row, col):

        return (self.is_valid_in_row(value, row) and
                self.is_valid_in_column(value, col) and
                self.is_valid_in_box(value, row, col))

    def is_valid_in_row(self, value, row):
        return value not in self.grid[row]

    def is_valid_in_column(self, value, col):
        return value not in [self.grid[row][col] for row in range(9)]

    def is_valid_in_box(self, value, row, col):
        box_x, box_y = (row // 3) * 3, (col // 3) * 3
        return value not in [self.grid[i][j] for i in range(box_x, box_x + 3) for j in range(box_y, box_y + 3)]