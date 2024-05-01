import pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing App")
clock = pygame.time.Clock()

# Starting position of the line
start_pos = (0, 0)
prev_pos = (0, 0)

# Variable to track whether to draw the line
drawing = False
drawing_curve = False
curve_points = []

# Variable to track the drawn lines
drawn_lines = []

# Default line color
line_color = BLACK

# Main loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check for mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                start_pos = pygame.mouse.get_pos()
                drawing = True
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    drawing_curve = True
                    curve_points = [start_pos]
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False
                if drawing_curve:
                    curve_points.append(pygame.mouse.get_pos())
                    drawn_lines.append((line_color, curve_points))
                    drawing_curve = False
                else:
                    end_pos = pygame.mouse.get_pos()
                    drawn_lines.append((line_color, [start_pos, end_pos]))
        elif event.type == pygame.MOUSEMOTION and drawing_curve:
            if pygame.mouse.get_pressed()[0]:
                curve_points.append(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                if drawn_lines:
                    drawn_lines.pop()  # Undo the last drawn line segment

            # Color picker
            if event.key == pygame.K_c:
                line_color = pygame.color.Color(pygame.mouse.get_pos())
                
    # Draw the lines
    for color, points in drawn_lines:
        if len(points) > 1:
            pygame.draw.lines(screen, color, False, points, 2)
        else:
            pygame.draw.circle(screen, color, points[0], 2)

    # Draw the current line if drawing
    if drawing:
        if drawing_curve:
            pygame.draw.lines(screen, line_color, False, curve_points, 2)
        else:
            end_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, line_color, start_pos, end_pos, 2)

    pygame.display.flip()
    clock.tick(60)
