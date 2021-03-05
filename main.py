from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix1 = new_matrix()

#test print_matrix
print("test print_matrix [1,2,3,1], [4,5,6,1], [7,8,9,1], [10,11,12,1]")
matrix1 = [[1,2,3,1], [4,5,6,1], [7,8,9,1], [10,11,12,1]]
print_matrix(matrix1)
print()

#test ident
print("test ident")
matrix2 = new_matrix()
matrix2 = [[0,0,0,1],[0,0,0,1],[0,0,0,1], [0,0,0,1]]
ident(matrix2)
print_matrix(matrix2)
print()

#test matrix mult
print("test matrix_mult ident by first")
matrix_mult(matrix2,matrix1)
print_matrix(matrix1)
print()

#test draw_lines
m = [[0,0,0,1],[500,500,0,1], [0,500,0,1],[500,0,0,1]]
draw_lines(m, screen, color)

#test add_edge
print("test add_edge [13,14,15,1][16,17,18,1] to first matrix")
add_edge(matrix1, 13, 14, 15, 16, 17, 18)
print_matrix(matrix1)
print()

#test add_point
print("test add_point [19,20,0,1] to first matrix")
add_point(matrix1, 19, 20)
print_matrix(matrix1)
print()
        

display(screen)

