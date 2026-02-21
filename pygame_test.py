# DRAW SHAPES USING PYGAME
# EXAMPLE 1

# import pygame
# import sys

# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("My First Pygame Window")

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((30, 144, 255))  # Sky blue background

#     # Draw a red rectangle
#     pygame.draw.rect(screen, (255, 0, 0), (50, 50, 150, 100))
#     # Draw a green circle
#     pygame.draw.circle(screen, (0, 255, 0), (320, 240), 60)
#     # Draw a yellow line
#     pygame.draw.line(screen, (255, 255, 0), (500, 100), (600, 400), 5)

#     pygame.display.flip()

# pygame.quit()
# sys.exit()
# #######################################################################################
# EXAMPLE 2
# import pygame

# pygame.init()
# clock = pygame.time.Clock()  # Create a clock object to manage the frame rate
# win_width = 500
# win_height = 400
# window = pygame.display.set_mode((win_width, win_height))
# while True:
#     for event in pygame.event.get():  # Handle events
#         if event.type == pygame.QUIT:  # Handle window close
#             pygame.quit()  # Close the Pygame window
#             raise SystemExit  # Exit the program
#     # Begin drawing statements
#     # Draw a red rectangle centered in the window
#     rect_width, rect_height = 100, 50
#     win_width, win_height = 500, 400
#     center_x = win_width // 2 - rect_width // 2
#     center_y = win_height // 2 - rect_height // 2
#     pygame.draw.rect(window, (255, 0, 0), (center_x,
#                      center_y, rect_width, rect_height))
#     pygame.draw.line(window, (255, 255, 0), (240, 120), (240, 340), 5)

#     # End drawing statements
#     pygame.display.update()  # Update the display ̰
#     clock.tick(60)  # Limit to 60 frames per second

# #######################################################################
# # EXAMPLE 3

# import pygame
# import sys

# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Drawing Example")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# # Circle parameters
# circle_center = (400, 300)
# circle_radius = 100

# # Rectangle parameters
# rect_x = 350
# rect_y = 250
# rect_width = 100
# rect_height = 50

# # Line parameters
# line_start = (200, 150)
# line_end = (600, 450)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(WHITE)

#     # Draw a blue circle
#     pygame.draw.circle(screen, BLUE, circle_center, circle_radius)

#     # Draw a red rectangle
#     pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

#     # Draw a green line
#     pygame.draw.line(screen, GREEN, line_start, line_end, 5)

#     # Draw a yellow ellipse
#     pygame.draw.ellipse(screen, YELLOW, (300, 200, 200, 100))

#     pygame.display.flip()

# pygame.quit()
# sys.exit()
#####################################################################################################
# EXAMPLE 4 - CLIP LINE TO RECTANGLE

import sys

# When tests import this module (e.g. pytest) we must not run GUI demos.
# Use RUN_DEMOS to guard runtime demos so import-time execution is avoided.
RUN_DEMOS = "pytest" not in sys.modules

if RUN_DEMOS:
    import pygame

    pygame.init()
    clock = pygame.time.Clock()  # Create a clock object to manage the frame rate
    win_width = 500
    win_height = 400
    window = pygame.display.set_mode((win_width, win_height))
    while True:
        for event in pygame.event():  # Handle events
            if event.type == pygame.QUIT:  # Handle window close
                pygame.quit()  # Close the Pygame window
                raise SystemExit  # Exit the program
        # Begin drawing statements
        # Draw a red rectangle centered in the window
        rect_width, rect_height = 100, 50
        win_width, win_height = 500, 400
        center_x = win_width // 2 - rect_width // 2
        center_y = win_height // 2 - rect_height // 2
        rect = pygame.Rect(center_x, center_y, rect_width, rect_height)
        pygame.draw.rect(window, (255, 0, 0), rect)

        # Line endpoints
        line_start = (100, 100)
        line_end = (400, 350)

        # End drawing statements
        pygame.display.update()  # Update the display ̰
        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()
    sys.exit()
##########################################################################################

# def draw_rainbow_squares():
#     import turtle

#     window = turtle.Screen()
#     window.title("Rainbow Squares")
#     window.bgcolor("white")
#     window.setup(width=800, height=600)
#     rainbow_colors = [
#         "#FF0000",
#         "#FF7F00",
#         "#FFFF00",
#         "#00FF00",
#         "#0000FF",
#         "#4B0082",
#         "#9400D3",
#     ]
#     start_x = -250
#     y = 0
#     size = 60
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.speed(0)
#     for i, color in enumerate(rainbow_colors):
#         t.penup()
#         t.goto(start_x + i * (size + 10), y)
#         t.pendown()
#         t.fillcolor(color)
#         t.begin_fill()
#         for _ in range(4):
#             t.forward(size)
#             t.left(90)
#         t.end_fill()
#         t.penup()
#         t.goto(start_x + i * (size + 10) + size // 2, y - 30)
#         t.pendown()
#         t.pencolor("black")
#         t.write(color, align="center", font=("Arial", 10, "normal"))
#     turtle.done()

# Uncomment below to run the rainbow demo
# draw_rainbow_squares()


def draw_color_boxes_with_hex():
    import turtle

    window = turtle.Screen()
    window.title("Color Boxes with Hex Codes")
    window.bgcolor("white")
    window.setup(width=800, height=200)
    rainbow_colors = [
        "#FF0000",
        "#FF7F00",
        "#FFFF00",
        "#00FF00",
        "#0000FF",
        "#4B0082",
        "#9400D3",
    ]
    start_x = -300
    y = 40
    size = 30
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    for i, color in enumerate(rainbow_colors):
        # Draw color box
        t.penup()
        t.goto(start_x + i * 100, y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(size)
            t.left(90)
        t.end_fill()
        # Write hex code next to box
        t.penup()
        t.goto(start_x + i * 100 + size + 10, y)
        t.pendown()
        t.pencolor("black")
        t.write(color, align="left", font=("Arial", 14, "normal"))
    turtle.done()


# Uncomment below to run the color box demo
if RUN_DEMOS:
    draw_color_boxes_with_hex()
