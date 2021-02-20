# -*- coding: utf-8 -*-
class CursorController:
    
    def move_right(grid):
        cursor_column = grid.get_cursor_column()
        grid_size = grid.size()
        if cursor_column == None:
            raise CursorNotSetError
        else:
            if cursor_column == grid_size - 1:
                cursor_column = 0
            else:
                cursor_column += 1
        grid.set_cursor(grid.get_cursor_row(), cursor_column)

    def move_left(grid):
        cursor_column = grid.get_cursor_column()
        grid_size = grid.size()
        if cursor_column == None:
            raise CursorNotSetError
        else:
            if cursor_column == 0:
                cursor_column = grid_size - 1
            else:
                cursor_column -= 1
        grid.set_cursor(grid.get_cursor_row(), cursor_column)

    def move_up(grid):
        cursor_row = grid.get_cursor_row()
        grid_size = grid.size()
        if cursor_row == None:
            raise CursorNotSetError
        if cursor_row == 0:
            cursor_row = grid_size - 1
        else:
            cursor_row -= 1;
        grid.set_cursor(cursor_row, grid.get_cursor_column())
        
    def move_down(grid):
        cursor_row = grid.get_cursor_row()
        grid_size = grid.size()
        if cursor_row == None:
            raise CursorNotSetError
        if cursor_row == grid_size - 1:
            cursor_row = 0
        else:
            cursor_row += 1;
        grid.set_cursor(cursor_row, grid.get_cursor_column())
        

class CursorNotSetError(Exception):
    def __init__(self, *args):
        Exception.__init__(self, args)
    