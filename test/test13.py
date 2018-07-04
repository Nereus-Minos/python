#encoding=utf-8

import pygame

import time

'''
1.搭建界面
2.
'''
class HeroPlane(object):

	def __init__(self, screen):
		#position
		self.x = 230
		self.y = 600
		#
		self.screen = screen
		#
		self.image = pygame.image.load("./feiji/hero.gif").convert()

	def display(self):
		self.screen.blit(self.image, (self.x, self.y))

	def move(self, KEYDWON):
		if KEYDWON == "K_LEFT":
			self.x -= 5
		elif KEYDWON == "K_RIGHT":
			self.x += 5

#
if __name__ == "__main__":

	#1.创建一个窗口，来显示内容
	screen = pygame.display.set_mode((480,890), 0, 32)

	#2.创建一个和窗口一样大小的图片，用来充当背景
	background = pygame.image.load("./feiji/background.png").convert()

	#3.
	heroPlane = HeroPlane(screen)

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
					print("space")

		heroPlane.display()

		#更新
		pygame.display.update()

		time.sleep(0.01)
