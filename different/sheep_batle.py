import random

# Создаем игровое поле
board = [[' ' for _ in range(10)] for _ in range(10)]


def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 10)


def check_winner(board, player):
    # Проверяем строки, столбцы и диагонали
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))


def player_turn():
    while True:
        row = int(input("Выберите строку (0, 1, 2): "))
        col = int(input("Выберите столбец (0, 1, 2): "))
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            return row, col
        print("Неверный ход. Попробуйте еще раз.")


def computer_turn():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col


def main():
    print("Игра в морской бой!")
    print_board(board)

    while True:
        player_row, player_col = player_turn()
        board[player_row][player_col] = 'X'
        print_board(board)

        if check_winner(board, 'X'):
            print("Вы победили!")
            break
        elif is_board_full(board):
            print("Ничья!")
            break

        print("Ход компьютера:")
        comp_row, comp_col = computer_turn()
        board[comp_row][comp_col] = 'O'
        print_board(board)

        if check_winner(board, 'O'):
            print("Компьютер победил!")
            break
        elif is_board_full(board):
            print("Ничья!")
            break


if __name__ == "__main__":
    main()
