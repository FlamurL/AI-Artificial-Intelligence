"""
Using list comprehension, modify a given matrix consisting of numbers so that each element is multiplied by 2.

Each element of the matrix is read from the keyboard in such a way that:

N (number of rows) and M (number of columns) are read first.
Then, in each row, the elements are read separated by a space.
"""

def multiply_matrix_by_2():

    n=int(input())
    m=int(input())
    matrix=[]

    for i in range(0,n):
        elementsRow=[int(elem) for elem in input().split(" ")]
        matrix.append(elementsRow)
   
    result1 = [elem*2 for row in matrix for elem in row ]
    print(result1)

    result2 =[[elem*2 for elem in row] for row in matrix]
    print(result2)



if __name__ == "__main__":
    multiply_matrix_by_2()