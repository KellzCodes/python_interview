def spiralTraverse(array):
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1
    spiral = []

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            spiral.append(array[startRow][col])

        for row in range(startRow + 1, endRow + 1):
            spiral.append(array[row][endCol])

        for col in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            spiral.append(array[endRow][col])

        for row in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            spiral.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return spiral
