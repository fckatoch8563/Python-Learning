# SHOWING DERIVATIVE OF SINE FUNCTION AND TANGENT LINE AT A POINT PI/4 = 45 degrees.
# SHIFT TANGENT LINE BY CHANGING THE ANGLE THETA.



import numpy as np
import matplotlib.pyplot as plt

# Set theta for tangent (in degrees)
theta_deg = 45  # Change this value to see the tangent move
theta = np.radians(theta_deg) # Convert degrees to radians

# Generate theta values for the curve
x = np.linspace(0, 2 * np.pi, 500) # 0 to 2π
y = np.sin(x) # sine values in radians
dy_dx = np.cos(x) # rate of change in y wrt x.

# Calculate tangent line at theta
y0 = np.sin(theta) # y value at theta at 0 < θ < 2π
slope = np.cos(theta) # slope of tangent line at theta or derivative of sin(x)
# Tangent line: y = y0 + slope * (x - theta)
tangent = y0 + slope * (x - theta) # equation of the tangent line

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='sin(x)')
plt.plot(x, dy_dx, label='cos(x) (derivative)', linestyle='--')
plt.plot(x, tangent, label=f'Tangent at θ={theta_deg}°', color='red')
plt.scatter([theta], [y0], color='black', zorder=5, label='Point of Tangency')
plt.xlabel('θ (radians)')
plt.ylabel('Value')
plt.title('Sine Curve, Derivative, and Tangent Line')
plt.legend()
plt.grid(True)
plt.show()
################################################################################################
# CHANGE THE ANGLE THETA TO SEE THE TANGENT LINE SLIDE AND ROTATE ALONG THE CURVE.

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 2 * np.pi, 500)
# y = np.sin(x)
# dy_dx = np.cos(x)

# plt.figure(figsize=(10, 6))
# plt.plot(x, y, label='sin(x)')
# plt.plot(x, dy_dx, label='cos(x) (derivative)', linestyle='--')

# # Plot tangent lines at several angles
# for theta_deg in range(0, 360, 45):  # Every 45 degrees from 0 to 360
#     theta = np.radians(theta_deg)
#     y0 = np.sin(theta)
#     slope = np.cos(theta)
#     tangent = y0 + slope * (x - theta)
#     plt.plot(x, tangent, label=f'Tangent at {theta_deg}°')

#     # Mark the point of tangency
#     plt.scatter([theta], [y0], color='black', zorder=5)

# plt.xlabel('θ (radians)')
# plt.ylabel('Value')
# plt.title('Sine Curve, Derivative, and Tangent Lines')
# plt.legend()
# plt.grid(True)
# plt.show()
####################################################################################
# Animated Sine and Cosine on Same Plane with Circle Projection

import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Animated Sine and Cosine on Same Plane with Circle Projection")
screen.setup(width=1000, height=600)
screen.tracer(0)

# Parameters
R = 120
center_x, center_y = -250, 0
wave_length = 720  # degrees
step = 2

# Drawing the circle
circle_drawer = turtle.Turtle()
circle_drawer.hideturtle()
circle_drawer.penup()
circle_drawer.goto(center_x, center_y - R) # Move to the bottom of the circle
circle_drawer.pendown()
circle_drawer.pensize(3)
circle_drawer.color("black")
circle_drawer.circle(R)

# Setting up the moving dot
moving_dot = turtle.Turtle()
moving_dot.shape("circle")
moving_dot.color("blue")
moving_dot.penup()
moving_dot.shapesize(1.2)

# Setting up the sine curve
sine_curve = turtle.Turtle()
sine_curve.hideturtle()
sine_curve.color("red")
sine_curve.pensize(2)
sine_curve.penup()
sine_curve.goto(center_x + R + 50, center_y)
sine_curve.pendown()

# Setting up the cosine curve
cos_curve = turtle.Turtle()
cos_curve.hideturtle()
cos_curve.color("green")
cos_curve.pensize(2)
cos_curve.penup()
cos_curve.goto(center_x + R + 50, center_y)
cos_curve.pendown()

# Setting up the circle trace
circle_trace = turtle.Turtle()
circle_trace.hideturtle()
circle_trace.color("blue")
circle_trace.pensize(2)
circle_trace.penup()

# Setting up the projection lines
proj_lines = turtle.Turtle()
proj_lines.hideturtle()
proj_lines.pensize(1)

# Setting up the axis
axis = turtle.Turtle()
axis.hideturtle()
axis.color("gray")
axis.pensize(1)


# Shared axis for both sine and cosine
axis.penup()
axis.goto(center_x + R + 50, center_y)
axis.pendown()
axis.goto(center_x + R + 50 + wave_length, center_y)


# Animation loop
angle = 0
sine_points = []
cos_points = []

while angle <= wave_length:
    theta = math.radians(angle)
    # Moving dot on circle
    x = center_x + R * math.cos(theta)
    y = center_y + R * math.sin(theta)
    moving_dot.goto(x, y)
    # Trace circle
    circle_trace.goto(x, y)
    if angle == 0:
        circle_trace.pendown()
    else:
        circle_trace.pendown()
    
     # Sine curve (right of circle, red)
    sx = center_x + R + 50 + angle
    sy = center_y + R * math.sin(theta)
    sine_curve.goto(sx, sy)
    sine_curve.dot(5, "red")
    sine_points.append((sx, sy))

    # Cosine curve (right of circle, green, on same axis)
    cx = center_x + R + 50 + angle
    cy = center_y + R * math.cos(theta)
    cos_curve.goto(cx, cy)
    cos_curve.dot(5, "green")
    cos_points.append((cx, cy))

    # Projection lines
    proj_lines.clear()
    # From circle dot to sine curve
    proj_lines.color("red")
    proj_lines.penup()
    proj_lines.goto(x, y)
    proj_lines.pendown()
    proj_lines.goto(sx, sy)


    # From circle dot to cosine curve
    proj_lines.color("green")
    proj_lines.penup()
    proj_lines.goto(x, y)
    proj_lines.pendown()
    proj_lines.goto(cx, cy)


    # From sine to cosine (vertical)
    proj_lines.color("purple")
    proj_lines.penup()
    proj_lines.goto(sx, sy)
    proj_lines.pendown()
    proj_lines.goto(cx, cy)
    screen.update()
    angle += step

screen.mainloop()