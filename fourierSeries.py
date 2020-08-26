import pygame
from pygame import *
import math
from pygame import gfxdraw
import random

n=5#this is the ammount of vectors to calculator to.
#The x axis is a representation of a sin function and since you can add vectors like thos,
#this whole project is about interpretting the infinite series of sine functions that can generate a sqauare wave known as a fourier series


arrowAngle = 35
arrowLength = 50

pygame.init()

xSize=1920
ySize=1080


win = pygame.display.set_mode((xSize, ySize), pygame.FULLSCREEN)
pygame.display.set_caption("Fourier Series")


class VectorArrow():
	x = xSize/2
	y = ySize/2
	angle = 0
	length = 100
	rotation = math.pi/2

	def getX(self):
		return math.cos(self.angle)*self.length + xSize/2 + (self.x - xSize/2)
	def getY(self):
		return math.sin(self.angle)*self.length + ySize/2 + (self.y-ySize/2)

	def drawMe(self):
		pygame.draw.line(win, (0,0,0),[self.x, self.y],[self.getX(), self.getY()], 3)
		try:
			pygame.draw.circle(win, (8, 200, 154), [int(self.x), int(self.y)], int(self.length), 1)
		except:
			pass





		

	#def rotateOnce(self, SCW): #(sprite coliding with)

run = True
win.fill((255,255,255))   

vectors = []
for i in range(0, n):#append each arrow sprite with the right stats
	temp = VectorArrow()
		#the first one needs to have 


	temp.length = (1/(((2*i)+1)))*150
	temp.rotation = ((2*i)+1) * math.pi /1.5


	vectors.append(temp)


#for i in vectors:
#	print(str(i.rotation) + " " + str(i.length))

simSpeed = 20
keepers = []


while run:
	win.fill((255,255,255))
	

	

	#pygame.time.delay(simSpeed) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

	for i in range(len(keepers)):
		if (i != 0): 
			pygame.draw.line(win, (0, 0, 255), [keepers[i][0], keepers[i][1]], [keepers[i-1][0], keepers[i-1][1]], 3)


			


	pygame.draw.circle(win, (255, 0, 0), (int(vectors[-1].getX()), int(vectors[-1].getY())), 6)
	for i in range(len(vectors)):


		if (n>4):
			temp = 40
		else:
			temp = 10
		vectors[i].angle += vectors[i].rotation / simSpeed / temp
		if (n>4):
			temp = 50



		#roots it at the end of the previous vector

		if (i != 0):
			vectors[i].x = vectors[i-1].getX() 
			vectors[i].y = vectors[i-1].getY()

		vectors[i].drawMe()




	for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
		if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
			run = False  # Ends the game loop

	keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.



	keepers.append((int(vectors[-1].getX()), int(vectors[-1].getY())))
	

	
	pygame.display.update()
pygame.quit()

