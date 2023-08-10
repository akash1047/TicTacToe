board = [
    "tic tac toe",
    " 1",
    " 2",
    " 3",
    " 4",
    " 5",
    " 6",
    " 7",
    " 8",
    " 9",
]

o = "🟢"
x = "❌"


def draw(position=0, player=" @"):
    if position in range(1, 10):
        board[position] = player

    print(
        """
  %s  │  %s  │  %s
──────┼──────┼──────
  %s  │  %s  │  %s
──────┼──────┼──────
  %s  │  %s  │  %s
"""
        % (
            board[1],
            board[2],
            board[3],
            board[4],
            board[5],
            board[6],
            board[7],
            board[8],
            board[9],
        )
    )


# game starts

# draw the board
draw()

player_is_o = True

while True:
    player = o if player_is_o else x

    # switch players
    player_is_o = not player_is_o

    i = input(f" {player}'s turn > ")

    draw(int(i), player)
