"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(4):
        line = ''
        for j in range(len(matrix)):
            line += str(matrix[j][i]) + "  "
        print(line)
        

    
#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    x = 0
    for i in range(4):
        for j in range(4):
            if j == x:
                matrix[j][i] = 1
            else:
                matrix[j][i] = 0
        x += 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = new_matrix()
    #rows
    for i in range(4):
        #columns
        for j in range(len(m2)):
            for k in range(4):
                temp[j][i] += m1[i][k] * m2[k][j]
    m2 = temp
                


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
