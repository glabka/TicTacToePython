# -*- coding: utf-8 -*-
class Grid:
    def __init__(self, size):
        """size is positive integer"""
        self._grid = [[ None for i in range(size) ] for j in range(size) ]
        self._cursor_row = None
        self._cursor_column = None

    def print_grid(self, debug_enabled = False):
        """debug_enabled is boolean"""
        # printing column's numbers
        if debug_enabled:
            print(" ", end ="")
            for column in range(0, len(self._grid)):
                print(column, end = "")
                if column != len(self._grid) - 1:
                    print("|", end = "")
            print()
        
        for row in range(0, len(self._grid)):
            if debug_enabled:
                print(row, end = "")
            for column in range(0, len(self._grid)):
                val = self._grid[row][column]
                cursor_enabled = row == self._cursor_row and column == self._cursor_column
                if val == None:
                    if cursor_enabled:
                        print("+", end = "")
                    else:
                        print(" ", end = "")
                else:
                    if cursor_enabled:
                        print(val.lower(), end = "")
                    else:
                        print(val, end = "")
                if column != len(self._grid) - 1:
                    print("|", end = "")
            print()

    def set_cursor(self, row, column):
        self.verify_coos_in_range(row, column)
        self._cursor_row = row
        self._cursor_column = column
    
    def _insert_val(self, row, column, val):
        self.verify_coos_in_range(row, column)
        if self._grid[row][column] != None:
            raise AlreadyFilledSquareError
        self._grid[row][column] = val
    
    def insert_cross(self, row, column):
        self._insert_val(row, column, "X")

    def insert_circle(self, row, column):
        self._insert_val(row, column, "O")
        
    def get_val(self, row, column):
        return self._grid[row][column]
        
    def verify_coos_in_range(self, row, column):
        grid_size = self.size()
        if row >= grid_size:
            raise IndexError("row:" + str(row) + " >= grid_size:" + str(grid_size))
        if column >= grid_size:
            raise IndexError("column:" + str(column) + " >= grid_size:" + str(grid_size))
        if row < 0:
            raise IndexError("row:" + str(row) +" < 0")
        if column < 0:
            raise IndexError("column:" + str(column) +" < 0")
            
    def size(self):
        return len(self._grid)
    
    def get_cursor_column(self):
        return self._cursor_column
    
    def get_cursor_row(self):
        return self._cursor_row

class Coo:
    def __init__(self, row, column):
        self._row = row
        self._column = column
    
    def get_row(self):
        return self._row
    
    def get_column(self):
        return self._column

class ValuedCoo(Coo):
    def __init__(self, row, column, val):
        Coo.__init__(self, row, column)
        self._val = val
        
    def get_val(self):
        return self._val

# custom exceptions            
class AlreadyFilledSquareError(Exception):
    def __init__(self, *args):
        Exception.__init__(self, args)