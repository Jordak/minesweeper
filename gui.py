
import tkinter as tk
from tkinter import messagebox
from minesweeper import Minesweeper

class MinesweeperGUI:
  def __init__(self, game):
    self.game = game
    self.root = tk.Tk()
    self.buttons = [[tk.Button(self.root, command=lambda x=i, y=j: self.on_click(x, y)) for j in range(game.n)] for i in range(game.m)]
    for i in range(game.m):
      for j in range(game.n):
        self.buttons[i][j].grid(row=i, column=j)

  def on_click(self, x, y):
    if self.game.uncover(x, y):
      self.buttons[x][y].config(text="X", state="disabled")
      self.game_over()
    else:
      self.update_buttons()
      if self.game.check_win():
        self.game_won()

  def update_buttons(self):
    for i in range(self.game.m):
      for j in range(self.game.n):
        if self.game.game_state[i][j] != " ":
          self.buttons[i][j].config(text=self.game.game_state[i][j], state="disabled")

  def game_over(self):
    self.root.update()
    for i in range(self.game.m):
      for j in range(self.game.n):
        self.buttons[i][j].config(state="disabled")
    messagebox.showinfo("Game Over", "You hit a mine!")
    self.root.destroy()

  def game_won(self):
    self.root.update()
    for i in range(self.game.m):
      for j in range(self.game.n):
        self.buttons[i][j].config(state="disabled")
    messagebox.showinfo("Congratulations", "You have won the game!")
    self.root.destroy()

  def run(self):
    self.root.mainloop()

if __name__ == "__main__":
  m, n, num_mines = map(int, input("Enter the size of the board (m n) and number of mines: ").split())
  game = Minesweeper(m, n, num_mines)
  gui = MinesweeperGUI(game)
  gui.run()