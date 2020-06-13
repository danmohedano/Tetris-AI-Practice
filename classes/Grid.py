from classes.Piece import Piece
from random import randint
class Grid:
    # the grid for the game
		
    GAME_OVER = 0
    PAUSE = 1
    fontName = "consolas"
    fontSize = 32
    font = pygame.font.Font(pygame.font.match_font(fontName),fontSize)
	
    # grid config variables
    GW = 10
    GH = 20
    BLOCK_DIM = 25
    BORDER = 10
    OFFSET = 50

    # grid data
    blocks = [0] * (GW*GH)
    currentPiece = None
    nextPiece = None

	# game status and scoring systems
	level = 0
	score = 0
	linesCleared = 0
	initialLevel = 0

	def __init__(self):
		self.currentPiece = Piece(randint(1,7), GW)
		self.generateNewPiece()

	def __init__(self,l):
		self.init()
		self.level = level
		self.initialLevel = level;

	def draw(self):
		print("test")

	def generateNewPiece(self):
		# Generates a new piece
		self.nextPiece = Piece(randint(1,7), GW)
		if (self.currentPiece.id == self.nextPiece.id):
			self.generateNewPiece()

	def move(self, direction: int) -> bool:
		check = True
		if (direction == -1):
			check = self.canFit(-1, 0, 0)
		elif(direction == 0):
			check = self.canFit(0, 1, 0)
		else:
			check = self.canFit(1, 0, 0)

	def rotate(self, direction: int) -> bool:
		if (self.canFit(0,0,direction) == False): 
			return False
		currentPiece.rotate(direction)
		return True


	def canFit(self, offsetX: int, offsetY: int, rotation: int) -> bool:
		# checks if the current piece can fit after a given action
		for i in range(4):
			for j in range(4):
				if (currentPiece.get(i,j,rotation) != 0):
					if ((currentPiece.getX() + offsetX + i) < 0 or (currentPiece.getX() + offsetX + i) >= GW):
						# check horizontal limits
						return False;
					if ((currentPiece.getY() + offsetY + j) >= GH):
						# check vertical limits
						return False;
					if ((currentPiece.getX() + offsetX + i) >= 0 and (currentPiece.getY() + offsetY + j) >= 0):
						# check collision with another piece
						if (blocks[(currentPiece.getX() + offsetX + i) + (currentPiece.getY() + offsetY + j)*GW] != 0):
							return False;
		return True

    
	def gravity(self):
		# Simulate the gravity (moving a piece down and checking if the piece has come in contact with another piece or the grid limits)
		# If so, saves the piece into the block grid and creates a new piece.
		if (self.move(0) == False):
			if (self.savePiece() == False):
				GAME_OVER = 1
				return
			self.checkLine()
			self.currentPiece = this.nextPiece
			self.generateNewPiece()

	def savePiece(self) -> bool:
		# Save the current piece into the blocks grid
		flag = True
		for i in range(4):
			for j in range(4):
				if (currentPiece.get(i,j,0) != 0):
					if ((currentPiece.getY() + j) >= 0):
						self.blocks[(currentPiece.getX() + i) + (currentPiece.getY() + j)*GW] = currentPiece.getId()
					else:
						flag = False
		return flag

	def checkLine(self):
		# Checks if there is any full line
		nLines = 0
		flag = 0
		for j in range(GH):
			flag = 0
			for i in range(GW):
				if (self.blocks[i + j*GW] == 0):
					flag = 1
					break

			if (flag == 0):
				nLines += 1
				self.shift(j)

		self.updateScore(nLines)

	def shift(self, line: int):
		# Shifts the block grid down until a given line
		for j in range(line, 0, -1):
			for i in range(GW):
				self.blocks[i + j*GW] = self.blocks[i + (j-1)*GW]

		for i in range(GW):
			self.blocks[i] = 0

	def updateScore(self, nLines: int):
		# Updates the score according to the number of lines cleared
		if (nLines == 1):
			self.score += 40*(self.level + 1)
		elif (nLines == 2):
			self.score += 100*(self.level + 1)
		elif (nLines == 3):
			self.score += 300*(self.level + 1)
		elif (nLines == 4):
			self.score += 1200*(self.level + 1)

		self.linesCleared += nLines
		self.level = min(self.initialLevel + int(self.linesCleared/10))

	def getLevel(self) -> int:
		return self.level
