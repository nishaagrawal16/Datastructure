matrix = [[1,2], [3,4], [5,6]]

trans_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(trans_matrix)