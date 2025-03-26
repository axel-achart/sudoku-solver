import pygame
from views.interface import Interface
from script.script import SudokuGrid
from algo.backtracking import Backtracking
from views.solver_interface import SolverInterface
from views.choice_cage_interface import ChoiceInterface

def main():
    pygame.init()
    
    # Launch Interface Home
    inter = Interface()
    inter.display()

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
    solver = Backtracking(sudoku.grid, interface)
    
    if solver.solve():
        print("Sudoku solved!")
        sudoku.display_grid()
    else:
        print("No solution found.")
    
    pygame.quit()


if __name__ == '__main__':
    main()