# raw solver method

import time
import itertools

class Sudoku:
    def __init__(self, grid, interface=None):
        self.grid = grid
        self.interface = interface
        self.start_time = None

    def solve(self):
        """Brute-force Sudoku solver that tries all possible values."""
        self.start_time = time.time()
        empty_cells = [(r, c) for r in range(9) for c in range(9) if self.grid[r][c] == 0]
        
        for values in itertools.product(range(1, 10), repeat=len(empty_cells)):
            for (r, c), v in zip(empty_cells, values):
                self.grid[r][c] = v
                if self.interface:
                    self.interface.update_grid()
            
            if self.is_solved():
                return True
            
            # Affichage du message après 10 secondes
            if time.time() - self.start_time > 10:
                print("Brute-force en cours... Revenez dans quelques siècles. 😂")
                return False
        
        return False

    def is_solved(self):
        """Check if the Sudoku is completely filled and valid."""
        for row in self.grid:
            if len(set(row)) != 9:
                return False
        for col in zip(*self.grid):
            if len(set(col)) != 9:
                return False
        for box_x in range(0, 9, 3):
            for box_y in range(0, 9, 3):
                box = [self.grid[r][c] for r in range(box_x, box_x+3) for c in range(box_y, box_y+3)]
                if len(set(box)) != 9:
                    return False
        return True