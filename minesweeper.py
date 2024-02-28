import random

class Minesweeper:
  def __init__(self, m, n, num_mines):
    self.m, self.n = m, n
    self.num_mines = num_mines
    self.board = None
    self.game_state = [[' ' for _ in range(n)] for _ in range(m)]  # Game state board with all cells hidden
    self.mines = None

  def create_board(self, m, n, num_mines, first_move):
    board = [[0. for _ in range(n)] for _ in range(m)]
    mines = []
    while len(mines) < num_mines:
      x, y = random.randint(0, m-1), random.randint(0, n-1)
      if (x, y) not in mines and (x, y) != first_move and not self.is_adjacent(first_move, (x, y)):
        mines.append((x, y))
        board[x][y] = 1.
    return board, mines

  def is_valid_move(self, x, y):
    return 0 <= x < self.m and 0 <= y < self.n

  def count_mines_around(self, x, y):
    count = 0
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        nx, ny = x + dx, y + dy
        if self.is_valid_move(nx, ny) and self.board[nx][ny] == 1.:
          count += 1
    return count

  def uncover(self, x, y):
    if self.board is None and self.mines is None:
      self.board, self.mines = self.create_board(self.m, self.n, self.num_mines, (x, y))
    if not self.is_valid_move(x, y) or self.game_state[x][y] != ' ':
      return False
    if self.board[x][y] == 1.:
      self.game_state[x][y] = 'X'  # Uncover the mine
      return True
    else:
      count = self.count_mines_around(x, y)
      self.game_state[x][y] = str(count)  # Uncover the cell
      if count == 0:  # If no mines around, uncover all neighboring cells
        for dx in [-1, 0, 1]:
          for dy in [-1, 0, 1]:
            self.uncover(x + dx, y + dy)
      return False

  def is_adjacent(self, cell1, cell2):
    return abs(cell1[0] - cell2[0]) <= 1 and abs(cell1[1] - cell2[1]) <= 1

  def print_board(self):
    print('   ' + '   '.join(str(i) for i in range(self.n)))  # Print column numbers
    print(' ' + '-' * (self.n * 4 + 1))  # Print horizontal line after each row
    for i, row in enumerate(self.game_state):
      print(str(i) + '| ' + ' | '.join(row) + ' |')  # Add row number and borders to the first and last columns
      print(' ' + '-' * (self.n * 4 + 1))  # Print horizontal line after each row

  def check_win(self):
    return all(self.game_state[i][j] != ' ' for i in range(self.m) for j in range(self.n) if self.board[i][j] != 1.)


if __name__ == "__main__":
  m, n, num_mines = map(int, input("Enter the size of the board (m n) and number of mines: ").split())
  game = Minesweeper(m, n, num_mines)

  while True:
    game.print_board()
    x, y = map(int, input("Enter your move (x y): ").split())
    if game.uncover(x, y):
      print("Game Over! You hit a mine.")
      game.print_board()
      break
    elif game.check_win():
      print("Congratulations! You have won the game.")
      game.print_board()
      break

