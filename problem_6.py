sumOfSquares = sum((x**2 for x in range(0,101)))
squareOfSum = sum((x for x in range(0,101)))**2
print(squareOfSum - sumOfSquares)