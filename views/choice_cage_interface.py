import pygame
from pygame.locals import *
from config import *

class ChoiceInterface:
    def __init__(self):
        pygame.init()
        self.root = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sudoku Solver - Developed by Perla, Alexandre, Axel")

        self.font_title = pygame.font.Font(None, 70)
        self.font = pygame.font.Font(None, 36)
        self.selected_file = None

        self.files = [
            "cages/first.txt", "cages/second.txt", "cages/third.txt",
            "cages/fourth.txt", "cages/fifth.txt"
        ]
        self.buttons = [(file, pygame.Rect(150, 150 + i * 100, 400, 60)) for i, file in enumerate(self.files)]

    def display(self):
        while True:
            self.root.fill(COLORS_BACKGROUND)

            title_text = self.font.render("Choose a cage", True, COLORS_FONT)
            self.root.blit(title_text, (260, 80))

            mouse_pos = pygame.mouse.get_pos()

            for file, rect in self.buttons:
                is_hovered = rect.collidepoint(mouse_pos)
                color = COLORS_BUTTON_ACTIVE if is_hovered else COLORS_BUTTON_INACTIVE
                pygame.draw.rect(self.root, color, rect, border_radius=15)

                button_text = self.font.render(file.split("/")[-1], True, COLORS_TEXT)
                self.root.blit(button_text, button_text.get_rect(center=rect.center))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    for file, rect in self.buttons:
                        if rect.collidepoint(event.pos):
                            self.selected_file = file
                            return

            pygame.display.flip()

    def get_selected_file(self):
        if not self.selected_file:
            self.display()
        return self.selected_file
