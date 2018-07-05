#encoding=utf-8

import pygame

import time

import random

'''
1.搭建界面
2.添加玩家飞机
'''
class Base(object):
	def __init__(self, screen):
		self.screen = screen 

class Plane(Base):
	def __init__(self, screen):
		super().__init__(screen)
		self.image = pygame.image.load(self.imageName).convert()
		self.bullets = []
		self.bullet = None
		
	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
		
		#
		for i in self.bullets:
			if i.y >890 or i.y <0 :
				self.bullets.remove(i)

		for bullet in self.bullets:
			bullet.display()



#玩家飞机
class HeroPlane(Plane):

	def __init__(self, screen):
		#position
		self.x = 230
		self.y = 600
		#
		self.imageName = "./feiji/hero.gif"
		super().__init__(screen)

	def move(self, KEYDOWN):
		if KEYDOWN == "K_LEFT":
			self.x -= 5
		elif KEYDOWN == "K_RIGHT":
			self.x += 5
		elif KEYDOWN == "K_SPACE":
			self.bullet = Bullet(self.x+40, self.y-20, self.screen, "hero")
			self.bullets.append(self.bullet)

class EnemyPlane(Plane):
	
	def __init__(self,screen):
		self.x = 0  
		self.y = 0
		self.direction = 'right'
		self.imageName = "./feiji/enemy-1.gif"
		super().__init__(screen)

	
	def move(self):

		if random.randint(0,80) in [1]:
			self.bullet = Bullet(self.x+20, self.y+15, self.screen, "enemy")
			self.bullets.append(self.bullet)

		if self.direction == 'right':
			self.x += 2
		elif self.direction == 'left':
			self.x -= 2

		if self.x >= 480-50:
			self.direction = 'left'
		elif self.x <= 0:
			self.direction = 'right'

class Bullet(object):
	
	def __init__(self, x, y, screen, playName):
		self.x = x
		self.y = y
		self.screen = screen
		self.image = pygame.image.load("./feiji/bullet-3.gif").convert()
		self.playName = playName

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))
		self.move()

	def move(self):	
		if self.playName == "hero":
			self.y -= 2
		elif self.playName == "enemy":
			self.y += 2


#主函数
if __name__ == "__main__":

	#1.创建一个窗口，来显示内容
	screen = pygame.display.set_mode((480,890), 0, 32)

	#2.创建一个和窗口一样大小的图片，用来充当背景
	background = pygame.image.load("./feiji/background.png").convert()

	#3.
	heroPlane = HeroPlane(screen)

	enemyPlane = EnemyPlane(screen)

	#3.把背景图片放到窗口中显示
	while True:
		#设定显示的背景图
		screen.blit(background, (0, 0))

		#读取事件
		for event in pygame.event.get():
			#判断是否点击了退出按钮
			if event.type == pygame.QUIT:
				print("exit")
				exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					heroPlane.move("K_LEFT")
				elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					heroPlane.move("K_RIGHT")
				elif event.key == pygame.K_SPACE:
					heroPlane.move("K_SPACE")
					

		heroPlane.display()

		enemyPlane.display()

		enemyPlane.move()
 
		#更新
		pygame.display.update()

		time.sleep(0.01)
