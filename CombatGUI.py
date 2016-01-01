import pygame
import os
from pygame.locals import *


black = (0, 0, 0)

def drawinitbox(surf):
	pygame.draw.line(surf, black, (10,10), (790,10), 5)
	pygame.draw.line(surf, black, (10,8), (10,62), 5)
	pygame.draw.line(surf, black, (10,60), (790,60), 5)
	pygame.draw.line(surf, black, (790,8), (790,62), 5)

def drawcharbox(surf):
	pygame.draw.line(surf, black, (10,70), (790,70), 5)
	pygame.draw.line(surf, black, (10,68), (10,402), 5)
	pygame.draw.line(surf, black, (10,400), (790,400), 5)
	pygame.draw.line(surf, black, (790,68), (790,402), 5)

def drawcharoptbox(surf):
	pygame.draw.line(surf, black, (10,410), (500,410), 5)
	pygame.draw.line(surf, black, (10,408), (10,582), 5)
	pygame.draw.line(surf, black, (10,580), (500,580), 5)
	pygame.draw.line(surf, black, (500,408), (500,582), 5)

def drawcharinfobox(surf):
	pygame.draw.line(surf, black, (510,410), (790,410), 5)
	pygame.draw.line(surf, black, (510,408), (510,582), 5)
	pygame.draw.line(surf, black, (510,580), (790,580), 5)
	pygame.draw.line(surf, black, (790,408), (790,582), 5)


def main():

	pygame.init()
	screensize = (800,600)
	screen = pygame.display.set_mode(screensize)
	pygame.display.set_caption('Combat GUI')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))


	while 1:

		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN and event.key == K_ESCAPE:
				return


		screen.blit(background, (0,0))
		drawinitbox(screen)
		drawcharbox(screen)
		drawcharoptbox(screen)
		drawcharinfobox(screen)
		pygame.display.flip()

main()