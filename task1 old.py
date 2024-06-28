from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window dimensions
W_Width, W_Height = 1000, 1000

# House boundaries
house_left, house_right = -200, 200
house_bottom, house_top = -300, 0
roof_top = 200

# Rain parameters
num_raindrops = 100
raindrops = []
rain_direction = [0, -5]  # Falling straight down initially

# Background color (day to night)
background_color = [0.0, 0.0, 0.0]  # Start with night
bg_increment = 0.01  # Increment for background color change


def draw_house():
    glBegin(GL_LINES)
    glColor3f(0.7, 0.9, 0.3)
    glVertex2f(-200, -300)
    glVertex2f(200, -300)
    glVertex2f(200, -300)
    glVertex2f(200, 0)
    glVertex2f(200, 0)
    glVertex2f(-200, 0)
    glVertex2f(-200, 0)
    glVertex2f(-200, -300)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-200, 0)
    glVertex2f(200, 0)
    glVertex2f(200, 0)
    glVertex2f(0, 200)
    glVertex2f(0, 200)
    glVertex2f(-200, 0)
    glColor3f(0.7, 0.0, 0.3)
    glVertex2f(-40, -300)
    glVertex2f(-40, -150)
    glVertex2f(-40, -150)
    glVertex2f(-160, -150)
    glVertex2f(-160, -150)
    glVertex2f(-160, -300)
    glColor3f(0.0, 0.5, 0.8)
    glVertex2f(50, -150)
    glVertex2f(180, -150)
    glVertex2f(180, -150)
    glVertex2f(180, -50)
    glVertex2f(50, -50)
    glVertex2f(180, -50)
    glVertex2f(50, -50)
    glVertex2f(50, -150)
    glEnd()


def draw_raindrops():
    glPointSize(5.0)  # Set the point size to make raindrops bigger
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.9, 1.0)
    for drop in raindrops:
        glVertex2f(drop[0], drop[1])
    glEnd()


def update_raindrops():
    global raindrops
    for i in range(len(raindrops)):
        raindrops[i][0] += rain_direction[0]
        raindrops[i][1] += rain_direction[1]
        if raindrops[i][1] < -W_Height / 2:
            raindrops[i] = generate_raindrop()


def generate_raindrop():
    x = random.randint(-W_Width // 2, W_Width // 2)
    y = random.randint(-W_Height // 2, W_Height // 2)

    while (house_left <= x <= house_right) and (house_bottom <= y <= roof_top):
        x = random.randint(-W_Width // 2, W_Width // 2)
        y = random.randint(-W_Height // 2, W_Height // 2)

    return [x, y]


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(*background_color, 1)  # Background color
    glLoadIdentity()
    gluOrtho2D(-W_Width / 2, W_Width / 2, -W_Height / 2, W_Height / 2)

    draw_house()
    draw_raindrops()

    glutSwapBuffers()


def idle():
    update_raindrops()
    glutPostRedisplay()


def special_keys(key, x, y):
    global rain_direction
    if key == GLUT_KEY_LEFT:
        rain_direction[0] -= 1
    elif key == GLUT_KEY_RIGHT:
        rain_direction[0] += 1


def keyboard(key, x, y):
    global background_color
    if key == b'n':  # Simulate night to day
        if background_color[0] < 1.0:
            background_color[0] += bg_increment
            background_color[1] += bg_increment
            background_color[2] += bg_increment
    elif key == b'd':  # Simulate day to night
        if background_color[0] > 0.0:
            background_color[0] -= bg_increment
            background_color[1] -= bg_increment
            background_color[2] -= bg_increment


def init():
    global raindrops
    raindrops = [generate_raindrop() for _ in range(num_raindrops)]
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-W_Width / 2, W_Width / 2, -W_Height / 2, W_Height / 2)


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutCreateWindow(b"House in the Rain")

init()
glutDisplayFunc(display)
glutIdleFunc(idle)
glutSpecialFunc(special_keys)
glutKeyboardFunc(keyboard)
glutMainLoop()
