import pygame
import random

pygame.init()

# Set up display
WIDTH = 400
HEIGHT = 400
GRID = 16
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Base class for game objects
class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        pass  # Placeholder for movement method

    def draw(self):
        pass  # Placeholder for drawing method

# Snake class inheriting from GameObject
class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.dx = GRID
        self.dy = 0
        self.cells = []
        self.max_cells = 4
        self.direction_queue = []

    def reset(self):
        self.__init__(160, 160)

    def move(self):
        if self.direction_queue:
            self.dx, self.dy = self.direction_queue.pop(0)
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        for cell in self.cells:
            pygame.draw.rect(DISPLAY, GREEN, (cell["x"], cell["y"], GRID - 1, GRID - 1))

# Apple class inheriting from GameObject
class Apple(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)

    def reset_position(self):
        self.x = random.randint(0, (WIDTH - GRID) // GRID) * GRID
        self.y = random.randint(0, (HEIGHT - GRID) // GRID) * GRID

    def draw(self):
        pygame.draw.rect(DISPLAY, RED, (self.x, self.y, GRID - 1, GRID - 1))

# GameSettings singleton class
class GameSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.score = 0
            cls._instance.high_score = 0
        return cls._instance

# Factory Method Pattern: GameObjectFactory class
class GameObjectFactory:
    @staticmethod
    def create_game_object(obj_type, x, y):
        if obj_type == "Snake":
            return Snake(x, y)
        elif obj_type == "Apple":
            return Apple(x, y)

# Function to save game state to a text file
def save_game_state(game_state, settings, snake, apple):
    with open(game_state, 'w') as file:
        file.write(f"{settings.score}\n")
        file.write(f"{settings.high_score}\n")
        file.write(f"{snake.x}\n")
        file.write(f"{snake.y}\n")
        file.write(f"{snake.dx}\n")
        file.write(f"{snake.dy}\n")
        file.write(f"{snake.max_cells}\n")  # Save snake's body length
        file.write(f"{apple.x}\n")
        file.write(f"{apple.y}\n")

# Function to load game state from a text file
def load_game_state(game_state, settings, snake, apple):
    try:
        with open(game_state, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 9:  # Check if there are enough lines in the file
                settings.score = int(lines[0].strip())
                settings.high_score = int(lines[1].strip())
                snake.x = int(lines[2].strip())
                snake.y = int(lines[3].strip())
                snake.dx = int(lines[4].strip())
                snake.dy = int(lines[5].strip())
                snake.max_cells = int(lines[6].strip())  # Load snake's body length
                apple.x = int(lines[7].strip())
                apple.y = int(lines[8].strip())
            else:
                # If file doesn't have enough lines, start with default state
                reset_game(settings, snake, apple)
    except FileNotFoundError:
        # If file not found, start with default state
        reset_game(settings, snake, apple)

# Game loop
def loop(settings, snake, apple):
    global count

    if count < 4:
        count += 1
        return

    count = 0
    DISPLAY.fill(WHITE)

    # Move snake
    snake.move()

    # Wrap snake position
    if not (0 <= snake.x < WIDTH and 0 <= snake.y < HEIGHT):
        game_over()
        return

    # Update snake cells
    snake.cells.insert(0, {"x": snake.x, "y": snake.y})
    if len(snake.cells) > snake.max_cells:
        snake.cells.pop()

    # Check collision with itself
    for cell in snake.cells[1:]:
        if cell["x"] == snake.x and cell["y"] == snake.y:
            game_over()
            return

    # Draw grid lines
    for x in range(0, WIDTH, GRID):
        pygame.draw.line(DISPLAY, (200, 200, 200), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID):
        pygame.draw.line(DISPLAY, (200, 200, 200), (0, y), (WIDTH, y))

    # Draw apple
    apple.draw()

    # Draw snake
    snake.draw()

    # Snake ate apple
    for cell in snake.cells:
        if cell["x"] == apple.x and cell["y"] == apple.y:
            snake.max_cells += 1
            apple.reset_position()
            settings.score += 1
            if settings.score > settings.high_score:
                settings.high_score = settings.score

    # Draw scores
    font = pygame.font.SysFont(None, 24)
    score_text = font.render(f"Score: {settings.score}", True, (0, 0, 0))
    high_score_text = font.render(f"High Score: {settings.high_score}", True, (0, 0, 0))
    DISPLAY.blit(score_text, (10, 10))
    DISPLAY.blit(high_score_text, (WIDTH - high_score_text.get_width() - 10, 10))

    pygame.display.update()

# Show game over message box
def game_over():
    font = pygame.font.SysFont(None, 36)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    restart_text = font.render("Restart Game", True, (0, 0, 255))
    exit_text = font.render("Exit", True, (0, 0, 255))

    DISPLAY.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
    DISPLAY.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
    DISPLAY.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                restart_rect = pygame.Rect(WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2,
                                           restart_text.get_width(), restart_text.get_height())
                exit_rect = pygame.Rect(WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 50,
                                        exit_text.get_width(), exit_text.get_height())
                if restart_rect.collidepoint(x, y):
                    reset_game(settings, snake, apple)
                    return
                elif exit_rect.collidepoint(x, y):
                    pygame.quit()
                    quit()

# Reset game state
def reset_game(settings, snake, apple):
    settings.score = 0
    snake.reset()
    apple.reset_position()

# Listen to keyboard events to move the snake
def handle_key_event(event, snake):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and snake.dx == 0:
            snake.direction_queue.append((-GRID, 0))
        elif event.key == pygame.K_UP and snake.dy == 0:
            snake.direction_queue.append((0, -GRID))
        elif event.key == pygame.K_RIGHT and snake.dx == 0:
            snake.direction_queue.append((GRID, 0))
        elif event.key == pygame.K_DOWN and snake.dy == 0:
            snake.direction_queue.append((0, GRID))

# Initialize game objects using Factory Method
count = 0
settings = GameSettings()
factory = GameObjectFactory()
snake = factory.create_game_object("Snake", 160, 160)
apple = factory.create_game_object("Apple", 320, 320)

# Load game state from file (if exists)
load_game_state("game_state.txt", settings, snake, apple)

# Start the game
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            handle_key_event(event, snake)

    loop(settings, snake, apple)
    clock.tick(15)  # Frames per second

# Save game state before quitting
save_game_state("game_state.txt", settings, snake, apple)

pygame.quit()

