"""Catapult Game."""
import pygame
import pymunk
import pymunk.pygame_util


height = 800
width = 1000

screen = pygame.display.set_mode((width, height))

# Find a way to get pymunk gravity to work

pygame.init()
# Drawing the image that the game will play in
done = False

# Insert a formula for drawing the catapult; base, fulcrum, item thrown, and forearm

class Catapult():
    """docstring for Catapult"""
    def __init__(self, x, y, forearm_length, item, cataheight, angle):
        self.x = x
        self.y = y
        self.forearm_length = forearm_length
        self.item = item
        self.cataheight = cataheight
        self.angle = angle

class Item():
    def __init__(self, air_resist, weight):
        self.air_resist = air_resist
        self.weight = weight


def physics_stuff():
    # First we need to figure out the time that the object is in the air for
    # To find this time we need to use the quadratic equation from the equation y = v(y)t - 1/2 gt^2
    a = y0
    b = v0
    c = .5 * g
    t1 = (-b + ((b ** 2) - 4 * a *c) ** .5) / 2 * a
    t2 = (-b - ((b ** 2) - 4 * a *c) ** .5) / 2 * a

    # Now we need to check to see if the time are even real, one of which should be negative so we have to find the positive one
    if t1 > 0 and t2 < 0:
        t1 = t
    if t2 > 0 and t1 < 0:
        t2 = t
    else:
        print("Error")
    # Once we have the time we are looking for we can determine how far the object will travel
    # x = v(x) * t
    xfinal = vx * t

# def draw_background():
    pygame.draw.rect(screen, (0, 102, 0), pygame.Rect(0, 600, 1000, 800))
    pygame.draw.rect(screen, (132, 112, 255), pygame.Rect(0, 0, 1000, 600))
    pygame.draw.circle(screen, (255, 255, 0), (0, 0), 150)

# Insert formula to create the target we are trying to hit

# Insert formula to test and see if we hit the target

# Insert formula to customize the catapult; lenght of forearm, weight of object, height of catapult

# Insert formula to draw the changing of the catapult dimesions, and weight of object

# Insert formula to figure out the keys/mouse click to try get the catapult to move




# draw_background()
# draw_catapult()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
