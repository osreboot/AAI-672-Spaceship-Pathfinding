from math import *
from OpenGL.GL import *


def draw_ship(ship):
    # Rotate around ship center
    glPushMatrix()
    glTranslatef(ship.x, ship.y, 0)
    glRotatef(ship.dir + 90, 0, 0, 1)
    glTranslatef(-ship.x, -ship.y, 0)

    glColor4f(0.5, 0.5, 0.5, 1.0)

    # Draw base
    glBegin(GL_QUADS)
    glVertex2f(ship.x - 5, ship.y - 5)
    glVertex2f(ship.x + 5, ship.y - 5)
    glVertex2f(ship.x + 5, ship.y + 5)
    glVertex2f(ship.x - 5, ship.y + 5)
    glEnd()

    # Draw nose
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(ship.x - 5, ship.y - 5)
    glVertex2f(ship.x, ship.y - 10)
    glVertex2f(ship.x + 5, ship.y - 5)
    glEnd()

    glColor4f(1.0, 1.0, 0.0, 1.0)

    # Draw trail
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(ship.x - 5, ship.y + 10)
    glVertex2f(ship.x, ship.y + 5)
    glVertex2f(ship.x + 5, ship.y + 10)
    glEnd()

    glPopMatrix()


def draw_asteroid(circle):
    glColor4f(0.5, 0.5, 0.5, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    for d in range(0, 360, 10):
        glVertex2f(circle.x + cos(radians(d)) * circle.r, circle.y + sin(radians(d)) * circle.r)
    glEnd()


def draw_goal(circle):
    glColor4f(0.5, 1.0, 0.5, 1.0)
    glBegin(GL_TRIANGLE_FAN)
    for d in range(0, 360, 10):
        glVertex2f(circle.x + cos(radians(d)) * circle.r, circle.y + sin(radians(d)) * circle.r)
    glEnd()
