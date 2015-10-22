from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fn_easyDraw = 0
easyGL_width = 800
easyGL_height = 600

def easyDraw():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
	glLoadIdentity()                                   # reset position
	refresh2d(easyGL_width, easyGL_height)                           # set mode to 2d
	
	if fn_easyDraw:
		fn_easyDraw()

	glutSwapBuffers()                                  # important for double buffering

def run(width, height, title, fn_draw):
	global fn_easyDraw, easyGL_height, easyGL_width
	fn_easyDraw = fn_draw
	easyGL_height = height
	easyGL_width  = width

	glutInit()                                             # initialize glut
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
	glutInitWindowSize(width, height)                      # set window size
	glutInitWindowPosition(0, 0)                           # set window position

	window = glutCreateWindow(title)              		   # create window with title
	glutDisplayFunc(easyDraw)                               # set draw function callback
	glutIdleFunc(easyDraw)                                  # draw all the time

	glutMainLoop()                                         # start everything

def setColor(R, G, B):
	    glColor3f(R, G, B)                           # set color

def setColorA(R, G, B, A):
		glEnable(GL_BLEND);
		glColor4f(R, G, B, A)

def drawRect(x, y, width, height):
    glBegin(GL_QUADS)                                  # start drawing a rectangle

    glVertex2f(x, y)                                   # bottom left point
    glVertex2f(x + width, y)                           # bottom right point
    glVertex2f(x + width, y + height)                  # top right point
    glVertex2f(x, y + height)                          # top left point

    glEnd() 
    glDisable(GL_BLEND) 
   
def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
    glDisable(GL_DEPTH_TEST);
    glClearColor(0, 0, 0, 0);
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
   
