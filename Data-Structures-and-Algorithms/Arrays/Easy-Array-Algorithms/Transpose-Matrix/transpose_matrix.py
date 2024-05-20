def transposeMatrix(matrix):
    transposed = []

    for col in range(len(matrix[0])):
        new_row = []

        for row in range(len(matrix)):
            new_row.append(matrix[row][col])

        transposed.append(new_row)

    return transposed
