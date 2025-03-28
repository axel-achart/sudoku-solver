# Main File to launch program
import pygame
from views.interface import Interface
from script.script import SudokuGrid
from algo.backtracking import Backtracking
from algo.bruteforce import Sudoku
from views.solver_interface import SolverInterface
from views.choice_cage_interface import ChoiceInterface

from algo.bruteforce import Sudoku

def main():
    pygame.init()
    
    # Launch Interface Home
    inter = Interface()
    method = inter.display()

    # Launch Interface to choose a cage
    choice_interface = ChoiceInterface()
    file_path = choice_interface.get_selected_file() 
    
    if not file_path:
        print("Any files selected")
        return

    # Launch Grid for Sudoku
    sudoku = SudokuGrid(file_path)
    sudoku.display_grid()

    # Launch Interface of the solver
    interface = SolverInterface(sudoku.grid)

    if method == "bruteforce":
        solver = Sudoku(sudoku.grid, interface)     # BruteForce
    else:
        solver = Backtracking(sudoku.grid, interface)       # BackTracking
    
    # Results
    if solver.solve():
        print("Sudoku solved!")
        sudoku.display_grid()
    else:
        print("No solution found.")
    
    pygame.quit()


# Launch by myself only
if __name__ == '__main__':
    main()