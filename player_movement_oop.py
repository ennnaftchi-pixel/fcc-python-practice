# player_movement_oop.py
"""A module implementing player movement on a 2D grid using OOP principles. 
Includes a base Player class and a Pawn subclass with movement capabilities. 
The Pawn can level up to gain additional movement options. """

from abc import ABC, abstractmethod
import random
from typing import List, Tuple


class Player(ABC):
    """
    Abstract base class representing a player on a 2D grid.
    """

    def __init__(self) -> None:
        self.moves: List[Tuple[int, int]] = []
        self.position: Tuple[int, int] = (0, 0)
        self.path: List[Tuple[int, int]] = [self.position]

    def make_move(self) -> Tuple[int, int]:
        """
        Makes a random move from the available moves and updates the player's position.
        """
        move = random.choice(self.moves)
        x, y = self.position
        dx, dy = move
        self.position = (x + dx, y + dy)
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self) -> None:
        """
        Improves the player's movement capabilities.
        """
        pass


class Pawn(Player):
    """
    A basic player that can move in four directions.
    """

    def __init__(self) -> None:
        super().__init__()
        self.moves = [
            (0, 1),    # up
            (0, -1),   # down
            (-1, 0),   # left
            (1, 0)     # right
        ]

    def level_up(self) -> None:
        """
        Adds diagonal movement options.
        """
        self.moves.extend([
            (1, 1),     # up-right
            (1, -1),    # down-right
            (-1, 1),    # up-left
            (-1, -1)    # down-left
        ])


if __name__ == "__main__":
    pawn = Pawn()

    for _ in range(5):
        pawn.make_move()

    pawn.level_up()

    for _ in range(5):
        pawn.make_move()

    print("Final position:", pawn.position)
    print("Path taken:", pawn.path)
