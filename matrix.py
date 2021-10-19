# [Matrix Class]
# Custom class to compute basic matrix arithmetic
# Developed by Mayfairr 

import math 

class Matrix: 
    def __init__(self, rows, cols):
        # Set the size of the matrix
        self.rows = rows
        self.cols = cols
        self.matrix = []

        #Initialise the matrix
        self._intializeSizeOfMatrix()

    def _intializeSizeOfMatrix(self, identity = 5):
        for rows in range(self.rows):
            self.matrix.append([identity] * self.cols)

    def index(self, row, col):
        return self.matrix[row][col]

    def setValueAtIndex(self, row, col, value):
        self.matrix[row][col] = value

    
    def multiply_with_scalar(self, scalar):
        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix[row][col] *= scalar
    
    def multiply_with_matrix(self, m):
        if type(m) != Matrix:
            print("Please provide matrix with correct type")
            return
        if self.cols != m.rows:
            print("Provided matrix cannot be multiplied due to inconsistent sizing")
            return
        buffer = Matrix(self.rows, m.cols)
        for row in range(buffer.rows):
            for col in range(buffer.cols):
                for col_m in range(m.cols):
                    value = 0
                    for row_m in range(m.rows):
                        value += m.index(row_m, col_m) * self.index(col_m, row_m)
                buffer.setValueAtIndex(row, col,value )
        return buffer;
    
a = Matrix(2,3)
b = Matrix(3,2)
print(a.multiply_with_matrix(b).matrix)

