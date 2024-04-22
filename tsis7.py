import pygame
pygame.init()

#Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Line")
clock = pygame.time.Clock()

# Starting position of the line
start_pos = (0, 0)

# Variable to track whether to draw the line
drawing = False

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
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                drawing = False

    # Update the line endpoint to follow the mouse pointer
    end_pos = pygame.mouse.get_pos()

    # Draw the line if drawing is enabled
    if drawing:
        pygame.draw.line(screen, BLACK, start_pos, end_pos, 2)

    pygame.display.flip()
    clock.tick(60)



