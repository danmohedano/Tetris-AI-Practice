import pygame
class Piece:
	COLOR_ID = [pygame.Color(105, 105, 105), pygame.Color(0, 255, 255), pygame.Color(0, 0, 139), pygame.Color(255, 165, 0), pygame.Color(255, 255, 0), pygame.Color(0, 128, 0), pygame.Color(186, 85, 211), pygame.Color(255, 0, 0), pygame.Color(255, 250, 250)]
	
	def __init__(self, id, GW):
		self.id = id
		self.posX = GW/2 - 2;
		self.posY = -4;
		self.cells = [0]*16
		self.setupCells()


	def setupCells(self):
		# setups the cells 
		if (self.id == 1):
			self.cells = [	0, 0, 1, 0,
							0, 0, 1, 0,
							0, 0, 1, 0,
							0, 0, 1, 0]
		elif (self.id == 2):
			self.cells = [	0, 0, 1, 0,
							0, 0, 1, 0,
							0, 1, 1, 0,
							0, 0, 0, 0]
		elif (self.id == 3):
			self.cells = [	0, 1, 0, 0,
							0, 1, 0, 0,
							0, 1, 1, 0,
							0, 0, 0, 0]
		elif (self.id == 4):
			self.cells = [	0, 0, 0, 0,
							0, 1, 1, 0,
							0, 1, 1, 0,
							0, 0, 0, 0]
		elif (self.id == 5):
			self.cells = [	0, 1, 0, 0,
							0, 1, 1, 0,
							0, 0, 1, 0,
							0, 0, 0, 0]
		elif (self.id == 6):
			self.cells = [	0, 0, 0, 0,
							0, 1, 0, 0,
							1, 1, 1, 0,
							0, 0, 0, 0]
		elif (self.id == 7):
			self.cells = [	0, 0, 1, 0,
							0, 1, 1, 0,
							0, 1, 0, 0,
							0, 0, 0, 0]

	def move(self, direction: int):
		if (direction < 0):
			self.posX -= 1
		elif(direction == 0):
			self.posY += 1
		else:
			self.posX += 1

	def rotate(self, direction: int):
		if (direction > 0):
			self.transpose()
			self.reverseRow()
		else:
			self.reverseRow()
			self.transpose()

	def transpose(self):
		aux = 0
		for i in range(4):
			for j in range(4):
				if (i > j):
					aux = self.cells[i+4*j]
					self.cells[i+4*j] = self.cells[j+4*i]
					self.cells[j+4*i] = aux

	def reverseRow(self):
		aux = 0
		for j in range(4):
			for i in range(2):
				aux = self.cells[i+4*j]
				self.cells[i+4*j] = self.cells[3-i+4*j]
				self.cells[3-i+4*j] = aux

	def getX(self) -> int:
		return self.posX

	def getY(self) -> int:
		return self.posY

	def getId(self) -> int:
		return self.id

	def draw(self, offset: int, dim: int):
		for i in range(4):
			for j in range(4):
				if (self.cells[i+4*j] != 0 and (self.posY + j) >= 0):
					pygame.draw.rect(pygame.display.get_surface(), self.COLOR_ID[self.id], pygame.Rect(offset+(self.posX+i)*dim, offset+(self.posY+j)*dim, dim, dim))