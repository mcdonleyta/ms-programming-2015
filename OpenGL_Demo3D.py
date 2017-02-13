from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0                                             # glut window number
width, height = 500, 400                               # window size


def switch3D():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0,float(width)/float(height),1,1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()                                   # reset position

    glEnable(GL_DEPTH_TEST)                            
    #glEnable(GL_LIGHTING)

def switch2D():
    global width, height
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -10, 10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()                                   # reset position

    glDisable(GL_DEPTH_TEST)                            #Disable so alpha blending works
    glDisable(GL_LIGHTING)



def drawColor(r, g, b):
    drawColorA(r,g,b,1)

def drawColorA(r, g, b, a):
    glColor4f(r,g,b,a)
    
def drawRect(x, y, w, h):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x+w, y)
    glVertex2f(x+w, y+h)
    glVertex2f(x, y+h)
    glEnd()
    

def resize(w, h):
    global width, height
    
    glViewport(0, 0, w, h) 
    width = w
    height = h

xrot = 0    
def draw():                                            # ondraw is called all the time
    global xrot
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen

    #draw 2D stuff
    switch2D()
    glColor4f(0.0, 1.0, 0.0, 0.5)
    drawRect(0,0,50,50)
    glColor4f(1.0, 0.0, 0.0, 0.5)
    drawRect(25,25,50,50)
   
    #draw 3D stuff
    switch3D()
    gluLookAt (0, 5, 0, 0, 0, 0, 0.0, 0.0, 1.0)
    glRotate(xrot, 1, 1, 0)
    xrot = xrot + 0.05
   # glutSolidSphere(10,10,50)
    x=0
    y=0
    z=0
    w=1
    h=1
    d=1  
    glBegin(GL_QUADS)
    drawColorA(1, 0, 0, 1)
    glVertex3f(x, y, z)         #Front face
    drawColorA(0, 1, 0, 1)
    glVertex3f(x, y-h, z)
    drawColorA(0, 0, 1, 1)
    glVertex3f(x+w, y-h, z)
    drawColorA(1, 0, 1, 1)
    glVertex3f(x+w, y, z)
                
    drawColorA(0, 1, 0, 1)
    glVertex3f(x, y, z+d)       #Back face
    glVertex3f(x, y-h, z+d)
    glVertex3f(x+w, y-h, z+d)
    glVertex3f(x+w, y, z+d)

    drawColorA(0, 0, 1, 1)
    glVertex3f(x, y, z)         #Left face
    glVertex3f(x, y-h, z)
    glVertex3f(x, y-h, z+d)
    glVertex3f(x, y, z+d)

    drawColorA(1, 1, 0, 1)
    glVertex3f(x+w, y, z)       #Right face
    glVertex3f(x+w, y-h, z)
    glVertex3f(x+w, y-h, z+d)
    glVertex3f(x+w, y, z+d)

    drawColorA(0, 1, 1, 1)
    glVertex3f(x, y, z)         #Top face
    glVertex3f(x, y, z+d)
    glVertex3f(x+w, y, z+d)
    glVertex3f(x+w, y, z)

    drawColorA(1, 0, 1, 1)
    glVertex3f(x, y-h, z)         #Bottom face
    glVertex3f(x, y-h, z+d)
    glVertex3f(x+w, y-h, z+d)
    glVertex3f(x+w, y-h, z)

    glEnd()
    
    glutSwapBuffers()                                  # important for double buffering
    

# initialization

glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(100, 100)                           # set window position
window = glutCreateWindow(b'VA Engine')              # create window with title


glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)       #Enable 2D Alpha blending
glEnable(GL_BLEND)

glShadeModel(GL_SMOOTH)

glColorMaterial(GL_FRONT, GL_DIFFUSE)                   #Mix surface color with light
glEnable(GL_COLOR_MATERIAL)

glEnable(GL_DEPTH_TEST)
glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
glEnable(GL_MULTISAMPLE)                                # Enable AA
glEnable(GL_NORMALIZE)                                  # Normalize Normal's to length 1

glutReshapeFunc(resize)
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everything
