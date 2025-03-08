"""Using list comprehension, take a given matrix (a list of lists) of numbers and modify each element based on its row position.

Rules:

If an element is in the upper half of the matrix (the row index is between 0 and N/2, where N is the number of rows), multiply the element by 2.
If an element is in the lower half of the matrix (the row index is greater than or equal to N/2), multiply the element by 3.
Input:

The matrix elements are read from the keyboard.
First, the number of rows (N) and columns (M) are read as separate integers.
Then, each row of the matrix is read as a line of space-separated integers."""

def mult(e,i,n):
    if(i<n/2):
        return e*2
    else:
        return e*3


def multiply_matrix_by_2():

    n=int(input())
    m=int(input())
    matrix=[]

    for i in range(0,n):
        elementsRow=[int(elem) for elem in input().split(" ")]
        matrix.append(elementsRow)
   
    result =[[mult(matrix[i][j],i,n) for j in range(m)] for i in range(n) ]
    print(result)


if __name__ == "__main__":
    multiply_matrix_by_2()