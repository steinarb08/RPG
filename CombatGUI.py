import pygame
import os
import CombatTeam
import Creature
import Combat
import sys
import AbilityTargeting
import AbilityExecute
import CombatAI
from pygame.locals import *
class CombatGUI:


	def __init__(self, playerTeam, enemyTeam):
		self._combat = Combat.Combat(playerTeam,enemyTeam)
		self._targetSys = 0
		self._playerSprite = []
		self._enemySprite = []
		self.black = (0, 0, 0)

	def drawinitbox(self,surf):
		pygame.draw.line(surf, self.black, (10,10), (790,10), 5)
		pygame.draw.line(surf, self.black, (10,8), (10,62), 5)
		pygame.draw.line(surf, self.black, (10,60), (790,60), 5)
		pygame.draw.line(surf, self.black, (790,8), (790,62), 5)

	def drawcharbox(self,surf):
		pygame.draw.line(surf, self.black, (10,70), (790,70), 5)
		pygame.draw.line(surf, self.black, (10,68), (10,402), 5)
		pygame.draw.line(surf, self.black, (10,400), (790,400), 5)
		pygame.draw.line(surf, self.black, (790,68), (790,402), 5)

	def drawcharoptbox(self,surf):
		pygame.draw.line(surf, self.black, (10,410), (500,410), 5)
		pygame.draw.line(surf, self.black, (10,408), (10,582), 5)
		pygame.draw.line(surf, self.black, (10,580), (500,580), 5)
		pygame.draw.line(surf, self.black, (500,408), (500,582), 5)

	def drawcharinfobox(self,surf):
		pygame.draw.line(surf, self.black, (510,410), (790,410), 5)
		pygame.draw.line(surf, self.black, (510,408), (510,582), 5)
		pygame.draw.line(surf, self.black, (510,580), (790,580), 5)
		pygame.draw.line(surf, self.black, (790,408), (790,582), 5)

	def spritelisting(self):
		self._playerSprite = pygame.sprite.RenderPlain(self._combat.GetPlayerTeam().GetAliveMembers())
		self._enemySprite = pygame.sprite.RenderPlain(self._combat.GetEnemyTeam().GetAliveMembers())

	def main(self):

		pygame.init()
		screensize = (800,600)
		screen = pygame.display.set_mode(screensize)
		pygame.display.set_caption('Combat GUI')

		background = pygame.Surface(screen.get_size())
		background = background.convert()
		background.fill((250, 250, 250))

		self.spritelisting()


		while 1:

			for event in pygame.event.get():
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					return



			screen.blit(background, (0,0))
			self.drawinitbox(screen)
			self.drawcharbox(screen)
			self.drawcharoptbox(screen)
			self.drawcharinfobox(screen)
			pygame.display.flip()
