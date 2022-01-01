import pygame
import random


def show_fps():
	''' shows the frame rate on the screen '''
	fps_text = str(int(clock.get_fps())) # get the clocl'fps
	# render a text surface
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
		# self.rect[0] = x
		# self.rect[1] = y

	def draw(self):
		self.rect[0] = self.x
		self.rect[1] = self.y
		screen.blit(self.image, (self.x,self.y))



class Enemy(Sprite):
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.image = pygame.image.load("img/enemy.png").convert()
		self.rect = self.image.get_rect()
		self.rect[0] = x
		self.rect[1] = y

	def move_ai(self):

		# ESCAPE TO THE RIGHT ===========================
		if self.x < 580  and self.x > 0:
			# it will escape from right if the player is more to left
			if player.x < self.x:
				self.x += 3
			elif player.x > self.x:
				self.x -= 3
			else:
				if random.random() > 0.5:
					self.x += 3
				else:
					self.x -=3

		if self.y < 380 and self.y > 0:
			if player.y < self.y:
				self.y += 3
			elif player.y > self.y:
				self.y -= 3
			if random.random() > 0.5:
				self.y += 3
			else:
				self.y -= 3

	def respawn(self):
		self.x = random.randrange(0, 580)
		self.y = random.randrange(0, 380)


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
# white surface on which we show the frame rate
fps_font = pygame.font.SysFont("Arial", 20) # a font for the fps
speed = 3




# =========== MAIN LOOP ==========
player = Player(0,0)
enemy = Enemy(100,100, Color.red)
loop = 1
while loop:
	loop = Screen.mainloop(loop) # all the actions


pygame.quit()