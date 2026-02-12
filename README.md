# Pong Game 🏓

## <img width="801" height="631" alt="image" src="https://github.com/user-attachments/assets/75bf9565-5bb4-48ec-82a0-a1693140940e" />

A classic, two-player arcade Pong game built using **Python** and the **Turtle** graphics library. This project demonstrates object-oriented programming (OOP) principles by separating the logic for paddles, the ball, and the scoreboard into distinct classes.

## 🎮 Features

* **Two-Player Mode:** Play against a friend on the same keyboard.
* **Real-time Scoring:** Automatic score tracking displayed at the top of the screen.
* **Dynamic Difficulty:** The ball speeds up slightly every time it hits a paddle.
* **Smooth Controls:** Responsive paddle movement.

## 🛠️ Built With

* [Python 3](https://www.python.org/)
* `turtle` module (built-in Python graphics)

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system. You can check your version by running:

```bash
python --version

```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/abatima/Pong_Game.git

```


2. Navigate to the project directory:
```bash
cd Pong_Game

```



### Running the Game

Run the main script to start the game:

```bash
python main.py

```

## 🕹️ How to Play

The objective is to hit the ball with your paddle. If the ball passes your paddle, the opponent gets a point.

### Controls

| Player | Up Key | Down Key |
| --- | --- | --- |
| **Left Player** | `W` | `S` |
| **Right Player** | `Up Arrow` | `Down Arrow` |

## 📂 File Structure

* `main.py`: The entry point of the game. It handles the game loop and screen updates.
* `paddle.py`: Contains the `Paddle` class for creating and moving the paddles.
* `ball.py`: Contains the `Ball` class, managing movement, bouncing logic, and resets.
* `scoreboard.py`: Handles the UI, score display, and game-over logic.

## 📜 License

This project is open-source and available under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for new features (like a single-player AI mode or sound effects).

---

Created by [abatima](https://github.com/abatima)
