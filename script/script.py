# A  script.py containing a SudokuGrid class whose methods allow you to:
# a. Import and parse a Sudoku grid,
# b. Display the grid elements,
# c. Solve using brute force and backtracking
# d. A file that retrieves a Sudoku example, calls one
# of the solving methods, and displays the solution in the terminal as well as in a Pygame window.

import pygame

class SudokuGrid:
    """Class to manage the Sudoku grid and solving process."""
    def __init__(self, file_path):
        self.grid = self.load_grid(file_path)
    
    def load_grid(self, file_path):
        """Load a Sudoku grid from a text file."""
        try:
            with open(file_path, "r") as f:
                grid = []
                for line in f:
                    line = line.strip()
                    if len(line) != 9 or not line.isdigit():
                        raise ValueError("Each line must contain exactly 9 digits.")
                    grid.append([int(ch) for ch in line])
                if len(grid) != 9:
                    raise ValueError("The file must contain exactly 9 lines.")
            return grid
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except ValueError as e:
            raise ValueError(f"Error in file {file_path}: {e}")

    def display_grid(self):
        """Display the Sudoku grid in the terminal."""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.grid[i][j] if self.grid[i][j] != 0 else ".", end=" ")
            print()
        print()