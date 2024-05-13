import pygame
import sys
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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

# Variables for moving the last drawn figure
last_figure = (400, 300)
move_speed = 5


while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                current_line = [pygame.mouse.get_pos()]  # Start a new line
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
                if current_line:  # Append the line to drawn_lines if it's not empty
                    drawn_lines.append((line_color, current_line))
                    # If there are more than 2 points in the current_line, connect the start and end points with a regular line
                    if len(current_line) >= 2:
                        drawn_lines.append((line_color, [current_line[0], current_line[-1]]))
                    current_line = []  # Reset current_line
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                current_line.append(pygame.mouse.get_pos())  # Add current mouse position to current_line
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Change line color to RED when "C" is pressed
                line_color = RED
            elif event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:  # Undo last drawn line with "Ctrl + Z"
                if drawn_lines:
                    drawn_lines.pop()  # Remove the last drawn line
            elif event.key == pygame.K_UP and last_figure:  
                last_figure = (last_figure[0], last_figure[1] - move_speed)
            elif event.key == pygame.K_DOWN and last_figure:  
                last_figure = (last_figure[0], last_figure[1] + move_speed)
            elif event.key == pygame.K_LEFT and last_figure:  
                last_figure = (last_figure[0] - move_speed, last_figure[1])
            elif event.key == pygame.K_RIGHT and last_figure:  
                last_figure = (last_figure[0] + move_speed, last_figure[1])

    # Draw all lines
    for color, points in drawn_lines:
        pygame.draw.lines(screen, color, False, points, 2)

    # Draw a rectangle around each figure
    for color, points in drawn_lines:
        if len(points) >= 2:
            rect = pygame.Rect(points[0], (0, 0)).unionall([pygame.Rect(point, (0, 0)) for point in points])
            pygame.draw.rect(screen, BLACK, rect, 1)

    pygame.display.flip()
    clock.tick(60)