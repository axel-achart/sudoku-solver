from config import *
import pygame
from algo.backtracking import Backtracking

class SolverInterface:
    def __init__(self, grid):
        self.grid = grid
        # Create a "given" matrix to track which numbers were initially provided
        self.given = [[True if num != 0 else False for num in row] for row in grid]

        # Initialize the window
        self.root = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sudoku Solver - Developed by Perla, Alexandre, Axel")

        # Load fonts
        self.font_title = pygame.font.Font(None, 70)
        self.font = pygame.font.Font(None, 34)

        # Set background color
        self.background = pygame.Surface(self.root.get_size())
        self.background.fill(COLORS_BACKGROUND)

        # Title text
        self.title_text = self.font_title.render("SOLVING...", True, COLORS_FONT)  
        self.title_pos = self.title_text.get_rect(center=(WINDOW_WIDTH // 2, 45))

        # Back button
        self.button_back_rect = pygame.Rect(10, 25, 180, 50) 
        self.inter = None


    def draw_grid(self):
        max_grid_size = 600
        cell_size = max_grid_size // 9 

        # Center grid
        grid_x = (WINDOW_WIDTH - max_grid_size) // 2
        grid_y = 85

        # Lines
        for i in range(10):
            thickness = 4 if i % 3 == 0 else 1  # Bold lines
            pygame.draw.line(self.root, COLORS_FONT, (grid_x + i * cell_size, grid_y), (grid_x + i * cell_size, grid_y + 9 * cell_size), thickness)
            pygame.draw.line(self.root, COLORS_FONT, (grid_x, grid_y + i * cell_size), (grid_x + 9 * cell_size, grid_y + i * cell_size), thickness)

        # Show numbers
        font_size = int(cell_size * 0.7)
        font = pygame.font.Font(None, font_size)

        for row in range(9):
            for col in range(9):
                num = self.grid[row][col]
                if num != 0:  # If the cell has a number
                    if self.given[row][col]:  # If the number is given
                        text_surface = font.render(str(num), True, COLORS_NEUTRAL)  # Black for given numbers
                    else:
                        text_surface = font.render(str(num), True, COLORS_FONT)  # Blue for tested numbers

                    text_rect = text_surface.get_rect(center=(grid_x + col * cell_size + cell_size // 2, grid_y + row * cell_size + cell_size // 2))
                    self.root.blit(text_surface, text_rect)


    def update_grid(self):
        self.root.fill(COLORS_BACKGROUND)
        self.root.blit(self.title_text, self.title_pos)
        self.draw_grid()
        pygame.display.update()
        """pygame.time.delay(50)"""

    def display(self, previous_interface):
        self.inter = previous_interface
        while True:
            self.root.fill(COLORS_BACKGROUND)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if back button is clicked
                    if self.button_back_rect.collidepoint(event.pos):
                        self.inter.display(self)  # Go back to the previous interface
                        return 


            # Render title text
            self.root.blit(self.title_text, self.title_pos)

            self.draw_grid()


            mouse_pos = pygame.mouse.get_pos()

            # **Back button hover effect** (change size and color when hovered)
            is_hovered_back = self.button_back_rect.collidepoint(mouse_pos)
            back_rect = self.button_back_rect.inflate(15, 15) if is_hovered_back else self.button_back_rect
            button_color = COLORS_BUTTON_ACTIVE if is_hovered_back else COLORS_BUTTON_INACTIVE
            pygame.draw.rect(self.root, button_color, back_rect, border_radius=15)
            button_back_text = self.font.render("BACK", True, COLORS_TEXT)
            self.root.blit(button_back_text, button_back_text.get_rect(center=back_rect.center))

            pygame.display.flip()