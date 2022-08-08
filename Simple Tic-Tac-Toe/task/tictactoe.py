def able_to_win(player):
    global game
    horizontals = ["".join(game[y] for y in range(3 * x, 3 * x + 3)) for x in range(3)]
    verticals = ["".join(game[y] for y in range(x, x + 7, 3)) for x in range(3)]
    diagonals = ["".join([game[0], game[4], game[8]]), "".join([game[2], game[4], game[6]])]
    return any(_ for _ in [horizontals, verticals, diagonals] for _ in _ if _ == player * 3)


def is_draw(player1, player2):
    global game
    return not able_to_win(player1) and not able_to_win(player2) and all([_ != ' ' for _ in game])


def play(player1, player2):
    player = [player1, player2]
    global step
    global game
    try:
        move = input().split()
        row, col = int(move[0]), int(move[1])
        if not (0 < row < 4 and 0 < col < 4):
            print("Coordinates should be from 1 to 3!")
            return play(player1, player2)
        if game[3 * row + col - 4] != " ":
            print("This cell is occupied! Choose another one!")
            return play(player1, player2)
        game[3 * row + col - 4] = player[step % 2]
        print("\n".join(
            [9 * "-", "\n".join("| " + " ".join(game[y] for y in range(3 * x, 3 * x + 3)) + " |" for x in range(3)),
             9 * "-"]))
        if able_to_win(player[step % 2]):
            print(f"{player[step % 2]} wins")
        elif is_draw(player1, player2):
            print('Draw')
        else:
            step += 1
            return play(player1, player2)
    except ValueError:
        print("You should enter numbers!")
        return play(player1, player2)


step = 0
game = [' '] * 9
print("\n".join(
    [9 * "-", "\n".join("| " + " ".join(game[y] for y in range(3 * x, 3 * x + 3)) + " |" for x in range(3)), 9 * "-"]))
play("X", "O")
