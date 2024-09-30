import pygame
import random

# Define las constantes del juego
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
BLOCK_SIZE = 20
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BOARD_X = 50
BOARD_Y = 50
COLORS = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255)]

# Define la clase Block
class Block:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (BOARD_X + self.x * BLOCK_SIZE, BOARD_Y + self.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Define la clase Board
class Board:
    def __init__(self):
        self.grid = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]
        self.current_block = None

    def new_block(self):
        x = BOARD_WIDTH // 2
        y = 0
        color = random.randint(1, len(COLORS) - 1)
        self.current_block = Block(x, y, COLORS[color])

    def draw(self, surface):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.grid[y][x] != 0:
                    color = COLORS[self.grid[y][x]]
                    pygame.draw.rect(surface, color, (BOARD_X + x * BLOCK_SIZE, BOARD_Y + y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        if self.current_block is not None:
            self.current_block.draw(surface)

    def update(self):
        if self.current_block is None:
            self.new_block()
        else:
            self.current_block.y += 1
            if self.collides():
                self.add_to_grid()
                self.current_block = None

    def collides(self):
        if self.current_block.y >= BOARD_HEIGHT:
            return True
        if self.current_block.x < 0 or self.current_block.x >= BOARD_WIDTH:
            return True
        if self.grid[self.current_block.y][self.current_block.x] != 0:
            return True
        return False

    def add_to_grid(self):
        for y in range(4):
            for x in range(4):
                if self.current_block.x + x >= 0 and self.current_block.x + x < BOARD_WIDTH and self.current_block.y + y >= 0 and self.current_block.y + y < BOARD_HEIGHT:
                    if self.current_block.color != COLORS[0]:
                        self.grid[self.current_block.y + y][self.current_block.x + x] = self.current_block.color

# Inicializa Pygame
pygame.init()

# Crea la ventana del juego
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Crea el tablero del juego
board = Board()

# Bucle principal del juego
while True:
    # Maneja los eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualiza el juego
    board.update()

    # Dibuja el juego
    screen.fill(COLORS[0])
    board.draw(screen)
    pygame.display.update()
