from config import *
import pygame
from pygame.locals import *
from views.choice_cage_interface import ChoiceInterface

pygame.init()

class Interface:
    def __init__(self):
        self.root = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sudoku Solver - Developed by Perla, Alexandre, Axel")

        self.background = pygame.Surface(self.root.get_size())
        self.background.fill(COLORS_BACKGROUND)

        self.root.blit(self.background, (0, 0))
        pygame.display.flip()

        self.font_title = pygame.font.Font(None, 70)
        self.font = pygame.font.Font(None, 34)

        self.text = self.font_title.render("SUDOKU SOLVER", True, COLORS_FONT)  
        self.textpos = self.text.get_rect(center=(WINDOW_WIDTH // 2, 125))
        self.root.blit(self.text, self.textpos)

        self.button_color = COLORS_BUTTON_INACTIVE
        self.hover_color = COLORS_BUTTON_ACTIVE

        self.button_brute_rect = pygame.Rect(150, 250, 400, 80)
        self.button_backtracking_rect = pygame.Rect(150, 450, 400, 80)

        self.choice_interface = ChoiceInterface()

    def display(self):
        while True:
            self.root.fill(COLORS_BACKGROUND) 
            self.root.blit(self.text, self.textpos) 

            mouse_pos = pygame.mouse.get_pos()
            is_hovered_brute = self.button_brute_rect.collidepoint(mouse_pos)
            is_hovered_backtracking = self.button_backtracking_rect.collidepoint(mouse_pos)

            brute_rect = self.button_brute_rect.inflate(10, 10) if is_hovered_brute else self.button_brute_rect
            pygame.draw.rect(self.root, self.hover_color if is_hovered_brute else self.button_color, brute_rect, border_radius=15)
            button_brute_text = self.font.render("Use BruteForce Method", True, (255, 255, 255))
            self.root.blit(button_brute_text, button_brute_text.get_rect(center=brute_rect.center))

            backtracking_rect = self.button_backtracking_rect.inflate(10, 10) if is_hovered_backtracking else self.button_backtracking_rect
            pygame.draw.rect(self.root, self.hover_color if is_hovered_backtracking else self.button_color, backtracking_rect, border_radius=15)
            button_backtracking_text = self.font.render("Use BackTracking Method", True, (255, 255, 255))
            self.root.blit(button_backtracking_text, button_backtracking_text.get_rect(center=backtracking_rect.center))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if is_hovered_backtracking:
                        selected_file = self.choice_interface.get_selected_file()
                        if selected_file:
                            print(f"File selected : {selected_file}")
                            return selected_file 
                    elif is_hovered_brute:
                        pass

            pygame.display.flip()
