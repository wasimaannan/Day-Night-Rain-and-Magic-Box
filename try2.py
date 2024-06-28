import sys
import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window dimensions
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

# Speed constants
min_speed = 0.01
max_speed = 1.0
speed_increment = 0.01

# Frozen state
frozen = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(-1, 1)
        self.dy = random.uniform(-1, 1)
        self.color = (random.random(), random.random(), random.random())
        self.speed = min_speed
        self.size = 5.0

points = []

def convert_coordinate(x, y):
    return x, WINDOW_HEIGHT - y

def create_point(x, y):
    c_x, c_y = convert_coordinate(x, y)
    points.append(Point(c_x, c_y))

def draw_points():
    glClear(GL_COLOR_BUFFER_BIT)
    for point in points:
        glPointSize(point.size)
        glBegin(GL_POINTS)
        glColor3f(*point.color)
        glVertex2f(point.x, point.y)
        glEnd()
    glutSwapBuffers()

def update_points():
    if not frozen:
        for point in points:
            point.x += point.dx * point.speed
            point.y += point.dy * point.speed

            # Simple boundary check (wrap around)
            if point.x < 0 or point.x > WINDOW_WIDTH:
                point.dx = -point.dx
            if point.y < 0 or point.y > WINDOW_HEIGHT:
                point.dy = -point.dy

def display_callback():
    draw_points()

def reshape_callback(width, height):
    global WINDOW_WIDTH, WINDOW_HEIGHT
    WINDOW_WIDTH = width
    WINDOW_HEIGHT = height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, height, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)

def mouse_callback(button, state, x, y):
    if state == GLUT_DOWN and not frozen:
        create_point(x, y)

def keyboard_callback(key, x, y):
    global frozen
    if key == b' ':
        frozen = not frozen
    elif key == b'\x1b':
        sys.exit(0)

def special_callback(key, x, y):
    global points
    if key == GLUT_KEY_UP and not frozen:
        for point in points:
            point.speed += speed_increment
            if point.speed > max_speed:
                point.speed = max_speed
    elif key == GLUT_KEY_DOWN and not frozen:
        for point in points:
            point.speed -= speed_increment
            if point.speed < min_speed:
                point.speed = min_speed

def idle_callback():
    update_points()
    glutPostRedisplay()

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)  # Clear color set to white

# Initialize GLUT and create window
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow(b"Amazing Box")

# Register callbacks
glutDisplayFunc(display_callback)
glutReshapeFunc(reshape_callback)
glutMouseFunc(mouse_callback)
glutKeyboardFunc(keyboard_callback)
glutSpecialFunc(special_callback)
glutIdleFunc(idle_callback)

# Initialize OpenGL
init()

# Start the main event loop
glutMainLoop()
