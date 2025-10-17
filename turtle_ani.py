import turtle
import math
import random

radius = 300
rotation_speed = 0.02

window = turtle.Screen()
window.tracer(0)
window.setup(1000, 1000)
window.bgcolor(0.1, 0.1, 0.2)

n_dots = 800
dots = []
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta", "white"]

for _ in range(n_dots):
    while True:
        x = random.randint(-window.window_width() // 2, window.window_width() // 2)
        y = random.randint(-window.window_height() // 2, window.window_height() // 2)
        # Discard points that fall outside the sphere
        if x ** 2 + y ** 2 <= radius ** 2:
            break
    dot = turtle.Turtle()
    dot.penup()
    dot.shape("circle")
    dot.setposition(x, y)  # Set the position of the dot
    dot.base_color = random.choice(colors) # Assign a base color randomly
    dot.color(dot.base_color)
    dot.turtlesize(0.15)
    dot.radians() # Use radians for angle calculations
    dot.small_radius = math.sqrt(radius ** 2 - y ** 2) # Calculate the small radius by pythagoras
    dot.theta = random.uniform(0, 2 * math.pi) # Random starting angle for each dot
    dot.twinkle = random.choice([True, False]) # Randomly decide which dot will twinkle
    dots.append(dot) # Append the dot to the list
while True:
    for dot in dots:
        x = dot.small_radius * math.sin(dot.theta) # Calculate new x position
        dot.setx(x) # Update the x position of the dot
        dot.theta += rotation_speed
        # More visible twinkle: higher chance, bigger size, color change
        if dot.twinkle and random.random() < 0.08: # 8% chance to twinkle
            dot.turtlesize(random.uniform(0.05, 0.6)) # Random size for twinkle between 0.05 and 0.6(floating)
            dot.color("white") # Change color to white when twinkling
        else:
            dot.turtlesize(0.15)
            dot.color(dot.base_color)
    window.update()