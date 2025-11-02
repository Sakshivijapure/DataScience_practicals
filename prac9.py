#!/usr/bin/python3
#check for sparse matrix
a=[[1,0,0,1,0],[0,1,0,0,0],[0,0,0,0,0],[1,0,1,0,0],[1,1,0,1,0]]

def check_matrix(matrix):
    if isinstance(matrix, list):
        row_length = len(matrix[0]) if matrix else 0
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True
    return False
if (check_matrix(a)):
	def check_sparse(matrix):
		count=0
		zero=0
		for row in matrix:
			for value in row:
				count=count+1
				if value==0:
					zero+=1
		return zero>count/2
print("matrix",a)
print(check_sparse(a))	

#################################################
#use numpy to check for sparse
import numpy as np
a = [[1, 0, 0, 1, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0],
     [1, 1, 0, 1, 0]]

# Convert to NumPy array
arr = np.array(a)

# Check if matrix is rectangular (optional if you trust input)
def check_matrix(matrix):
    return matrix.ndim == 2 and all(len(row) == matrix.shape[1] for row in matrix)

# Check for sparsity
def check_sparse_numpy(matrix):
    total_elements = matrix.size
    zero_elements = np.count_nonzero(matrix == 0)
    return zero_elements > total_elements / 2

# Apply checks
if check_matrix(arr):
    print("matrix:\n", arr)
    print("Is sparse:", check_sparse_numpy(arr))
####################################################
# to plot a table of row,column and value
a = [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0]
]

def check_matrix(matrix):
    if isinstance(matrix, list):
        row_length = len(matrix[0]) if matrix else 0
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True
    return False

def check_sparse(matrix):
    count = 0
    zero = 0
    for row in matrix:
        for value in row:
            count += 1
            if value == 0:
                zero += 1
    return zero > count / 2

def analyze_matrix(matrix):
    ones_count = 0
    nonzero_elements = []
    
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value != 0:
                nonzero_elements.append([i, j, value])
            if value == 1:
                ones_count += 1

    return ones_count, nonzero_elements

if check_matrix(a):
    print("Matrix:", a)
    print("Is sparse?", check_sparse(a))
    
    ones, nonzero_list = analyze_matrix(a)
    print("Number of ones:", ones)
    
    print("Row\tColumn\tValue")
    for elem in nonzero_list:
        print(f"{elem[0]}\t{elem[1]}\t{elem[2]}")
else:
    print("Invalid matrix")
 #################################################################################
 # to use numpy to do that
import numpy as np

a = [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 1, 0]
]

# Convert list to NumPy array
arr = np.array(a)
def check_matrix_np(matrix):
    return matrix.ndim == 2

def check_sparse_np(matrix):
    zero_count = np.count_nonzero(matrix == 0)
    total = matrix.size
    return zero_count > total / 2

def analyze_matrix_np(matrix):
    ones_count = np.count_nonzero(matrix == 1)
    
    nonzero_indices = np.argwhere(matrix != 0)
    nonzero_values = matrix[matrix != 0]
    
    nonzero_elements = np.hstack((nonzero_indices, nonzero_values.reshape(-1, 1)))
    
    return ones_count, nonzero_elements

if check_matrix_np(arr):
    print("Matrix:\n", arr)
    print("Is sparse?", check_sparse_np(arr))
    
    ones, nonzero_list = analyze_matrix_np(arr)
    print("Number of ones:", ones)
    
    print("Row\tColumn\tValue")
    for row, col, val in nonzero_list:
        print(f"{row}\t{col}\t{val}")
else:
    print("Invalid matrix")
############################################################################################
#check if matrix is square and symmetric
a = [
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]

def check_matrix(matrix):
    if isinstance(matrix, list):
        row_length = len(matrix[0]) if matrix else 0
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True
    return False

def is_square_matrix(matrix):
    return len(matrix) == len(matrix[0])

def is_symmetric_matrix(matrix):
    if not is_square_matrix(matrix):
        return False
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

if check_matrix(a):
    print("Matrix is valid.")
    print("Matrix:")
    for row in a:
        print(row)
    
    if is_square_matrix(a):
        print("This is a square matrix.")
    else:
        print("This is NOT a square matrix.")
    
    if is_symmetric_matrix(a):
        print("This is a symmetric matrix.")
    else:
        print("This is NOT a symmetric matrix.")
else:
    print("Invalid matrix.")
########################################
# to check if square and symmetric using numpy
import numpy as np

a = [
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0]
]
arr = np.array(a)
def check_matrix_np(matrix):
    return matrix.ndim == 2
def is_square_matrix_np(matrix):
    return matrix.shape[0] == matrix.shape[1]
def is_symmetric_matrix_np(matrix):
    if not is_square_matrix_np(matrix):
        return False
    return np.array_equal(matrix, matrix.T)
if check_matrix_np(arr):
    print("Matrix is valid.")
    print("Matrix:\n", arr)

    if is_square_matrix_np(arr):
        print("This is a square matrix.")
    else:
        print("This is NOT a square matrix.")

    if is_symmetric_matrix_np(arr):
        print("This is a symmetric matrix.")
    else:
        print("This is NOT a symmetric matrix.")
else:
    print("Invalid matrix.")
########################################
# to check if matrix is horizontally symmetric
b = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
def check_matrix(matrix):
    if isinstance(matrix, list):
        row_length = len(matrix[0]) if matrix else 0
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True
    return False
def is_horiz_matrix(matrix):
    size = len(matrix)
    for i in range(size // 2):
        if matrix[i] != matrix[size - 1 - i]:
            return False
    return True
if check_matrix(b):
    if is_horiz_matrix(b):
        print("This is a horizontally symmetric matrix.")
    else:
        print("This is NOT a horizontally symmetric matrix.")
else:
    print("Invalid matrix.")
##########################################
# to check if matrix is horizontally symmetric using numpy
import numpy as np

b = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]
arr = np.array(b)
def check_matrix_np(matrix):
    return matrix.ndim == 2
def is_horiz_symmetric_np(matrix):
    return np.array_equal(matrix, np.flipud(matrix))
if check_matrix_np(arr):
    if is_horiz_symmetric_np(arr):
        print("This is a horizontally symmetric matrix.")
    else:
        print("This is NOT a horizontally symmetric matrix.")
else:
    print("Invalid matrix.")
#############################################
# to check if matrix is vertically symmetric
b = [
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1]
]

def check_matrix(matrix):
    if isinstance(matrix, list):
        row_length = len(matrix[0]) if matrix else 0
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True
    return False
def is_vert_matrix(matrix):
    size = len(matrix)
    for j in range(size // 2):
        if matrix[j] != matrix[size - 1 - j]:
            return False
    return True
if check_matrix(b):
    if is_vert_matrix(b):
        print("This is a vertically symmetric matrix.")
    else:
        print("This is NOT a vertically symmetric matrix.")
else:
    print("Invalid matrix.")
#######################################
#to check if matrix is vertically symmmetric using numpy
import numpy as np
b = [
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1]
]
arr = np.array(b)
def check_matrix_np(matrix):
    return matrix.ndim == 2
def is_vert_symmetric_np(matrix):
    return np.array_equal(matrix, np.fliplr(matrix))
if check_matrix_np(arr):
    if is_vert_symmetric_np(arr):
        print("This is a vertically symmetric matrix.")
    else:
        print("This is NOT a vertically symmetric matrix.")
else:
    print("Invalid matrix.")

