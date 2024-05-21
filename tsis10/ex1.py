import pygame
import sys

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Line")
clock = pygame.time.Clock()

# List to store drawn lines
drawn_lines = []

# Variable to track whether to draw the line
drawing = False
current_line = []  # List to store points of the current line

line_color = BLACK  # Default line color

# Color palette
palette_colors = [RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE]
palette_rects = []
palette_width = 50
palette_height = 50
palette_padding = 10

# Calculate positions for the colors in a row
for i, color in enumerate(palette_colors):
    rect = pygame.Rect(10 + (palette_width + palette_padding) * i, 10, palette_width, palette_height)
    palette_rects.append(rect)

# Function to draw a heart shape
def draw_heart(center, size):
    """
    Function to draw a heart shape.

    Args:
        center (tuple): Coordinates of the center of the heart.
        size (int): Size of the heart.

    Returns:
        list: List of points describing the heart shape.
    """
    x, y = center
    points = [
        (x, y - size),
        (x + size // 6, y - size // 3),
        (x + size // 3, y - size // 6),
        (x + size // 2, y),
        (x + size // 3, y + size // 6),
        (x + size // 6, y + size // 3),
        (x, y + size // 2),
        (x - size // 6, y + size // 3),
        (x - size // 3, y + size // 6),
        (x - size // 2, y),
        (x - size // 3, y - size // 6),
        (x - size // 6, y - size // 3),
    ]
    return points

# Function to display settings window
def show_settings():
    font = pygame.font.Font(None, 36)
    size_text = font.render("Heart Size:", True, BLACK)
    size_rect = size_text.get_rect(center=(400, 200))

    input_rect = pygame.Rect(350, 250, 100, 40)
    size_value = 50
    input_text = font.render(str(size_value), True, BLACK)
    input_text_rect = input_text.get_rect(center=input_rect.center)

    running = True
    while running:
        screen.fill(WHITE)
        screen.blit(size_text, size_rect)
        pygame.draw.rect(screen, BLACK, input_rect, 2)
        screen.blit(input_text, input_text_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return int(input_text.get_text())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if input_rect.collidepoint(event.pos):
                        pygame.event.set_blocked(pygame.MOUSEMOTION)
                        active = True
                    else:
                        active = False
                else:
                    active = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pygame.event.set_allowed(pygame.MOUSEMOTION)
            if event.type == pygame.MOUSEMOTION:
                if active:
                    input_text = font.render(input_text.get_text() + event.unicode, True, BLACK)
                    input_text_rect = input_text.get_rect(center=input_rect.center)
                    if input_text_rect.width > input_rect.width - 10:
                        input_text = font.render(input_text.get_text()[:-1], True, BLACK)
                        input_text_rect = input_text.get_rect(center=input_rect.center)

# Main loop
while True:
    screen.fill(WHITE)

    # Draw color palette
    for i, color in enumerate(palette_colors):
        pygame.draw.rect(screen, color, palette_rects[i])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Check if mouse clicked on color palette
                for i, rect in enumerate(palette_rects):
                    if rect.collidepoint(event.pos):
                        line_color = palette_colors[i]
                        break
                else:
                    drawing = True
                    current_line = [pygame.mouse.get_pos()]  # Start a new line
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
                if current_line:  # Append the line to drawn_lines if it's not empty
                    if len(current_line) >= 2:
                        current_line.append(current_line[0])  # Connect the last point to the first point
                    drawn_lines.append((line_color, current_line))
                    current_line = []  # Reset current_line
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_line.append(pygame.mouse.get_pos())  # Add current mouse position to current_line
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:  # Undo last drawn line with "Ctrl + Z"
                if drawn_lines:
                    drawn_lines.pop()  # Remove the last drawn line
            elif event.key == pygame.K_h:  # Draw a heart shape when "H" key is pressed
                drawing = False
                size_value = show_settings()
                current_line = draw_heart(pygame.mouse.get_pos(), size_value)
                drawn_lines.append((line_color, current_line))

    # Draw all lines
    for color, points in drawn_lines:
        pygame.draw.lines(screen, color, False, points, 2)

    pygame.display.flip()
    clock.tick(60)
