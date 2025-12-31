"""my_turtle.py

Annotated cheat-sheet for Python's `turtle` module.

This file is a compact reference with common functions, aliases, and
small usage examples. It's intended as a quick local cheat-sheet; run
snippets interactively or in scripts that end with `turtle.mainloop()`.

Notes:
- Prefer `import turtle as t` in scripts to avoid polluting the global
  namespace (and to keep names explicit).
- `turtle` requires Tk (`_tkinter`) available on the system.

Examples below assume `import turtle as t`.
"""

# Quick import patterns
# from turtle import *          # convenient for quick experiments (not recommended in scripts)
# import turtle as t           # recommended in scripts

# Basic motion (move and turn)
# t.forward(100)   # move forward 100 pixels (alias: t.fd)
# t.backward(50)   # move backward 50 (alias: t.back, t.bk)
# t.right(90)      # rotate clockwise 90 degrees (alias: t.rt)
# t.left(45)       # rotate counter-clockwise 45 degrees (alias: t.lt)

# Pen control
# t.pendown() / t.pd()        # start drawing
# t.penup() / t.pu()          # stop drawing (move without drawing)
# t.pensize(3) / t.width(3)   # line width
# t.color('red')              # set pen and fill color
# t.begin_fill(); t.circle(50); t.end_fill()

# Position & state
# t.pos() / t.position()      # returns (x, y)
# t.xcor(), t.ycor()          # coordinates
# t.home()                    # move to (0,0) and reset heading
# t.speed(0)                  # animation speed (0 = no animation)

# Shapes, stamps and dots
# t.shape('turtle')  # shape names: 'arrow','turtle','circle','square','triangle','classic'
# t.stamp()          # stamp the current shape on the canvas
# t.dot(10, 'blue')  # draw a circular dot

# Screen control
# import turtle as t
# screen = t.Screen()
# screen.bgcolor('lightblue')
# screen.setup(600, 400)
# screen.title('My Turtle Demo')
# screen.mainloop()   # keep the window open (or t.mainloop()/t.done())

# Reverse/animation control
# t.tracer(n, delay)  # set update frequency and delay (useful for fast batch drawing)
# t.update()          # manually update when tracer(0) used

# Object-oriented interface (recommended for non-trivial programs):
# from turtle import Turtle, Screen
# screen = Screen()
# t1 = Turtle()           # a new Turtle instance
# t2 = Turtle()           # can have multiple turtles drawing independently
# t1.forward(80)
# t2.color('red'); t2.left(90); t2.forward(40)
# screen.mainloop()

# Events & interactivity
# screen.onclick(lambda x, y: print('clicked', x, y))
# screen.onkey(lambda: print('key pressed'), 'space')
# screen.listen()

# Useful small patterns
# last key of a dict (insertion order preserved since Python 3.7)
# last_key = next(reversed(some_dict))

# Example: simple drawing function (safe to import; execute only when run as script)


def draw_example():
    import turtle as t

    screen = t.Screen()
    screen.title("Turtle Cheat-sheet Demo")
    t.speed("fastest")

    t.color("navy")
    for i in range(36):
        t.forward(150)
        t.right(170)

    # keep window open
    screen.mainloop()


if __name__ == "__main__":
    # Running the module will open a small demo window (requires a GUI).
    # Comment out the next line if running in a headless environment.
    try:
        draw_example()
    except Exception as e:
        print("Could not run turtle demo here:", e)
"""my_turtle.py

Annotated cheat-sheet for Python's `turtle` module.

This file is a compact reference with common functions, aliases, and
small usage examples. It's intended as a quick local cheat-sheet; run
snippets interactively or in scripts that end with `turtle.mainloop()`.

Notes:
- Prefer `import turtle as t` in scripts to avoid polluting the global
  namespace (and to keep names explicit).
- `turtle` requires Tk (`_tkinter`) available on the system.

Examples below assume `import turtle as t`.
"""

# Quick import patterns
# from turtle import *          # convenient for quick experiments (not recommended in scripts)
# import turtle as t           # recommended in scripts

# Basic motion (move and turn)
# t.forward(100)   # move forward 100 pixels (alias: t.fd)
# t.backward(50)   # move backward 50 (alias: t.back, t.bk)
# t.right(90)      # rotate clockwise 90 degrees (alias: t.rt)
# t.left(45)       # rotate counter-clockwise 45 degrees (alias: t.lt)

# Pen control
# t.pendown() / t.pd()        # start drawing
# t.penup() / t.pu()          # stop drawing (move without drawing)
# t.pensize(3) / t.width(3)   # line width
# t.color('red')              # set pen and fill color
# t.begin_fill(); t.circle(50); t.end_fill()

# Position & state
# t.pos() / t.position()      # returns (x, y)
# t.xcor(), t.ycor()          # coordinates
# t.home()                    # move to (0,0) and reset heading
# t.speed(0)                  # animation speed (0 = no animation)

# Shapes, stamps and dots
# t.shape('turtle')  # shape names: 'arrow','turtle','circle','square','triangle','classic'
# t.stamp()          # stamp the current shape on the canvas
# t.dot(10, 'blue')  # draw a circular dot

# Screen control
# import turtle as t
# screen = t.Screen()
# screen.bgcolor('lightblue')
# screen.setup(600, 400)
# screen.title('My Turtle Demo')
# screen.mainloop()   # keep the window open (or t.mainloop()/t.done())

# Reverse/animation control
# t.tracer(n, delay)  # set update frequency and delay (useful for fast batch drawing)
# t.update()          # manually update when tracer(0) used

# Object-oriented interface (recommended for non-trivial programs):
# from turtle import Turtle, Screen
# screen = Screen()
# t1 = Turtle()           # a new Turtle instance
# t2 = Turtle()           # can have multiple turtles drawing independently
# t1.forward(80)
# t2.color('red'); t2.left(90); t2.forward(40)
# screen.mainloop()

# Events & interactivity
# screen.onclick(lambda x, y: print('clicked', x, y))
# screen.onkey(lambda: print('key pressed'), 'space')
# screen.listen()

# Useful small patterns
# last key of a dict (insertion order preserved since Python 3.7)
# last_key = next(reversed(some_dict))

# Example: simple drawing function (safe to import; execute only when run as script)


def draw_example():
    import turtle as t

    screen = t.Screen()
    screen.title("Turtle Cheat-sheet Demo")
    t.speed("fastest")

    t.color("navy")
    for i in range(36):
        t.forward(150)
        t.right(170)

    # keep window open
    screen.mainloop()


if __name__ == "__main__":
    # Running the module will open a small demo window (requires a GUI).
    # Comment out the next line if running in a headless environment.
    try:
        draw_example()
    except Exception as e:
        print("Could not run turtle demo here:", e)
