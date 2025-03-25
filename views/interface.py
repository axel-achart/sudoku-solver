from config import *
import pygame
from pygame.locals import *
from views.choice_cage_interface import ChoiceInterface

# Initialize pygame once at the beginning
pygame.init()

class Interface:
    def __init__(self):
        # Initialize the window
        self.root = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sudoku Solver - Developed by Perla, Alexandre, Axel")

        # Background setup
        self.background = pygame.Surface(self.root.get_size())
        self.background = self.background.convert()
        self.background.fill(COLORS_BACKGROUND)

        # Initial screen blit
        self.root.blit(self.background, (0, 0))
        pygame.display.flip()

        # Fonts
        self.font_title = pygame.font.Font(None, 70)
        self.font = pygame.font.Font(None, 34)

        # Title
        self.text = self.font_title.render("SUDOKU SOLVER", True, COLORS_FONT)  
        self.textpos = self.text.get_rect(center=(self.background.get_rect().centerx, 125))
        self.background.blit(self.text, self.textpos)

        # Button colors
        self.button_color = COLORS_BUTTON_INACTIVE
        self.hover_color = COLORS_BUTTON_ACTIVE

        # Buttons positions and sizes
        self.button_brute_rect = pygame.Rect(150, 250, 400, 80)
        self.button_backtracking_rect = pygame.Rect(150, 450, 400, 80)

    def display(self):
        loop = True
        # Go next interface
        self.choice_interface = ChoiceInterface()
        while loop:
            mouse_pos = pygame.mouse.get_pos()
            
            # Check if the mouse is hovering over a button
            is_hovered_brute = self.button_brute_rect.collidepoint(mouse_pos)
            is_hovered_backtracking = self.button_backtracking_rect.collidepoint(mouse_pos)

            # Refresh the screen
            self.root.blit(self.background, (0, 0))

            # Draw the BruteForce button
            brute_rect = self.button_brute_rect.inflate(10, 10) if is_hovered_brute else self.button_brute_rect
            pygame.draw.rect(self.root, self.hover_color if is_hovered_brute else self.button_color, brute_rect, border_radius=15)
            button_brute_text = self.font.render("Use BruteForce Method", True, (255, 255, 255))
            self.root.blit(button_brute_text, button_brute_text.get_rect(center=brute_rect.center))

            # Draw the BackTracking button
            backtracking_rect = self.button_backtracking_rect.inflate(10, 10) if is_hovered_backtracking else self.button_backtracking_rect
            pygame.draw.rect(self.root, self.hover_color if is_hovered_backtracking else self.button_color, backtracking_rect, border_radius=15)
            button_backtracking_text = self.font.render("Use BackTracking Method", True, (255, 255, 255))
            self.root.blit(button_backtracking_text, button_backtracking_text.get_rect(center=backtracking_rect.center))

            # Handle events
            for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False
                elif event.type == MOUSEBUTTONDOWN:
                    if is_hovered_brute:
                        print("BruteForce method selected!")
                        self.choice_interface.display(self)  # Pass current interface to go back
                    elif is_hovered_backtracking:
                        print("BackTracking method selected!")
                        self.choice_interface.display(self)  # Pass current interface to go back

            # Update display once after all drawing
            pygame.display.flip()
