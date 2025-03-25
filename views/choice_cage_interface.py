from config import *
import pygame

class ChoiceInterface:
    def __init__(self):
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
        self.title_text = self.font_title.render("CHOOSE A CAGE (1-5)", True, COLORS_FONT)  
        self.title_pos = self.title_text.get_rect(center=(WINDOW_WIDTH // 2, 125))

        # Input box properties
        self.input_box = pygame.Rect(200, 350, 400, 50)
        self.color_inactive = COLORS_BUTTON_INACTIVE
        self.color_active = COLORS_BUTTON_ACTIVE
        self.color = self.color_inactive
        self.active = False
        self.text = ''

        # Back button
        self.button_back_rect = pygame.Rect(250, 500, 200, 60)  # Define position & size

        self.inter = None  # Initialize but don't create a new instance yet

    def display(self, previous_interface):
        self.inter = previous_interface  # Store the previous interface

        while True:
            self.root.fill(COLORS_BACKGROUND)  # Clear the screen on each frame

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Toggle input box activation on click
                    if self.input_box.collidepoint(event.pos):
                        self.active = not self.active
                    else:
                        self.active = False
                    self.color = self.color_active if self.active else self.color_inactive
                    
                    # Check if back button is clicked
                    if self.button_back_rect.collidepoint(event.pos):
                        self.inter.display()  # Go back to the previous interface
                        return  # Exit the loop

                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            return self.text  # Return input when Enter is pressed
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        elif event.unicode.isdigit():  # Allow only digit input
                            self.text += event.unicode

            # Render title text
            self.root.blit(self.title_text, self.title_pos)

            # Render input text
            txt_surface = self.font.render(self.text, True, COLORS_FONT)
            width = max(300, txt_surface.get_width() + 10)
            self.input_box.w = width  # Adjust input box width dynamically

            # Draw input box and text
            pygame.draw.rect(self.root, self.color, self.input_box, 2)
            self.root.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 10))

            mouse_pos = pygame.mouse.get_pos()

            # **Back button hover effect** (change size and color when hovered)
            is_hovered_back = self.button_back_rect.collidepoint(mouse_pos)
            back_rect = self.button_back_rect.inflate(15, 15) if is_hovered_back else self.button_back_rect
            button_color = COLORS_BUTTON_ACTIVE if is_hovered_back else COLORS_BUTTON_INACTIVE
            pygame.draw.rect(self.root, button_color, back_rect, border_radius=15)
            button_back_text = self.font.render("BACK", True, (255, 255, 255))
            self.root.blit(button_back_text, button_back_text.get_rect(center=back_rect.center))

            pygame.display.flip()
