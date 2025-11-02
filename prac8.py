#!/usr/bin/python3
a = [[1, 2, 1], [3, 2, 1], [4, 1, 3]]
b = [[1, 2, 3], [4, 5, 2], [1, 2, 1]]
def check_matrix(matrix):
    if isinstance(matrix, list):
        row_length = len(matrix[0]) if matrix else 0
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True
    return False
if check_matrix(a) and check_matrix(b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        c = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[i])):
                row.append(a[i][j] + b[i][j])
            c.append(row)

        print("Matrix c (a + b):")
        for row in c:
            print(row)
    else:
        print("Matrices have different dimensions, can't add them.")
else:
    print("One or both matrices are not valid.")


####subtraction of matrix
a=[[4,5,1],[3,6,7],[9,8,6]]
b=[[1,2,1],[2,5,3],[6,5,2]]

def check_matrix(matrix):
    if isinstance(matrix, list):
        row_length = len(matrix[0]) if matrix else 0
        for row in matrix:
            if not isinstance(row, list) or len(row) != row_length:
                return False
        return True
    return False
if check_matrix(a) and check_matrix(b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        c = []
        for i in range(len(a)):
            row = []
            for j in range(len(a[i])):
                row.append(a[i][j] - b[i][j])
            c.append(row)

        print("Matrix c (a - b):")
        for row in c:
            print(row)
    else:
        print("Matrices have different dimensions, can't add them.")
else:
    print("One or both matrices are not valid.")

	
##### multiplication of matrix

a=[[1,2],[2,1],[4,5]]
b=[[1,1,2],[2,3,1]]


if(len(a[0])!=len(b)):
	print("cannot multiply")
else:
	c=[]
	for i in range(len(a)):
		row=[]
		for j in range(len(b[0])):
			total=0
			for k in range(len(b)):
				total += a[i][k]*b[k][j]
			row.append(total)
		c.append(row)
	print("product of matrices:",c)
			
