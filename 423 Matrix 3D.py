import pygame
import random
import numpy as np
import math
import sys
import time

SCALE = 100

BLACK = (0,0,0)
GRAY = (128,128,128)
WHITE = (255,255,255)

RED = (191,64,64)
GREEN = (64,191,64)
BLUE = (64,64,191)

YELLOW = (191,191,64)
CYAN = (64,191,191)
PURPLE = (191,64,191)

WIDTH = 800
HEIGHT = 600

SIZE = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

CAMERA = [0, 0, 0, 0, 60, 0]

class Shape:

    def __init__(self, c, *ver):

        self.vertex = ver
        self.c = c

        self.x = np.array([])
        self.y = np.array([])
        self.z = np.array([])

        for v in self.vertex:
            self.x = np.concatenate((self.x, np.array([v[0] * SCALE])))
            self.y = np.concatenate((self.y, np.array([v[1] * SCALE])))
            self.z = np.concatenate((self.z, np.array([v[2] * SCALE])))

    def colour(self, c):
        self.c = c

    def draw(self, outline = 0):

        lst = []

        for i in range(len(self.vertex)):
            lst.append((self.x[i] + WIDTH // 2, -self.y[i] + HEIGHT // 2))

        pygame.draw.polygon(SCREEN, self.c, lst, outline)

    def draw_vertices(self, r = 5, cv = None):

        if cv == None:
            cv = self.c

        for i in range(len(self.vertex)):
            pygame.draw.circle(SCREEN, cv, (self.x[i] + WIDTH // 2, -self.y[i] + HEIGHT // 2), r)
            print(i)

    def rotate(self, theta, axis = "z"):

        theta = theta * (math.pi / 180)

        if axis.lower() == "x":
            self.matrix(1, 0, 0, 0, math.cos(theta), -math.sin(theta), 0, math.sin(theta), math.cos(theta))

        elif axis.lower() == "y":
            self.matrix(math.cos(theta), 0, math.sin(theta), 0, 1, 0, -math.sin(theta), 0, math.cos(theta))

        elif axis.lower() == "z":
            self.matrix(math.cos(theta), -math.sin(theta), 0, math.sin(theta), math.cos(theta), 0, 0, 0, 1)

    def translate(self, dx, dy, dz):
        self.x += dx * SCALE
        self.y += dy * SCALE
        self.z += dz * SCALE

    def enlarge(self, s):
        self.x *= s
        self.y *= s
        self.z *= s

    def matrix(self, x1, y1, z1, x2, y2, z2, x3, y3, z3):
        new_x = (x1 * self.x) + (y1 * self.y) + (z1 * self.z)
        new_y = (x2 * self.x) + (y2 * self.y) + (z2 * self.z)
        new_z = (x3 * self.x) + (y3 * self.y) + (z3 * self.z)

        self.x = new_x
        self.y = new_y
        self.z = new_z


def draw_grid():

    pygame.draw.line(SCREEN, BLACK, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT), width = 3)
    pygame.draw.line(SCREEN, BLACK, (0, HEIGHT / 2), (WIDTH, HEIGHT / 2), width = 3)

    for axis_var in range(1, WIDTH // (SCALE * 2)):

        pygame.draw.line(SCREEN, BLACK, (WIDTH / 2 + SCALE * axis_var, 0), (WIDTH / 2 + SCALE * axis_var, HEIGHT))
        pygame.draw.line(SCREEN, BLACK, (WIDTH / 2 - SCALE * axis_var, 0), (WIDTH / 2 - SCALE * axis_var, HEIGHT))

    for axis_var in range(1, HEIGHT // (SCALE * 2)):

        pygame.draw.line(SCREEN, BLACK, (0, HEIGHT / 2 + SCALE * axis_var), (WIDTH, HEIGHT / 2 + SCALE * axis_var))
        pygame.draw.line(SCREEN, BLACK, (0, HEIGHT / 2 - SCALE * axis_var), (WIDTH, HEIGHT / 2 - SCALE * axis_var))


def draw_grid_3D():

    for axis_var in range(-WIDTH // (SCALE), WIDTH // (SCALE)):

        L = Shape(GRAY, (-WIDTH // (SCALE), axis_var, 0), (WIDTH // (SCALE), axis_var, 0))

        L.rotate(-CAMERA[3], "x")
        L.rotate(-CAMERA[4], "y")
        L.rotate(-CAMERA[5], "z")
        L.draw(1)

    for axis_var in range(-HEIGHT // (SCALE), HEIGHT // (SCALE)):

        L = Shape(GRAY, (axis_var, -HEIGHT // (SCALE), 0), (axis_var, HEIGHT // (SCALE), 0))

        L.rotate(-CAMERA[3], "x")
        L.rotate(-CAMERA[4], "y")
        L.rotate(-CAMERA[5], "z")
        L.draw(1)

    x_axis = Shape(RED, (0, 0, 0), (WIDTH // (SCALE * 2), 0, 0))
    y_axis = Shape(GREEN, (0, 0, 0), (0, HEIGHT // (SCALE * 2), 0))
    z_axis = Shape(BLUE, (0, 0, 0), (0, 0, HEIGHT // (SCALE * 2)))

    axis = [x_axis, y_axis, z_axis]

    for a in axis:
        a.rotate(-CAMERA[3], "x")
        a.rotate(-CAMERA[4], "y")
        a.rotate(-CAMERA[5], "z")
        a.draw(2)



rot_x = 0
rot_y = 0
rot_z = 0

while True:
    prev_time = time.time()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill(WHITE)


    if True:

        #cubeFront = Shape(GREEN, (2, 1, 1), (2, -1, 1), (-2, -1, 1), (-2, 1, 1))
        #cubeRear = Shape(GREEN, (2, 1, -1), (2, -1, -1), (-2, -1, -1), (-2, 1, -1))
        #cubeRight = Shape(GREEN, (2, 1, 1), (2, 1, -1), (2, -1, -1), (2, -1, 1))
        #cubeLeft = Shape(GREEN, (-2, 1, 1), (-2, 1, -1), (-2, -1, -1), (-2, -1, 1))
        #cubeTop = Shape(GREEN, (2, 1, 1), (2, 1, -1), (-2, 1, -1), (-2, 1, 1))
        #cubeBottom = Shape(GREEN, (2, -1, 1), (2, -1, -1), (-2, -1, -1), (-2, -1, 1))
        
        cubeFront = Shape(GREEN, (1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1))
        cubeRear = Shape(GREEN, (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1))
        cubeRight = Shape(GREEN, (1, 1, 1), (1, 1, -1), (1, -1, -1), (1, -1, 1))
        cubeLeft = Shape(GREEN, (-1, 1, 1), (-1, 1, -1), (-1, -1, -1), (-1, -1, 1))
        cubeTop = Shape(GREEN, (1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, 1, 1))
        cubeBottom = Shape(GREEN, (1, -1, 1), (1, -1, -1), (-1, -1, -1), (-1, -1, 1))

        env = [cubeFront, cubeRear, cubeRight, cubeLeft, cubeTop, cubeBottom]

        
        for c in env:

            c.rotate(-CAMERA[3], "x")
            c.rotate(-CAMERA[4], "y")
            c.rotate(-CAMERA[5], "z")

            c.draw(5)

        rot_x += 1.3
        rot_y += 0.7
        rot_z += 1.2
        

        CAMERA = [0,0,0, rot_x, rot_y, rot_z]
        

    if False:

        square = Shape(GREEN, (2, 1, 1), (2, -1, 1), (-2, -1, 1), (-2, -1, 1))
        square.draw(5)
        square.translate(2, 2, 0)
        square.draw(5)
        square.rotate(90, "y")
        square.draw(5)


    if False:
        triangle = Shape(GREEN, (0, 0, 1), (0, 2, 1), (1, 0, 1))
        triangle.draw()

        triangle.translate(2,2,1)
        triangle.colour(BLUE)
        triangle.draw()

        triangle.rotate(90)
        triangle.colour(RED)
        triangle.draw()

    #draw_grid_3D()
    pygame.display.update()

    print(f"FPS: {1 / (time.time() - prev_time)}")
