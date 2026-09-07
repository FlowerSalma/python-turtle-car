import turtle
from PIL import ImageGrab
import time

# ==========================================================
# SCREEN
# ==========================================================

wn = turtle.Screen()
wn.setup(1200, 760)
wn.bgcolor("white")
wn.title("Salma's Concept Car")

# ==========================================================
# TURTLE
# ==========================================================

salma = turtle.Turtle()
salma.shape("turtle")

# Use 5 if you want to watch the turtle draw.
# Change to 0 for fastest drawing.
salma.speed(5)

salma.pensize(2)
salma.color("black")

# ==========================================================
# BASIC MOVEMENT
# ==========================================================

def jump(x, y):
    salma.penup()
    salma.goto(x, y)
    salma.pendown()


def line(points, color="black", width=2):
    salma.color(color)
    salma.pensize(width)

    jump(points[0][0], points[0][1])

    for x, y in points[1:]:
        salma.goto(x, y)


def fill_shape(points, fill_color):
    salma.color(fill_color, fill_color)

    jump(points[0][0], points[0][1])

    salma.begin_fill()

    for x, y in points[1:]:
        salma.goto(x, y)

    salma.goto(points[0][0], points[0][1])

    salma.end_fill()

# ==========================================================
# BÉZIER CURVE
# ==========================================================

def bezier(
    start,
    control,
    end,
    color="black",
    width=2,
    steps=50
):
    salma.color(color)
    salma.pensize(width)

    jump(start[0], start[1])

    for i in range(1, steps + 1):

        t = i / steps

        x = (
            (1 - t) ** 2 * start[0]
            + 2 * (1 - t) * t * control[0]
            + t ** 2 * end[0]
        )

        y = (
            (1 - t) ** 2 * start[1]
            + 2 * (1 - t) * t * control[1]
            + t ** 2 * end[1]
        )

        salma.goto(x, y)

# ==========================================================
# CIRCLE
# ==========================================================

def circle_at(
    x,
    y,
    radius,
    outline,
    fill=None,
    width=2
):
    jump(x, y - radius)

    salma.setheading(0)
    salma.pensize(width)

    if fill:
        salma.color(outline, fill)

        salma.begin_fill()
        salma.circle(radius)
        salma.end_fill()

    else:
        salma.color(outline)
        salma.circle(radius)

# ==========================================================
# WHEEL
# ==========================================================

def wheel(x, y, radius):

    # Tire
    circle_at(
        x,
        y,
        radius,
        "#050708",
        "#050708",
        3
    )

    # Outer rim
    circle_at(
        x,
        y,
        radius * 0.75,
        "#D9E3E8",
        "#17242A",
        3
    )

    # Brake disc
    circle_at(
        x,
        y,
        radius * 0.50,
        "#60747C",
        "#26373E",
        2
    )

    # Spokes
    salma.color("#DDEBF0")
    salma.pensize(3)

    for angle in range(0, 360, 30):

        jump(x, y)
        salma.setheading(angle)
        salma.forward(radius * 0.63)

    # Hub
    jump(x, y)
    salma.dot(18, "#DDEBF0")

    jump(x, y)
    salma.dot(8, "#00AACC")

# ==========================================================
# ROAD
# ==========================================================

jump(-560, -220)

salma.setheading(0)
salma.color("#999999")
salma.pensize(4)

salma.forward(1120)

# ==========================================================
# MAIN CAR BODY
# ==========================================================

body = [
    (-500, -120),
    (-485, -75),
    (-440, -40),
    (-350, -10),
    (-265, 18),

    (-185, 110),
    (-100, 145),
    (20, 158),
    (140, 145),
    (245, 100),

    (330, 42),
    (430, 20),
    (495, -20),
    (520, -75),
    (495, -120),

    (410, -145),
    (355, -145),
    (310, -120),

    (250, -120),
    (205, -145),

    (-205, -145),
    (-250, -120),

    (-310, -120),
    (-355, -145),
    (-425, -140)
]

fill_shape(body, "red")

# ==========================================================
# REAR EXTERIOR
# ==========================================================

line(
    [
        (-500, -120),
        (-485, -75),
        (-440, -40),
        (-350, -10),
        (-265, 18)
    ],
    "black",
    3
)

# ==========================================================
# ROOF
# ==========================================================

bezier(
    (-265, 18),
    (-175, 180),
    (20, 158),
    "black",
    4
)

bezier(
    (20, 158),
    (180, 165),
    (330, 42),
    "black",
    4
)

# ==========================================================
# FRONT EXTERIOR
# ==========================================================

line(
    [
        (330, 42),
        (430, 20),
        (495, -20),
        (520, -75),
        (495, -120)
    ],
    "black",
    3
)

# ==========================================================
# LOWER BODY
# ==========================================================

line(
    [
        (-425, -140),
        (-355, -145),
        (-310, -120)
    ],
    "black",
    3
)

line(
    [
        (-250, -120),
        (-205, -145),
        (205, -145),
        (250, -120)
    ],
    "black",
    3
)

line(
    [
        (310, -120),
        (355, -145),
        (410, -145),
        (495, -120)
    ],
    "black",
    3
)

# ==========================================================
# REAR WINDOW
# ==========================================================

rear_window = [
    (-215, 40),
    (-153, 110),
    (-95, 137),
    (12, 145),
    (45, 42)
]

