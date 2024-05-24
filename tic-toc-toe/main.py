"""This module contains the main logic for a Tic-Tac-Toe game."""

import ioput as io
from game_engine import TicTacToe, Player


def create_player(players: list):
    """
    Create a player for the Tic-Tac-Toe game.
    Args:
        players (list): List of existing players.
    Returns:
        Player: The created player.
    Raises:
        KeyError: If an error occurs during player creation.
    """
    signs = ["X", "O"]
    players_count = len(players)
    while True:
        try:
            name = io.read_text("Please enter the name: ")
            if players_count != 1:
                sign = io.read_text(f"{name} choose your sign: ")
            elif len(players) > 0:
                first_player = players[0]
                signs.remove(first_player.sign)
                sign = signs.pop()
                print(
                    f"First player {first_player.name}, selected {first_player.sign}\n"
                    f"So second player {name}, assigned {sign}"
                )
            player = Player(name=name, sign=sign)
            print(f"Player name: {player.name} and sign: {player.sign}")
            return player
        except KeyError as message:
            print(f"{message}\nFailed to get registration! Try again\n")


def create_the_game():
    """
    Create a new Tic-Tac-Toe game.
    Returns:
        TicTacToe: The created game.
    """
    players = []
    for i in range(2):
        print(f"For {i+1}. player")
        player = create_player(players)
        players.append(player)
    return TicTacToe(players=players)


def main():
    """
    The main function to run the Tic-Tac-Toe game.
    """
    game = create_the_game()
    print(f"\n{game.display_board()}")
    players = game.players
    while game.game_on:
        for player in players:
            while True:
                number = io.read_int_ranged(
                    f"{player.name}`s turn\n{player.name}"
                    " Please select a number between 1 and 9: ",
                    minimum_value=1,
                    maximum_value=9,
                )
                board = game.player_selected(player=player, number=number)
                if not board:
                    print("This place is already taken, choose a number from the table")
                    continue
                break
            print(f"\n{board}")
            if game.is_there_winner(player=player):
                game.game_on = False
                print(f"The winner is {player.name.upper()}")
                break
            if game.is_board_full():
                game.game_on = False
                print("DRAW")
                break


if __name__ == "__main__":
    main()
