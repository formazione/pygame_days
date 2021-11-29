import pygame


pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

speed = 5
class Screen:
	def mainloop(loop):
		# when press left, right...
		if player.left:
			player.x -= speed
		elif player.right:
			player.x += speed
		elif player.up:
			player.y -= speed
		elif player.down:
			player.y += speed

		# get user event (press key...)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				loop = 0
			elif event.type == pygame.KEYDOWN:

				# when you press left, right...
				if event.key == pygame.K_LEFT:
					player.left = 1
					player.right = 0
					player.up = 0
					player.down = 0
					print("press left")
				elif event.key == pygame.K_RIGHT:
					player.left = 0
					player.right = 1
					player.up = 0
					player.down = 0
					print("press right")
				elif event.key == pygame.K_UP:
					player.down = 0
					player.up = 1
					player.left = 0
					player.right = 0
					print("press right")
				elif event.key == pygame.K_DOWN:
					player.up = 0
					player.down = 1
					player.left = 0
					player.right = 0

					print("press right")
			# when you release the key player stops
			elif event.type == pygame.KEYUP:
				player.left = 0
				player.right = 0
				player.up = 0
				player.down = 0
		pygame.display.update()
		clock.tick(60)
		return loop

class Sprite:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.create_sprite()
		self.left = 0
		self.right = 0
		self.up = 0
		self.down = 0

	def create_sprite(self):
		self.image = pygame.Surface((50, 50))
		self.image.fill((255,0,0))

	def draw(self):
		screen.blit(self.image, (self.x,self.y))







# =========== MAIN LOOP ==========
player = Sprite(0,0)
loop = 1
while loop:
	loop = Screen.mainloop(loop)
	screen.fill(0)
	player.draw()


pygame.quit()