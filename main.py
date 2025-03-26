import pygame
from views.interface import Interface
from script.script import SudokuGrid
from algo.backtracking import Backtracking
from views.solver_interface import SolverInterface
from views.choice_cage_interface import ChoiceInterface

def main():
    pygame.init()
    
    inter = Interface()
    inter.display()
    choice_interface = ChoiceInterface()
    file_path = choice_interface.get_selected_file() 
    
    if not file_path:
        print("Any files selected")
        return

    sudoku = SudokuGrid(file_path)
    sudoku.display_grid()

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
