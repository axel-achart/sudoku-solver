
import time
import itertools

class Sudoku:
    def __init__(self, grid, interface=None):
        self.grid = grid
        self.interface = interface
        self.start_time = None

    def solve(self):

        self.start_time = time.time()
        empty_cells = sorted([(r, c) for r in range(9) for c in range(9) if self.grid[r][c] == 0], key=lambda x: (x[0], x[1]))

        for values in itertools.product(range(1, 10), repeat=len(empty_cells)):
            for (r, c), v in zip(empty_cells, values):
                self.grid[r][c] = v
                if self.interface:
                    self.interface.update_grid()

            if self.is_solved():
                return True

            if time.time() - self.start_time > 10:
                print("More than 10 secondes...Brute force in progress... Come back in a few years. 😂")
                return False

        return False

    def is_solved(self):

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


"""import math
from datetime import datetime
import sys
import time

class Sudoku(object):
    def __init__(self):
        self.n = 0
        self.b = 0
        self.puzzle = []
        self.num_guesses = 0
        self.known_indices = []
        print("Initialisation du puzzle.")

    def load_puzzle(self, puzzle_string):
        print("Chargement du puzzle à partir d'une chaîne.")
        self.puzzle = []
        self.known_indices = []
        rows = [row for row in puzzle_string.split("\n") if row]
        self.n = len(rows)
        self.b = int(math.sqrt(self.n))
        print(f"Taille de la grille (n): {self.n}, taille de chaque bloc (b): {self.b}")
        
        for row_index, row in enumerate(rows):
            for col_index, c in enumerate(row):
                if c.isdigit():
                    self.puzzle.append(int(c))
                    if int(c) != 0:
                        self.known_indices.append((row_index * self.n) + col_index)
        print(f"Puzzle chargé: {self.puzzle}")

    def load_puzzle_from_file(self, path):
        try:
            print(f"Chargement du puzzle depuis le fichier {path}.")
            with open(path, 'r') as f:
                self.load_puzzle(f.read())
        except FileNotFoundError:
            print(f"Erreur : fichier '{path}' introuvable.")
            sys.exit(1)

    def to_string(self, pretty=True):
        result = ""
        for i, c in enumerate(self.puzzle):
            if pretty:
                if i % self.n == 0 and i != 0:
                    result += "\n"
                result += str(c) + " "
            else:
                result += str(c)
        return result

    def __repr__(self):
        return self.to_string(pretty=False)

    def __str__(self):
        return self.to_string()

    def solve(self):
        print("Début de la résolution du puzzle...")
        start_time = datetime.now()
        self.num_guesses = 0
        r = self.solve_from(0, 1)
        while r is not None:
            print(f"Recalcul à l'index {r[0]} avec le début du choix {r[1]}")
            r = self.solve_from(r[0], r[1])
        end_time = datetime.now()
        print(f"Temps total pour résoudre: {end_time - start_time}")
        return end_time - start_time

    def solve_from(self, index, starting_guess):
        print(f"Résolution à partir de l'index {index} avec le choix {starting_guess}")
        if index < 0 or index > len(self.puzzle):
            raise Exception(f"Index invalide du puzzle {index} après {self.num_guesses} suppositions")

        last_valid_guess_index = None
        found_valid_guess = False
        for i in range(index, len(self.puzzle)):
            if i not in self.known_indices:
                found_valid_guess = False
                for guess in range(starting_guess, self.n + 1):
                    print(f"Essai de placer {guess} à l'index {i}")
                    self.num_guesses += 1
                    if self.valid(i, guess):
                        found_valid_guess = True
                        last_valid_guess_index = i
                        self.puzzle[i] = guess
                        print(f"Placé {guess} à l'index {i}")
                        break
                starting_guess = 1
                if not found_valid_guess:
                    break

        if not found_valid_guess:
            new_index = last_valid_guess_index if last_valid_guess_index is not None else index - 1
            new_starting_guess = self.puzzle[new_index] + 1
            print(f"Aucun choix valide trouvé, réinitialisation de l'index {new_index} et essai de {new_starting_guess}")
            self.reset_puzzle_at(new_index)

            while new_starting_guess > self.n or new_index in self.known_indices:
                print(f"Nouvelle réinitialisation de l'index {new_index} avec {new_starting_guess}")
                new_index -= 1
                new_starting_guess = self.puzzle[new_index] + 1
                self.reset_puzzle_at(new_index)

            return (new_index, new_starting_guess)
        else:
            return None

    def reset_puzzle_at(self, index):
        print(f"Réinitialisation du puzzle à l'index {index}")
        for i in range(index, len(self.puzzle)):
            if i not in self.known_indices:
                self.puzzle[i] = 0

    def valid_for_row(self, index, guess):
        print(f"Vérification si {guess} est valide pour la ligne à l'index {index}")
        row_index = index // self.n
        start = self.n * row_index
        finish = start + self.n
        for c_index in range(start, finish):
            if c_index != index and self.puzzle[c_index] == guess:
                return False
        return True

    def valid_for_column(self, index, guess):
        print(f"Vérification si {guess} est valide pour la colonne à l'index {index}")
        col_index = index % self.n
        for r in range(0, self.n):
            r_index = col_index + (self.n * r)
            if r_index != index and self.puzzle[r_index] == guess:
                return False
        return True

    def valid_for_block(self, index, guess):
        print(f"Vérification si {guess} est valide pour le bloc à l'index {index}")
        row_index = index // self.n
        col_index = index % self.n
        block_row = row_index // self.b
        block_col = col_index // self.b
        row_start = block_row * self.b
        row_end = row_start + self.b - 1
        col_start = block_col * self.b
        col_end = col_start + self.b - 1
        for r in range(row_start, row_end + 1):
            for c in range(col_start, col_end + 1):
                i = c + (r * self.n)
                if self.puzzle[i] == guess:
                    return False
        return True

    def valid(self, index, guess):
        print(f"Vérification si {guess} est valide pour l'index {index}")
        return self.valid_for_row(index, guess) and self.valid_for_column(index, guess) and self.valid_for_block(index, guess)

if __name__ == "__main__":
    s = Sudoku()
    if len(sys.argv) < 2:
        print("Usage: python SudokuSolver.py <path_to_puzzle_file>")
        sys.exit(1)
    s.load_puzzle_from_file(sys.argv[1])

    print("\nPuzzle initial :\n%s" % (s))
    time = s.solve()
    print("\nSolution :\n%s" % (s))
    print("\nNombre de suppositions : %s" % (s.num_guesses))
    print("Temps total : %s" % (time))"""