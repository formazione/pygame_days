import pygame


class Screen:

	def check_collision():
		if player.rect.colliderect(player2):
			print("\nCollision detected")
			player2.change_color(Color.blue)
		if not player.rect.colliderect(player2):
			print("\n No Collision detected")
			player2.change_color(Color.red)
		else:
			print("-----------------")

	def mainloop(loop):
		# when press left, right...
		if player.direction == 0: # left
			player.x -= speed
		elif player.direction == 2: # right
			player.x += speed
		elif player.direction == 1: # up
			player.y -= speed
		elif player.direction == 3: # down
			player.y += speed

		# get user event (press key...)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = 0
			elif event.type == pygame.KEYDOWN:

				# when you press left, right...
				'''	
                            u 1

				       l 0        2 r
                            
                            d 3

				'''
				if event.key == pygame.K_LEFT: # left = 0, right = 2, up = 1, down =3
					player.direction = 0
				elif event.key == pygame.K_RIGHT:
					player.direction = 2
				elif event.key == pygame.K_UP:
					player.direction = 1
				elif event.key == pygame.K_DOWN:
					player.direction = 3

			# when you release the key player stops
			elif event.type == pygame.KEYUP:
				print("\nYou stopped at")
				print(f"{player.rect=}")
				print(f"{player2.rect=}")
				player.direction = -1
		Screen.check_collision()
		pygame.display.update()
		clock.tick(60)
		return loop

class Color:
	yellow = (0, 255, 0)
	red = (255, 0, 0)
	blue = (0, 0, 255)

class Sprite:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.direction = -1
		self.image = pygame.Surface((50, 50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect[0] = x
		self.rect[1] = y
		print(self.rect)

	def change_color(self, color):
		self.image.fill(color)

	def draw(self):
		self.rect[0] = self.x
		self.rect[1] = self.y
		screen.blit(self.image, (self.x,self.y))


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

speed = 5




# =========== MAIN LOOP ==========
player = Sprite(0,0, Color.yellow)
player2 = Sprite(100,100, Color.red)
loop = 1
while loop:
	loop = Screen.mainloop(loop)
	screen.fill(0)
	player.draw()
	player2.draw()


pygame.quit()