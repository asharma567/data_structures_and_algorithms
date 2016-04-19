def multiply_matrices(A, B):
    new = []
    empty_rows = A.shape[1] * None 
    new.append(B.shape[1] * empty_rows)
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            row = A[i][:]
            col = B[:][j]
            new_matrix[i][j] = get_dot_product(row, col)

def get_dot_product(row, col):
    #O(n)
    return [col[i] * element for i, element in enumerate(row)]



