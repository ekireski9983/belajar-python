import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_donut():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5)

    glRotatef(1, 3, 1, 1)

    glBegin(GL_QUADS)
    glColor3fv((1,0,0))
    glVertex3fv((-1, 1, 0))
    glVertex3fv((1, 1, 0))
    glVertex3fv((1, -1, 0))
    glVertex3fv((-1, -1, 0))
    glEnd()

    pygame.display.flip()
    pygame.time.wait(10)

pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0,-5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_donut()
