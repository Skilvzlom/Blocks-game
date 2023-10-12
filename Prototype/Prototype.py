import pygame
import random

#Colors and other main settings
BLACK = (0,0,0)
BACKGROUND = (106, 148, 171)
RED = (159, 43, 104)
CYAN  = (105, 177, 165)
ORANGE = (255, 128, 0)
WHITE = (255, 255, 255)

CHOOSE_COLOR = (208, 220, 179)


WIDTH = 1280
HEIGHT = 720
FPS = 20

#Class for Blocks
class Blocks():
	Width = 98
	Height = 98
	def __init__(self ,posx, posy, color):
		self.posx = posx
		self.posy = posy
		self.color = color
		self.rect = pygame.Rect((self.posx * 100 + WIDTH /2 - 250, self.posy * 100 + HEIGHT /2 - 200, Blocks.Width, Blocks.Height))
	def getpose(self):
		return (self.posx, self.posy)

	def changeposx(self, x, self_block, chossing_block):
		if 0 <= self.posx + x < 5:
			self.rect.move_ip(x*100, 0)
			for i in range(25):
				if self.rect.contains(block[i].rect) and self_block != i:
					if block[i].color == WHITE:
						chossing_block += x
						block[i].rect.move_ip(x*(-100), 0)
						surf.fill(block[i].color)
						screen.blit(surf, block[i].rect)
						surf.fill(self.color)
						screen.blit(surf, self.rect)
						chossing_rect.move_ip(x*(100), 0)
						screen.blit(chossing_surf, chossing_rect)
						pygame.display.update(block[i].rect)
						pygame.display.update(self.rect)
						self.posx += x
						block[i].posx -= x
						break
			else:
				self.rect.move_ip(x*(-100), 0)	
		return chossing_block
		
	def changeposy(self, y, self_block, chossing_block):
		if 0 <= self.posy + y < 5:
			self.rect.move_ip(0, y*100)
			for i in range(25):
				if self.rect.contains(block[i].rect) and self_block != i:
					if block[i].color == WHITE:
						chossing_block += y*5
						block[i].rect.move_ip(0, y*(-100))
						surf.fill(block[i].color)
						screen.blit(surf, block[i].rect)
						surf.fill(self.color)
						screen.blit(surf, self.rect)
						chossing_rect.move_ip(0, y * (100))
						screen.blit(chossing_surf, chossing_rect)
						pygame.display.update(block[i].rect)
						pygame.display.update(self.rect)
						self.posy += y
						block[i].posy -= y
						break
			else:
				self.rect.move_ip(0, y*(-100))	
		return chossing_block


#----------Main------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND)
pygame.display.set_caption("Prot2")
clock = pygame.time.Clock()
#--------colors of blocks and other variables
block = []
chossing_block = 0
second_id_chossing_block = 0
moving_flag = False

First_column = False
Second_column = False
Third_column = False


colors_of_blocks = [RED,ORANGE,CYAN,RED,ORANGE,CYAN,RED,ORANGE,CYAN,RED,ORANGE,CYAN,RED,ORANGE,CYAN ]
black_blocks = [[BLACK, BLACK, BLACK, WHITE, WHITE], [BLACK, BLACK, BLACK, WHITE, WHITE]]
colors_of_end = [RED, ORANGE, CYAN]
random.shuffle(colors_of_blocks)
random.shuffle(colors_of_end)
random.shuffle(black_blocks[0])
random.shuffle(black_blocks[1])


#--------colors blocks for endend-------------
temp_rect = pygame.Rect(WIDTH / 2 - 250, 25, Blocks.Width, Blocks.Height)
temp_surf = pygame.Surface((Blocks.Width, Blocks.Height))
for i in range(3):
	temp_surf.fill(colors_of_end[i])
	screen.blit(temp_surf, temp_rect)
	temp_rect.move_ip(200, 0)
del temp_rect, temp_surf
end_rect = pygame.Rect(WIDTH / 2 - 250, HEIGHT / 2 - 200, Blocks.Width, Blocks.Height)


#---------chossing part-------------
chossing_rect = pygame.Rect(WIDTH / 2 - 250, HEIGHT / 2 - 200, Blocks.Width, Blocks.Height)
chossing_surf = pygame.Surface((Blocks.Width, Blocks.Height))
chossing_surf.fill(CHOOSE_COLOR)
chossing_surf.set_alpha(150)
clearing_surf = pygame.Surface((Blocks.Width, Blocks.Height))
# ---------Creating blocks-------------------


