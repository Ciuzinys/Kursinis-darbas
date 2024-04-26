# Coursework Paper: Snake Game Report

## 1. Introduction

### a. What is your application?

My application is a classic Snake game implemented using the Pygame library in Python. The Snake game is a simple arcade game where the player controls a snake that grows longer as it eats food (represented by red apples) while avoiding collisions with walls and itself.

### b. How to run the program?

To run the program, ensure you have Python and Pygame installed on your system. Python can be downloaded from the official website [here](https://www.python.org), and Pygame can be installed using pip in PowerShell using a command:
Pip install pygame

Once installed, execute the Python script `SnakeGame.py` by running the following command in the terminal:
Python SnakeGame.py

### c. How to use the program?

- Use the arrow keys (up, down, left, right) on your keyboard to control the movement of the snake.
- The snake will continuously move in the direction specified by the arrow keys.
- The objective is to guide the snake to eat the red apples that appear on the screen.
- Each time the snake eats an apple, it grows longer.
- Avoid collisions with the walls or the snake's own body, as this will end the game.


## 2. Body/Analysis

### a. Explain how the program covers functional requirements

The program fulfills the following functional requirements:

1. **User Control**: Allows the user to control the snake's movement using the arrow keys. This functionality is implemented by capturing keyboard events and updating the snake's direction accordingly.

2. **Growth Mechanism**: Increases the snake's length when it eats the apple. When the snake's head collides with the apple, a new segment is added to the snake's body, making it longer.

3. **Game Over Conditions**: Ends the game when the snake collides with the walls or itself. This is achieved by checking for collisions between the snake's head and the game boundaries or its own body segments.

4. **Polimorphism**: Polimorphism is used between the lines 41 and 52. Code line: def move(self), def reset(self), def draw(self). I used polimorphism, because it allowed me to define methods in the child class that have the same name as the methods in the parent class

5. **Abstraction**: Abstraction is used between the lines 24 and 29. Code line: @abstractionmethod. I chose to use abstraction here, because other people do not really need to know how the snake is moving or how everything is drawn.

6. **Encapsulation**: Encapsulation is used between the lines 20 and 84. Code line: class GameObject. Encapsulation is used thoughout the entire code, but it shows more accurately in lines where a class is used.

7. **Inheritance**: Inheritance is used between the lines 32 and 64. Code line: class Apple(GameObject), class Snake(GameObject). I chose to use inheritance here, because I needed that the snake and apple would take the coordinates.

## 3. Results and Summary

### a. Results

The development of the Snake game presented several challenges that I encountered and successfully addressed:

1. **Collision Detection**: Implementing accurate collision detection between the snake's head and the game boundaries or its own body segments was a significant challenge. I had to ensure that collisions were detected reliably and consistently to provide a seamless gaming experience.

2. **Game Logic Complexity**: Managing the game's logic, including the snake's movement, growth mechanism, and game over conditions, required careful planning and implementation. I needed to design efficient algorithms to handle these aspects while maintaining code readability and modularity.

3. **User Interface Design**: Designing an intuitive user interface that provides clear feedback to the player, such as displaying the score and high score, posed a challenge. I focused on creating a clean and visually appealing interface that enhances the overall gaming experience.

4. **Testing and Bug Fixing**: Testing the game thoroughly to identify and fix any bugs or issues was an ongoing challenge throughout the development process. I conducted rigorous testing to ensure the game's stability and reliability across different scenarios and users.

5. **Performance Optimization**: Optimizing the game's performance to ensure smooth gameplay, especially on lower-end hardware, was another challenge. I optimized critical sections of the code and implemented strategies such as frame rate control to maintain consistent performance.

Despite these challenges, I successfully overcame them through collaborative problem-solving, iterative development, and attention to detail. The result is a polished and enjoyable Snake game that provides a satisfying gaming experience for players of all ages.
### b. Conclusions

In conclusion, the Snake game demonstrates effective use of object-oriented programming principles and Pygame library functionalities to create an interactive gaming experience. The modular design allows for easy extension and modification of the game's features.

### c. How it would be possible to extend your application?

While the Snake game provides a simple and enjoyable gaming experience, there are several ways it could further enhance it:

1. **Customization Options**: Introducing customization options that allow players to personalize their gaming experience. This could include different snake skins, background themes, or sound effects.

2. **Challenge Modes**: Implementing challenge modes that offer unique gameplay mechanics or objectives. For example, time-based challenges where players must eat as many apples as possible within a limited time period.

3. **AI Opponent**: Adding an AI opponent for single-player mode, providing players with a more challenging experience. The AI could dynamically adjust its behavior based on the player's performance, offering increasingly difficult gameplay.

4. **Online Leaderboards**: Integrating online leaderboards where players can compete against each other for high scores. This adds a competitive element to the game and encourages replayability.

These extensions focus on enhancing the replay value and engagement of the Snake game while maintaining its simplicity and core mechanics.
## 4. Resources, references list

- Python: [Official Website] (https://www.python.org/)
- Pygame: [Pygame Website] (https://www.pygame.org/)



