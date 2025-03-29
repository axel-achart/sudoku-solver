# Sudoku Solver 🔍

## Overview

This project is a Sudoku solver implemented in Python. It provides two solving methods:

- **Brute Force**: Tries all possible number combinations until a valid solution is found.
- **Backtracking**: A recursive approach that fills the grid step by step, backtracking when needed.

The solver reads Sudoku puzzles from input files and displays the solution in the terminal and with a graphical interface using Pygame.

The brute force method is inefficient and takes too much time, which can be measured in years.
As for the backtracking method, it's much faster, capable of solving in a few seconds.
Approximately 1 second for level 1, and 11 seconds for level 5.

## Algorithms and Tools Used

### Backtracking Algorithm

1. **Selection of an Empty Cell**: The algorithm selects an empty cell in the grid.
2. **Trial of Values**: It attempts to place a digit (from 1 to 9) in the selected cell.
3. **Validation**: After placing a digit, the algorithm checks if this placement maintains the validity of the grid (i.e., no duplicate digits in the current row, column, or subgrid).
4. **Recursion**: If the placement is valid, the algorithm moves to the next empty cell and repeats the process.
5. **Backtracking**: If placing any digit in the current cell leads to an invalid state or no solution further down the path, the algorithm backtracks by removing the last placed digit and trying the next possible value.

This method continues until the grid is completely and correctly filled or until all possibilities have been exhausted, indicating that the puzzle is unsolvable.

### Tools and Programming Language

The project is implemented in **Python**, a versatile and widely-used programming language known for its readability and extensive library support. Python's standard libraries and data structures facilitate the implementation of complex algorithms like backtracking and constraint propagation.

## Observations

- **Efficiency on Easier Puzzles**: The solver performs exceptionally well on easy to medium puzzles, providing solutions almost instantaneously.
- **Increased Time for Harder Puzzles**: As the difficulty increases (more empty cells and complex constraints), the execution time rises significantly due to the exponential nature of the backtracking algorithm.
- **Constraint Propagation Benefits**: Incorporating constraint propagation techniques notably reduces the number of possibilities the algorithm needs to explore, thereby enhancing performance, especially on medium-difficulty puzzles.

## Conclusion

The implemented Sudoku solver effectively utilizes the backtracking algorithm complemented by constraint propagation techniques to solve puzzles across various difficulty levels. While the solver demonstrates high efficiency on simpler puzzles, its performance declines on more complex puzzles due to the inherent limitations of the backtracking approach.

## References

- [Backtracking](https://www.geeksforgeeks.org/backtracking-algorithm-in-python/)
- [Brute force](https://www.mathinfo.ovh/Premiere_NSI/G05_Algo_Glouton/index.html)
- [Backtracking](https://www.easiio.com/fr/backtracking-algorithm/)
- [Algo X of Knuth](https://fr.wikipedia.org/wiki/Algorithmes_de_r%C3%A9solution_des_sudokus)
