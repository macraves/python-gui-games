"""Tic Tac Toe Methods"""

from player import Player


class TicTacToe:
    """A class representing the Tic Tac Toe game."""

    def __init__(self, players: list):
        """
        Initialize the Tic Tac Toe game.
        Args:
            players (list): A list of Player objects representing the players of the game.
        """
        self.players = players
        self.game_on = True
        self._create_game_board()

    def _create_game_board(self):
        """
        Create the game board for Tic Tac Toe.
        """
        numbers = list(range(1, 10))[::-1]
        board = [
            [f"{numbers.pop() if numbers else ''}" for _ in range(3)] for _ in range(3)
        ]
        self.board = board

    def display_board(self):
        """
        Display the current state of the game board.
        Returns:
            str: The formatted string representation of the game board.
        """
        underlines = [["-" * 9] for _ in range(2)]
        board = "\n".join(
            map(
                lambda row: " | ".join(row)
                + f"\n{underlines.pop()[0] if underlines else ''}",
                self.board,
            )
        )
        return board

    def player_selected(self, player: Player, number: int):
        """
        Process the player's move and update the game board.
        Args:
            player (Player): The Player object representing the current player.
            number (int): The number representing the position on the game board.
        Returns:
            Union[str, bool]: The updated game board if the move is valid, False otherwise.
        """
        number = str(number)
        number_index = None
        for row in self.board:
            if number in row:
                number_index = row.index(number)
                if row[number_index] in Player.valid_signs:
                    return False
                row[number_index] = player.sign
                break
        if number_index is None:
            return False
        return self.display_board()

    def is_there_winner(self, player: Player):
        """
        Check if there is a winner in the game.
        Args:
            player (Player): The Player object representing the current player.
        Returns:
            bool: True if the player has won, False otherwise.
        """
        winning_conditions = (
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        )
        return [player.sign, player.sign, player.sign] in winning_conditions

    def is_board_full(self):
        """
        Check if the game board is full.
        Returns:
            bool: True if the game board is full, False otherwise.
        """
        return all(value in Player.valid_signs for row in self.board for value in row)
