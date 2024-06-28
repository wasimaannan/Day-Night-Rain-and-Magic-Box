from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random

wind = 0
drop = 0
h_red = 0
h_green = 0
h_blue = 0
h_alpha = 0
bg_red = 1
bg_blue = 1
bg_green = 1
bg_alpha = 1


def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def draw_Lines(x, y, a, b):
    glLineWidth(8)  # pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glVertex2f(a, b)
    glEnd()


def draw_WD_Lines(x, y, a, b):
    glLineWidth(1)  # pixel size. by default 1 thake
    glBegin(GL_LINES)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glVertex2f(a, b)
    glEnd()


def draw_raindrop(x, y):
    global drop
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x, y + drop)
    glVertex2f(x - wind, (y - 15 + drop))
    glEnd()


def area(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area



def draw_house():
    glBegin(GL_LINES)
    # Roof
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(200, 600)
    glVertex2f(800, 600)
    glVertex2f(200, 600)
    glVertex2f(500, 800)
    glVertex2f(500, 800)
    glVertex2f(800, 600)

    # House body
    glColor3f(0.7, 0.9, 0.3)
    glVertex2f(220, 600)
    glVertex2f(220, 200)
    glVertex2f(220, 200)
    glVertex2f(780, 200)
    glVertex2f(780, 200)
    glVertex2f(780, 600)

    # Door
    glColor3f(0.7, 0.0, 0.3)
    glVertex2f(360, 200)
    glVertex2f(360, 420)
    glVertex2f(360, 420)
    glVertex2f(480, 420)
    glVertex2f(480, 420)
    glVertex2f(480, 200)

    # Window
    glColor3f(0.0, 0.5, 0.8)
    glVertex2f(580, 440)
    glVertex2f(700, 440)
    glVertex2f(580, 440)
    glVertex2f(580, 560)
    glVertex2f(580, 560)
    glVertex2f(700, 560)
    glVertex2f(700, 560)
    glVertex2f(700, 440)
    # glVertex2f(580, 500)
    # glVertex2f(700, 500)
    # glVertex2f(640, 560)
    # glVertex2f(640, 440)
    glEnd()


def draw_rain():
    global wind
    for i in range(150):  # num of raindrops
        x = random.randint(0, 1000) % 1000
        y = random.randint(0, 1000) % 1000
        if RainNotInRoof(x, y) and RainNotInHouse(x, y):
            draw_raindrop(x, y)


def RainNotInRoof(x, y):
    flag = False
    a = area(500, 840, 160, 600, 840, 600)
    a1 = area(x, y, 500, 840, 160, 600)
    a2 = area(x, y, 160, 600, 840, 600)
    a3 = area(x, y, 840, 600, 500, 840)

    if (a1 + a2 + a3) != a:
        flag = True
    return flag


def RainNotInHouse(x, y):
    flag = False

    house_left = 220
    house_right = 780
    house_bottom = 200
    house_top = 600

    if x < house_left or x > house_right or y < house_bottom or y > house_top:
        flag = True

    return flag


def specialKeyListener(key, x, y):
    global wind, h_red, h_green, h_blue, bg_blue, bg_red, bg_green, bg_alpha, h_alpha
    if key == GLUT_KEY_LEFT:
        wind += 1
        print("wind_left")
    if key == GLUT_KEY_RIGHT:
        wind -= 1
        print('wind_right')
    # if key == GLUT_KEY_DOWN:
    #     house = h_red
    #     if house >= 0:
    #         h_red -= 0.1
    #         h_blue -= 0.1
    #         h_green -= 0.1
    #         h_alpha -= 0.1
    #     bg = bg_red
    #     if bg <= 1:
    #         bg_red += 0.1
    #         bg_blue += 0.1
    #         bg_green += 0.1
    #         bg_alpha += 0.1
    # if key == GLUT_KEY_UP:
    #     house = h_red
    #     if house <= 1:
    #         h_red += 0.1
    #         h_blue += 0.1
    #         h_green += 0.1
    #         h_alpha += 0.1
    #     bg = bg_red
    #     if bg >= 0:
    #         bg_red -= 0.1
    #         bg_blue -= 0.1
    #         bg_green -= 0.1
    #         bg_alpha -= 0.1

    glutPostRedisplay()
def keyboard(key, x, y):
    global wind, h_red, h_green, h_blue, bg_blue, bg_red, bg_green, bg_alpha, h_alpha
    if key == b'd':
        house = h_red
        if house >= 0:
            h_red -= 0.1
            h_blue -= 0.1
            h_green -= 0.1
            h_alpha -= 0.1
        bg = bg_red
        if bg <= 1:
            bg_red += 0.1
            bg_blue += 0.1
            bg_green += 0.1
            bg_alpha += 0.1
    elif key == b'n':
        house = h_red
        if house <= 1:
            h_red += 0.1
            h_blue += 0.1
            h_green += 0.1
            h_alpha += 0.1
        bg = bg_red
        if bg >= 0:
            bg_red -= 0.1
            bg_blue -= 0.1
            bg_green -= 0.1
            bg_alpha -= 0.1

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global h_red, h_blue, h_green, bg_red, bg_blue, bg_green, bg_alpha
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glClearColor(bg_red, bg_blue, bg_green, bg_alpha)
    glColor3f(h_red, h_blue, h_green)
    draw_rain()
    draw_house()
    glutPostRedisplay()
    glutSwapBuffers()


def animate():
    global drop
    b = (drop + 1) % 15
    glutPostRedisplay()


def init():
    global bg_red, bg_blue, bg_green, bg_alpha
    glClearColor(bg_red, bg_blue, bg_green, bg_alpha)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)  # window size
glutInitWindowPosition(0, 0)
a = glutCreateWindow(b"House in the rain")  # window name
init()
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyboard)
glutMainLoop()
