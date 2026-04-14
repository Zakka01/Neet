def reverseMatrix(matrix):
    for l in matrix:
        l.reverse()
    sorted_matrix = sorted(matrix, key=lambda m: m[0], reverse=True)
    print(sorted_matrix)



# Basic cases
reverseMatrix([[1, 2], [3, 4]])        
# [[4, 3], [2, 1]]

reverseMatrix([[1, 2, 3], [4, 5, 6]])  
# [[6, 5, 4], [3, 2, 1]]

# Single row
reverseMatrix([[1, 2, 3, 4]])          
# [[4, 3, 2, 1]]

# Single column
reverseMatrix([[1], [2], [3]])         
# [[3], [2], [1]]

# Edge cases
reverseMatrix([[1]])                   
# [[1]]

reverseMatrix([])                      
# []

# Larger matrix
reverseMatrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# [[9, 8, 7], [6, 5, 4], [3, 2, 1]]