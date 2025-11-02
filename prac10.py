#!/usr/bin/python3

list=[[3,1,5],[4,0,2]]
newlist=[]
for row in list:
	for item in row:
		newlist.append(item)
		
print(list)
newlist.sort()
print(newlist)


m=[[3,1,5],[4,0,2]]

num_rows=len(m[0])
num_cols=len(m)
new_matrix=[]
for i in range(0,num_rows):
	new_row=[]
	for j in range(0,num_cols):
		new_row.append(m[j][i])
	new_matrix.append(new_row)
print(new_matrix)

m=[3,1,5,4,0,2]
def sumlist(m):
	return sumlistItem(m,len(m)-1)
def sumlistItem(list,index):
	if index<0:
		return 0
	return list[index]+sumlistItem(list,index-1)
print(sumlist(m))
#################################################################################
import numpy as np

lst = [[3, 1, 5], [4, 0, 2]]
arr = np.array(lst)

# Flatten and sort using NumPy
newlist = np.sort(arr.flatten())

print(lst)
print(newlist)

import numpy as np
m = [[3, 1, 5], [4, 0, 2]]
arr = np.array(m)
# Transpose the matrix
new_matrix = arr.T
print(new_matrix)

import numpy as np
m = [3, 1, 5, 4, 0, 2]
arr = np.array(m)
# Use NumPy's sum function
total = np.sum(arr)
print(total)

