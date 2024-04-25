import unittest
from SnakeGame import Snake, Apple, GameSettings, GameObjectFactory, loop, reset_game

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
        pass
    def test_initial_position(self):
        self.assertEqual(self.snake.x, 160)
        self.assertEqual(self.snake.y, 160)
        pass

class TestApple(unittest.TestCase):
    def setUp(self):
        self.apple = Apple()
        pass
    def test_reset_position(self):
        self.apple.reset_position()
        self.assertTrue(0 <= self.apple.x < 400)
        self.assertTrue(0 <= self.apple.y < 400)
        pass

class TestGameSettings(unittest.TestCase):
    def setUp(self):
        self.settings = GameSettings()
        pass
    def test_singleton_instance(self):
        new_instance = GameSettings()
        self.assertIs(self.settings, new_instance)
        pass

class TestGameObjectFactory(unittest.TestCase):
    def test_create_snake(self):
        snake = GameObjectFactory.create_game_object("Snake")
        self.assertIsInstance(snake, Snake)
        pass
    def test_create_apple(self):
        apple = GameObjectFactory.create_game_object("Apple")
        self.assertIsInstance(apple, Apple)
        pass

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.settings = GameSettings()
        self.snake = Snake(160, 160)
        self.apple = Apple(320, 320)
        pass
    def test_game_over_when_snake_out_of_bounds(self):
        # Arrange
        self.snake.x = 400  # Set snake out of bounds
        self.snake.y = 400
        pass
        # Act
        game_over_result = loop(self.settings, self.snake, self.apple)
        pass
        # Assert
        self.assertTrue(game_over_result)  # Check if game over is triggered
        pass

class TestResetGame(unittest.TestCase):
    def setUp(self):
        self.settings = GameSettings()
        self.snake = Snake(160, 160)
        self.apple = Apple(320, 320)
        pass
    def test_reset_game(self):
        # Arrange
        self.settings.score = 10
        self.snake.x = 200
        self.snake.y = 200
        self.snake.dx = 2
        self.snake.dy = 2
        self.snake.max_cells = 5
        self.apple.x = 240
        self.apple.y = 240
        pass
        # Act
        reset_game(self.settings, self.snake, self.apple)
        pass
        # Assert
        self.assertEqual(self.settings.score, 0)  # Score should be reset to 0
        self.assertEqual(self.snake.x, 160)  # Snake position should be reset
        self.assertEqual(self.snake.y, 160)
        self.assertEqual(self.snake.dx, 16)  # Snake direction should be reset
        self.assertEqual(self.snake.dy, 0)
        self.assertEqual(self.snake.max_cells, 4)  # Snake body length should be reset
        # Apple position should be reset, note that the position may differ due to randomization
        self.assertTrue(0 <= self.apple.x < 400)  
        self.assertTrue(0 <= self.apple.y < 400)
        pass

if __name__ == '__main__':
    unittest.main()