fill_shape(rear_window, "#102A33")

line(
    rear_window + [rear_window[0]],
    "#1DA1A1",
    2
)

# ==========================================================
# FRONT WINDOW
# ==========================================================

front_window = [
    (70, 142),
    (150, 125),
    (245, 77),
    (290, 42),
    (85, 42)
]

fill_shape(front_window, "#102A33")

line(
    front_window + [front_window[0]],
    "#1DA1A1",
    2
)

# Window divider
line(
    [
        (53, 140),
        (65, 42)
    ],
    "black",
    4
)

# ==========================================================
# WHEEL ARCHES
# ==========================================================

bezier(
    (-385, -125),
    (-315, 10),
    (-235, -125),
    "black",
    3
)

bezier(
    (230, -125),
    (310, 10),
    (395, -125),
    "black",
    3
)

# ==========================================================
# SIDE CHARACTER LINE
# ==========================================================

bezier(
    (-425, -40),
    (-80, 5),
    (375, -35),
    "#444444",
    2
)

# ==========================================================
# LOWER AERODYNAMIC LINE
# ==========================================================

bezier(
    (-210, -102),
    (20, -130),
    (215, -102),
    "#444444",
    2
)

# ==========================================================
# HEADLIGHT
# ==========================================================

headlight = [
    (350, 7),
    (448, -7),
    (412, -37),
    (332, -27)
]

fill_shape(
    headlight,
    "#8CFFFF"
)

line(
    headlight + [headlight[0]],
    "black",
    2
)

line(
    [
        (352, -5),
        (415, -17),
        (390, -27)
    ],
    "black",
    3
)

# ==========================================================
# REAR LIGHT
# ==========================================================

tail_light = [
    (-440, -30),
    (-482, -46),
    (-458, -72),
    (-408, -50)
]

fill_shape(
    tail_light,
    "#D7263D"
)

line(
    tail_light + [tail_light[0]],
    "black",
    2
)

# ==========================================================
# FRONT AIR INTAKE
# ==========================================================

air_intake = [
    (412, -78),
    (500, -68),
    (475, -112),
    (390, -112)
]

fill_shape(
    air_intake,
    "#050708"
)

line(
    air_intake + [air_intake[0]],
    "#566C75",
    2
)

# ==========================================================
# DOOR LINES
# ==========================================================

line(
    [
        (-125, 32),
        (-115, -82)
    ],
    "#555555",
    1
)

line(
    [
        (75, 34),
        (85, -82)
    ],
    "#555555",
    1
)

# ==========================================================
# DOOR HANDLES
# ==========================================================

line(
    [
        (-70, -15),
        (-27, -15)
    ],
    "black",
    4
)

line(
    [
        (125, -15),
        (168, -15)
    ],
    "black",
    4
)

# ==========================================================
# MIRROR
# ==========================================================

mirror = [
    (-140, 53),
    (-178, 61),
    (-193, 43),
    (-150, 36)
]

fill_shape(
    mirror,
    "#CCCCCC"
)

line(
    mirror + [mirror[0]],
    "black",
    2
)

# ==========================================================
# WHEELS
# ==========================================================

wheel(
    -310,
    -140,
    78
)

wheel(
    310,
    -140,
    78
)

# ==========================================================
# FRONT SPLITTER
# ==========================================================

line(
    [
        (390, -120),
        (500, -120),
        (520, -130)
    ],
    "#00AACC",
    4
)

# ==========================================================
# REAR DIFFUSER
# ==========================================================

line(
    [
        (-500, -120),
        (-450, -135),
        (-407, -135)
    ],
    "#00AACC",
    4
)

# ==========================================================
# SIGNATURE
# ==========================================================



jump(0, -285)
salma.color("#222222")

salma.write(
    "Salma Hasannejad",
    align="center",
    font=("Arial", 16, "bold")
)

jump(0, -315)
salma.color("#444444")

salma.write(
    "PYTHON TURTLE SKETCH",
    align="center",
    font=("Arial", 12, "normal")
)

jump(0, -340)
salma.color("#666666")

salma.write(
    "DATA SCIENCE  •  MATHEMATICS  •  CREATIVITY",
    align="center",
    font=("Arial", 10, "normal")
)
# ==========================================================
# SHOW LITTLE TURTLE AT THE END
# ==========================================================

salma.shape("turtle")
salma.color("green")

jump(535, -190)
salma.setheading(145)

# ==========================================================
# SAVE FINISHED DRAWING AS PNG
# ==========================================================

wn.update()

# Allow the Turtle window to fully render
time.sleep(1)

# Hide the turtle only before saving the image
salma.hideturtle()

wn.update()
time.sleep(0.5)

# Get the Turtle canvas
canvas = wn.getcanvas()

# Find the canvas location on the screen
x = canvas.winfo_rootx()
y = canvas.winfo_rooty()

width = canvas.winfo_width()
height = canvas.winfo_height()

# Capture only the Turtle drawing area
image = ImageGrab.grab(
    bbox=(
        x,
        y,
        x + width,
        y + height
    )
)

# Save the output
image.save("red_car.png")

print("✓ Drawing saved as red_car.png")

# ==========================================================
# KEEP WINDOW OPEN
# ==========================================================

wn.exitonclick()