counter = 0
counter_unmoveable1 = 0
counter_unmoveable2 = 0
for j in range(5):
	for i in range(5):
		if i % 2 != 1:
			block.append(Blocks(i,j,colors_of_blocks[counter]))
			counter += 1
		elif i == 1:
			block.append(Blocks(i,j,black_blocks[0][counter_unmoveable1]))
			counter_unmoveable1 += 1
		elif i == 3:
			block.append(Blocks(i,j,black_blocks[1][counter_unmoveable2]))
			counter_unmoveable2 += 1
del counter
del counter_unmoveable1
del counter_unmoveable2
del black_blocks
del colors_of_blocks
surf = pygame.Surface((98, 98))

for i in range(25):
	surf.fill(block[i].color)
	screen.blit(surf, block[i].rect)
screen.blit(chossing_surf, chossing_rect)
#Main cycle
running = True
pygame.display.update()

while running:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			#chossing block part
			if event.key in (pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT) and moving_flag == False: 
				for i in range(25):
					if chossing_rect.contains(block[i].rect):
						clearing_surf.fill(block[i].color)
						screen.blit(clearing_surf, chossing_rect)
						break
				if event.key == pygame.K_DOWN:
					if chossing_block + 5 < 25:
						chossing_block += 5
						chossing_rect.move_ip(0, 100)
						screen.blit(chossing_surf, chossing_rect)
				elif event.key == pygame.K_UP:
					if chossing_block - 5 > -1:
						chossing_block -= 5
						chossing_rect.move_ip(0, -100)
						screen.blit(chossing_surf, chossing_rect)
				elif event.key == pygame.K_RIGHT:
					if chossing_block + 1 < 25:
						chossing_block += 1
						if chossing_block % 10 == 0 or chossing_block % 10 == 5:
							chossing_rect.move_ip(-400, 100)
							screen.blit(chossing_surf, chossing_rect)
						else:
							chossing_rect.move_ip(100, 0)
							screen.blit(chossing_surf, chossing_rect)
					else:
						chossing_block = 0
						chossing_rect.move_ip(-400, -400)
						screen.blit(chossing_surf, chossing_rect)
				
				elif event.key == pygame.K_LEFT:
					if chossing_block - 1 > -1:
						chossing_block -= 1
						if chossing_block % 10 == 4 or chossing_block % 10 == 9:
							chossing_rect.move_ip(400, -100)
							screen.blit(chossing_surf, chossing_rect)
						else:
							chossing_rect.move_ip(-100, 0)
							screen.blit(chossing_surf, chossing_rect)
					else:
						chossing_block = 24
						chossing_rect.move_ip(400, 400)
						screen.blit(chossing_surf, chossing_rect)
				for i in range(25):
					if chossing_rect.contains(block[i].rect):
						second_id_chossing_block = i
						break
			#moving block part
			elif event.key in (pygame.K_DOWN, pygame.K_UP, pygame.K_RIGHT, pygame.K_LEFT) and moving_flag == True:
				if event.key == pygame.K_DOWN:
					chossing_block = block[second_id_chossing_block].changeposy(1, second_id_chossing_block, chossing_block)
				elif event.key == pygame.K_UP:
					chossing_block = block[second_id_chossing_block].changeposy(-1, second_id_chossing_block, chossing_block)
				elif event.key == pygame.K_RIGHT:
					chossing_block = block[second_id_chossing_block].changeposx(1, second_id_chossing_block, chossing_block)
				elif event.key == pygame.K_LEFT:
					chossing_block = block[second_id_chossing_block].changeposx(-1, second_id_chossing_block, chossing_block)
				for _ in block:
					if _.posx == 0 and _.color == colors_of_end[0]:
						First_column = True
					elif _.posx == 0 and _.color != colors_of_end[0]:
						First_column = False
						break
					elif  _.posx == 2 and _.color == colors_of_end[1]:
						Second_column = True
					elif  _.posx == 2 and _.color != colors_of_end[1]:
						Second_column = False
						break
					elif  _.posx == 4 and _.color == colors_of_end[2]:
						Third_column = True
					elif _.posx == 4 and _.color != colors_of_end[2]:
						Third_column = False
						break
					

				if First_column and Second_column and Third_column:
					running = False
			elif event.key == pygame.K_SPACE:
				if block[second_id_chossing_block].color in (RED, CYAN, ORANGE) and moving_flag == False:
					moving_flag = True
				elif moving_flag == True:
					moving_flag = False

			pygame.display.update()

pygame.quit()
