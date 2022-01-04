import pygame
import random

'''
https://pythonprogramming.altervista.org
Github repository with the codel (001.py)
https://github.com/formazione/pygame_days

1 https://youtu.be/wAKLVFMb7eE Move Sprite
2 https://youtu.be/rsBJgWqsoa4 collisions
3 https://youtu.be/J3k4-tqy_kM Ai enemy 1
4 https://youtu.be/vwYu9Eel9QM frame rate
6 https://youtu.be/UaPjKtuQyfA Enemy AI 2
7 https://youtu.be/ZuEc6gncGNs Images, movements
8 https://youtu.be/wobJoDgI0LQ Bullet 1

https://youtu.be/wAKLVFMb7eE
https://youtu.be/rsBJgWqsoa4
https://youtu.be/J3k4-tqy_kM
https://youtu.be/vwYu9Eel9QM
https://youtu.be/UaPjKtuQyfA
https://youtu.be/ZuEc6gncGNs
https://youtu.be/wobJoDgI0LQ

'''

def show_fps():
	''' shows the frame rate on the screen '''
	fps_text = str(int(clock.get_fps())) # get the clocl'fps
	# render a text surface
	fps_text += f" {enemy.x=} {enemy.y=}"
	fps_surface = fps_font.render(fps_text, 1, pygame.Color("white"))
	# blit the text surface on the backgroud
	screen.blit(fps_surface, (0, 0))


class Screen:

	def check_collision():
		if player.rect.colliderect(enemy):
			enemy.respawn()


	def mainloop(loop):
		# when press left, right...
		if player.left == 1: # left
			player.x -= speed
		if player.right == 1: # right
			player.x += speed
		if player.up == 1: # up
			player.y -= speed
		if player.down == 1: # down
			player.y += speed

		# get user event (press key...)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = 0
			if event.type == pygame.KEYDOWN:

				# left = 0, right = 2, up = 1, down =3
				if event.key == pygame.K_LEFT:
					player.left = 1
				if event.key == pygame.K_RIGHT:
					player.right = 1
				if event.key == pygame.K_UP:
					player.up = 1
				if event.key == pygame.K_DOWN:
					player.down = 1

			# when you release the key player stops
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.left = 0
				if event.key == pygame.K_RIGHT:
					player.right = 0
				if event.key == pygame.K_UP:
					player.up = 0
				if event.key == pygame.K_DOWN:
					player.down = 0
		Screen.check_collision()
		screen.fill(0)
		show_fps()
		player.draw()
		enemy.draw()
		bullet.draw()
		enemy.move_ai()
		pygame.display.update()
		clock.tick(60)
		return loop

class Color:
	yellow = (0, 255, 0)
	red = (255, 0, 0)
	blue = (0, 0, 255)

class Sprite:

	def draw(self):
		self.rect[0] = self.x
		self.rect[1] = self.y
		screen.blit(self.image, (self.x,self.y))


class Player(Sprite):
	def __init__(self, x, y):
		self.left = 0
		self.right = 0
		self.up = 0
		self.down = 0
		self.x = x
		self.y = y
		self.image = pygame.image.load("img/player.png").convert()
		self.rect = self.image.get_rect()

class Bullet():
	def __init__(self):
		self.x = enemy.x
		self.y = enemy.y
		self.image = pygame.image.load("img/bullet.png").convert()
		self.rect = self.image.get_rect()

	def draw(self):
		if enemy.x < player.x:
			self.rect[0] = enemy.x + 50
		if enemy.x > player.x:
			self.rect[0] = enemy.x
		if abs(enemy.x - player.x) < 8:
			self.rect[0] = enemy.x + 24


		if enemy.y > player.y:
			self.rect[1] = enemy.y
		if enemy.y < player.y:
			self.rect[1] = enemy.y + 50
		if abs(enemy.y - player.y) < 8:
			self.rect[1] = enemy.y + 24
		screen.blit(self.image, self.rect)


class Enemy(Sprite):
	def __init__(self, x, y):
		# Position is the same as enemy's position
		self.x = x
		self.y = y
		self.image = pygame.image.load("img/enemy.png").convert()
		self.rect = self.image.get_rect()
		self.rect[0] = x
		self.rect[1] = y
		self.border = 0
		self.speed = 1 # day 9 (1)

	def move_ai(self):

		if self.border == 0: # day 9 (2)

			# ESCAPE HORIZONTALLY
			if self.x < 550  and self.x > 0:
				# it will escape from right if the player is more to left
				if player.x < self.x:
					self.x += self.speed # day 9 (3) 
				elif player.x > self.x:
					self.x -= self.speed # day 9 (3) 
				else:
					if random.random() > 0.5:
						self.x += self.speed # day 9 (3) 
					else:
						self.x -=self.speed # day 9 (3) 

			# ESCAPE VERTICALLY
			if self.y < 350 and self.y > 0:
				if player.y < self.y:
					self.y += self.speed # day 9 (3) 
				elif player.y > self.y:
					self.y -= self.speed # day 9 (3) 
				if random.random() > 0.5:
					self.y += self.speed # day 9 (3) 
				else:
					self.y -= self.speed # day 9 (3) 

		# day 9 (4) - new AI: when reaches border, changes behaviour

		if (-4 <= self.y <= 0) or \
			(-4 <= self.x <= 4) or \
			(350 <= self.y <= 355) or \
			(550 <= self.x <= 555):
			self.border = 1
			self.respawn()

		# === end day 9 - New AI

	def show_text(self):
		''' shows informations about enemy '''
		fps_text = f" {enemy.x=} {enemy.y=} {enemy.border=}"
		fps_surface = fps_font.render(fps_text, 1, pygame.Color("white"))
		# blit the text surface on the backgroud
		screen.blit(fps_surface, (300, 0))

	def respawn(self):
		self.x = random.randrange(0, 580)
		self.y = random.randrange(0, 380)
		self.border = 0

	def draw(self):
		self.rect[0] = self.x
		self.rect[1] = self.y
		self.show_text()
		screen.blit(self.image, (self.x,self.y))

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
# white surface on which we show the frame rate
fps_font = pygame.font.SysFont("Arial", 20) # a font for the fps
speed = 3




# =========== MAIN LOOP ==========
player = Player(0,0)
enemy = Enemy(100,100)
bullet = Bullet()
loop = 1
while loop:
	loop = Screen.mainloop(loop) # all the actions


pygame.quit()