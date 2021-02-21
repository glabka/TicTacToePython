# -*- coding: utf-8 -*-
from components import *
from players import *
from grid_computations import *

grid = Grid(5)
grid.print_grid(True)
grid.print_grid()
grid.set_cursor(1,3)
grid.print_grid(True)
grid.insert_cross(1,3)
grid.insert_cross(1,4)
grid.insert_circle(2,2)
grid.print_grid(True)
#grid.set_cursor(1,5)
ui_player = UIPlayer("Player 1", "O")
#print(ui_player.next_move(grid))

computations = Computations() # instantiating Computations so class method can be called
print(Computations.get_all_rows(grid))
print("\n\n")
grid.print_grid(True)
print(Computations.get_all_columns(grid))
print("\n\n")
grid.print_grid(True)
print(Computations.get_all_left_diagonals(grid))
print("\n\n")
grid.print_grid(True)
print(Computations.get_all_right_diagonals(grid))
print("\n\n")
grid.print_grid(True)
for stripe in Computations.get_all_stripes(grid):
    print(stripe)