# -*- coding: utf-8 -*-
from components import *

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