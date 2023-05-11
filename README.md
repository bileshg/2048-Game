## 2048 Game

This project is a simple implementation of the classic 2048 game using Python, designed to run in the command-line interface.

### Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

### Requirements

This project requires the following dependencies:

- Python 3.6+
- Poetry
- terminaltables
- termcolor

### Installation

1. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already.

2. Clone the repository:
   ```bash
   git clone https://github.com/bileshg/2048-Game
   ```
3. Change to the repository directory:
   ```bash
   cd 2048-Game
   ```

4. Install the dependencies using Poetry:
   ```bash
   poetry install
   ```

### Usage

1. Run the `main.py` file to launch the game using Poetry:
   ```bash
   poetry run python main.py
   ```
2. The command-line interface will display the 2048 game board.

3. Players use the `W`, `A`, `S`, `D` keys to move the tiles, trying to combine them to reach the 2048 tile. Press `X` to quit the game.

4. Once the game ends, you can run the `main.py` file again to start a new game.