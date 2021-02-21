# -*- coding: utf-8 -*-
from components import Coo, ValuedCoo

class Computations:
    def __init__(self):
        pass
    
    @classmethod
    def get_all_rows(cls, grid):
        return cls.get_all_rows_or_columns(grid, cls.create_row)
    
    @classmethod
    def get_all_columns(cls, grid):
        return cls.get_all_rows_or_columns(grid, cls.create_column)
    
    def get_all_rows_or_columns(grid, fun):
        all_rows_or_columns = []
        for index in range(grid.size()):
            all_rows_or_columns.append(fun(grid, index))
        return all_rows_or_columns
        
    def create_row(grid, row_index):
        row = []
        for column_index in range(grid.size()):
            val = grid.get_val(row_index, column_index)
            row.append(ValuedCoo(row_index, column_index, val))
        return row
    
    def create_column(grid, column_index):
        column = []
        for row_index in range(grid.size()):
            val = grid.get_val(row_index, column_index)
            column.append(ValuedCoo(row_index, column_index, val))
        return column
    
    @classmethod
    def get_all_left_diagonals(cls, grid):
        left_diagonals = []
        for row_index in range(grid.size()):
            left_diagonals.append(cls.create_left_diagonal(grid, row_index, 0))
        for column_index in range(1, grid.size()):
            # starts at 1 because first row_index = 0 already checked column_index = 0 diagonal
            left_diagonals.append(cls.create_left_diagonal(grid, 0, column_index))
        return left_diagonals
    
    def create_left_diagonal(grid, starting_row_index, starting_column_index):
        if starting_row_index != 0 and starting_column_index != 0:
            raise ValueError("Either startin_row_index or starting_column_index has to be 0 but starting_row_index = " + str(starting_row_index) + ", starting_row_index = " + str(starting_column_index))
        row_index = starting_row_index
        column_index = starting_column_index
        left_diagonal = []
        
        grid_size = grid.size()
        while row_index < grid_size and column_index < grid_size:
            val = grid.get_val(row_index, column_index)
            left_diagonal.append(ValuedCoo(row_index, column_index, val))
            row_index += 1
            column_index += 1
        
        return left_diagonal
    
    @classmethod
    def get_all_right_diagonals(cls, grid):
        right_diagonals = []
        grid_size = grid.size()
        for row_index in range(grid_size):
            right_diagonals.append(cls.create_right_diagonal(grid, row_index, grid_size - 1))
        for column_index in range(0, grid_size - 1):
            # ends at grid_size - 1 because diagonal starting on last column was already checked
            right_diagonals.append(cls.create_right_diagonal(grid, 0, column_index))
        return right_diagonals
    
    def create_right_diagonal(grid, starting_row_index, starting_column_index):
        if starting_row_index != 0 and starting_column_index != grid.size() - 1:
            raise ValueError("Either startin_row_index has to be equal to zero or starting_column_index has to be grid.size() - 1 but starting_row_index = " + str(starting_row_index) + ", starting_row_index = " + str(starting_column_index)) 
        row_index = starting_row_index
        column_index = starting_column_index
        right_diagonal = []
        
        grid_size = grid.size()
        while row_index < grid_size and column_index >= 0:
            val = grid.get_val(row_index, column_index)
            right_diagonal.append(ValuedCoo(row_index, column_index, val))
            row_index += 1
            column_index -= 1
        
        return right_diagonal
    
    @classmethod
    def get_all_stripes(cls, grid):
        return cls.get_all_rows(grid) + cls.get_all_columns(grid) + cls.get_all_left_diagonals(grid) + cls.get_all_right_diagonals(grid)
    
    
    #----------------------------full streaks----------------------------
    
    @classmethod
    def get_full_streaks(cls, grid, length):
        pass