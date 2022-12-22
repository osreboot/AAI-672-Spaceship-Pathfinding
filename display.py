from time import time_ns

from OpenGL.GL import *
from OpenGL.GLUT import *


class Display:

    def __init__(self, updateRef, deltaMin, size, title):
        self.updateRef = updateRef
        self.deltaMin = deltaMin

        # Initialize the window with GLUT
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
        glutInitWindowSize(size[0], size[1])
        glutCreateWindow(bytes(title, "ascii"))
        glutDisplayFunc(self.__update)
        glutIdleFunc(self.__update)

        # Initialize render settings
        glClearColor(0.0, 0.0, 0.0, 1.0)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, size[0], size[1], 0, 1, -1)
        glMatrixMode(GL_MODELVIEW)

        # Start the main program
        self.timeLastUpdate = time_ns()
        glutMainLoop()

    def __update(self):
        # Calculate time since update was last called (in seconds)
        delta = 0.0
        while delta < self.deltaMin:
            delta = float(time_ns() - self.timeLastUpdate) / 1000000000.0
        self.timeLastUpdate = time_ns()

        # Prepare for rendering
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # Run the main program update function
        self.updateRef(delta)

        # Display the rendered scene
        glutSwapBuffers()
