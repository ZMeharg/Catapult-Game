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
Class pymunk.Circle(None, 5, offset=())

# class Catapult():
#     def __init__(self,v0,angle,y0,g = -9.8):
#         self.y0 = y0
#         self.dx = 0
#         self.dy = y0
#         self.v0x = math.cos(angle/57.2958)*v0
#         self.v0y = math.sin(angle/57.2958)*v0
#         self.time = 0
#         self.g = g
#         self.frame = 0
#         self.xrange = get_xrange(y0,v0,angle/57.2958)
#         self.yrange = -self.v0y*self.v0y/g/2 + y0
#         self.radius = 5
#         self.trajectory = []

#     def update(self):
#         if self.dy >= 0:
#             self.dx = self.time * self.v0x
#             self.dy = self.time*self.time*self.g/2 + self.time*self.v0y + self.y0
#             self.trajectory.append((int(self.dx*360/self.xrange)+50,430-int(self.dy*280/self.yrange)))

#             self.frame += 1
#             self.time += 1/120
#             if self.frame == 120:
#                 self.frame = 0

#     def draw(self):
#         pygame.draw.rect(screen,WHITE,(375, 170, 200, 85))
#         timelabel = font.render("time = " + shorten_float(self.time) + "s", 1, BLACK)
#         xrlabel = font.render("x-range = " + shorten_float(self.xrange) + "m", 1, BLACK)
#         yrlabel = font.render("y-range = " + shorten_float(self.yrange) + "m", 1, BLACK)
#         screen.blit(timelabel, (380, 173))
#         screen.blit(xrlabel, (380, 203))
#         screen.blit(yrlabel, (380, 233))
#         for i in self.trajectory:
#             pygame.draw.circle(screen,LIGHTBLUE,i,1)
#         pygame.draw.circle(screen,LIGHTBLUE,(int(self.dx*360/self.xrange)+47,427-int(self.dy*280/self.yrange)),self.radius)





# class Catapult():
#     """docstring for Catapult"""
#     def __init__(self, forearm_length, item, cataheight, angle):
#         self.forearm_length = forearm_length
#         self.materials = materials
#         self.cataheight = cataheight
#         self.angle = angle
# # Creating the catapult
# class Item():
#     def __init__(self, weight, image):
#         self.name = name
#         self.weight = weight
#         self.image = image

# # List of items getting thrown
# boulder = Item("Boulder")
# bag_of_feathers = Item("Feathers")
# pig = Item("Pig")
# barrel = Item("Barrel")

# # List of the items' weights
# boulder.weight = 200
# bag_of_feathers.weight = 10
# pig.weight = 500
# barrel.weight = 100

# # Giving the items their images
# boulder.image = pygame.image.load('Virus.jpg')


# def physics_stuff():
#     # First we need to figure out the time that the object is in the air for
#     # To find this time we need to use the quadratic equation from the equation y = v(y)t - 1/2 gt^2
#     a = y0
#     b = v0
#     c = .5 * g
#     t1 = (-b + ((b ** 2) - 4 * a *c) ** .5) / 2 * a
#     t2 = (-b - ((b ** 2) - 4 * a *c) ** .5) / 2 * a

#     # Now we need to check to see if the time are even real, one of which should be negative so we have to find the positive one
#     if t1 > 0 and t2 < 0:
#         t1 = t
#     if t2 > 0 and t1 < 0:
#         t2 = t
#     else:
#         print("Error")
#     # Once we have the time we are looking for we can determine how far the object will travel
#     # x = v(x) * t
#     xfinal = vx * t

def draw_background():
    pygame.draw.rect(screen, (0, 102, 0), pygame.Rect(0, 600, 1000, 800))
    pygame.draw.rect(screen, (132, 112, 255), pygame.Rect(0, 0, 1000, 600))
    pygame.draw.circle(screen, (255, 255, 0), (0, 0), 150)

# Insert formula to create the target we are trying to hit
# class target():
#     def __init__(self, location):
#         self.location = location
    # Add a function to randomize the target with in a certain range

# Insert formula to test and see if we hit the target
# def Congragulations():

# Insert formula to customize the catapult; lenght of forearm, weight of object, height of catapult

# Insert formula to draw the changing of the catapult dimesions, and weight of object

# Insert formula to figure out the keys/mouse click to try get the catapult to move




# draw_background()
main()
# draw_catapult()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
