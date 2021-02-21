# -*- coding: utf-8 -*-
from game_mechanics import *

class Player:
    def __init__(self, name, val):
        Player.verify_val_is_correct(val)
        self._name = name
        self._val = val
        
    def get_name(self):
        return self._name
    
    def get_val(self):
        return self._val
    
    def verify_val_is_correct(val):
        if val != "X" and val != "O":
            raise ValueError("val can be either \"X\" or \"O\"")
    
class UIPlayer(Player):
    def __init__(self, name, val):
        Player.__init__(self, name, val)
        self._input_message = "Enter either sequence of w, s, a or d to change cursor position or enter i to insert " + val

    def next_move(self, grid):
        print(self._input_message)
        grid.print_grid(True)
        while(True):
            input_str = input()
            insert_entered = False
            while(len(input_str) > 0):
                char = input_str[0]
                if len(input_str) != 1:
                    input_str = input_str[1:]
                else:
                    input_str = ""
                    
                char = char.lower()
                if char == "w":
                    CursorController.move_up(grid)
                    grid.print_grid(True)
                elif char == "s":
                    CursorController.move_down(grid)
                    grid.print_grid(True)
                elif char == "a":
                    CursorController.move_left(grid)
                    grid.print_grid(True)
                elif char == "d":
                    CursorController.move_right(grid)
                    grid.print_grid(True)
                elif char == "i":
                    insert_entered = True
                    break
                else:
                    print(self._input_message)
                    
            if not insert_entered:
                continue
            elif grid.get_val(grid.get_cursor_row(), grid.get_cursor_column()) == None:
                return (grid.get_cursor_row(), grid.get_cursor_column())
            else:
                print("On given coordinates there is already a filled up square. Please choose different coordinates.")
            
            