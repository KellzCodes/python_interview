def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    smallest = float('inf')
    current = float('inf')
    smallestPair = []
    idxOne = 0
    idxTwo = 0

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]

    return smallestPair
