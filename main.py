import pygame
from views.interface import Interface
from script.script import SudokuGrid
from algo.backtracking import Backtracking
from algo.bruteforce import Sudoku
from views.solver_interface import SolverInterface
from views.choice_cage_interface import ChoiceInterface
import time

from algo.bruteforce import Sudoku

def main():
    pygame.init()
    
    inter = Interface()
    method = inter.display()

    choice_interface = ChoiceInterface()
    file_path = choice_interface.get_selected_file() 
    
    if not file_path:
        print("Any files selected")
        return

    sudoku = SudokuGrid(file_path)
    sudoku.display_grid()

    interface = SolverInterface(sudoku.grid)

    if method == "bruteforce":
        start_time = time.time()
        solver = Sudoku(sudoku.grid, interface)
    else:
        start_time = time.time()
        solver = Backtracking(sudoku.grid, interface) 
    
    if solver.solve():
        print("Sudoku solved!")
        sudoku.display_grid()
        print("Time to be solved: ", time.time() - start_time, "seconds")
    else:
        print("No solution found.")
        print("Time to process: ", time.time() - start_time, "seconds")
    
    pygame.quit()


if __name__ == '__main__':
    main()