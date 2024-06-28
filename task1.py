from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

W_Width, W_Height = 1000,1000

wind = 0
drop = 0

houseRed = 0
houseGreen = 0
houseBlue = 0
houseAlpha = 0

bgRed = 1
bgBlue = 1
bgGreen = 1
bgAlpha = 1


def draw_points(x, y):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # jekhane show korbe pixel
    glEnd()


def draw_raindrop(x, y):
    global drop
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(x,y+drop)
    glVertex2f(x-wind,(y-15+drop))
    glEnd()


def area(x1, y1, x2, y2, x3, y3):
    area = 0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
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
    glEnd()


def draw_rain():
    global wind
    for i in range(500):
        x = random.randint(0,1000)%1000
        y = random.randint(0,1000)%1000
        if RainNotInRoof(x,y) and RainNotInHouse(x,y):
            draw_raindrop(x,y)

def RainNotInRoof(x, y):
    flag = False
    a = area(500,840,160,600,840,600)
    a1 = area(x,y,500,840,160,600)
    a2 = area(x,y,160,600,840,600)
    a3 = area(x,y,840,600,500,840)
    if (a1+a2+a3)!=a:
        flag=True
    return flag

def RainNotInHouse(x, y):
    flag = False
    houseLeft = 220
    houseRight = 780
    houseBottom = 200
    houseTop = 600
    if x<houseLeft or x>houseRight or y<houseBottom or y>houseTop:
        flag = True
    return flag


def specialKeyListener(key, x, y):
    global wind, houseRed, houseGreen,houseBlue, houseAlpha, bgBlue, bgRed, bgGreen, bgAlpha
    if key == GLUT_KEY_LEFT:
        wind += 1
        print("wind left")
    if key == GLUT_KEY_RIGHT:
        wind -= 1
        print('wind right')

    glutPostRedisplay()

def keyboardListener(key, x, y):
    global wind, houseRed, houseGreen, houseBlue, houseAlpha, bgBlue, bgRed, bgGreen, bgAlpha
    if key == b'd':
        house = houseRed
        if house >= 0:
            houseRed -= 0.1
            houseBlue -= 0.1
            houseGreen -= 0.1
            houseAlpha -= 0.1
        bg = bgRed
        if bg <= 1:
            bgRed += 0.1
            bgBlue += 0.1
            bgGreen += 0.1
            bgAlpha += 0.1
    elif key == b'n':
        house = houseRed
        if house <= 1:
            houseRed += 0.1
            houseBlue += 0.1
            houseGreen += 0.1
            houseAlpha += 0.1
        bg = bgRed
        if bg >= 0:
            bgRed -= 0.1
            bgBlue -= 0.1
            bgGreen -= 0.1
            bgAlpha -= 0.1

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    global houseRed, houseBlue, houseGreen, bgRed, bgBlue, bgGreen, bgAlpha
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glClearColor(bgRed, bgBlue, bgGreen, bgAlpha)
    glColor3f(houseRed,houseBlue, houseGreen)
    draw_rain()
    draw_house()
    glutPostRedisplay()
    glutSwapBuffers()


def animate():
    global drop
    b = (drop+1)%15
    glutPostRedisplay()


def init():
    global bgRed, bgBlue, bgGreen, bgAlpha
    glClearColor(bgRed, bgBlue, bgGreen, bgAlpha)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
a = glutCreateWindow(b"Building a House in Rainfall")
init()

glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()		#The main loop of OpenGL