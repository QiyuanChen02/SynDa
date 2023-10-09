import math


def floorArbitrary(number, multiple):
    return math.floor(number / multiple) * multiple


# This function takes the array of synapse data and returns the maximum and minimum values of the X or Y coordinates, depending on the type argument for creating the grid
# This useful for creating the grid of the density plot from the maximum and minimum values of the x and y coordinates of the synapses, by rounding them so we can have a whole number of squares.
def coordinateRange(pointsData, type):
    arrayIndex = 0 if type == "X" else 1

    # Initialize maxElement with the first element of the array
    maxElement = float(pointsData[0][arrayIndex])
    minElement = float(pointsData[0][arrayIndex])

    # Iterate through the array to find the maximum element
    for num in pointsData:
        if float(num[arrayIndex]) > maxElement:
            maxElement = float(num[arrayIndex])
        if float(num[arrayIndex]) < minElement:
            minElement = float(num[arrayIndex])

    return (maxElement, minElement)


def getGridDimensions(gridsize, data):
    # Read the excel file to get the data and maximum and minimum values of the x and y coordinates
    maxElementX, minElementX = coordinateRange(data, "X")
    maxElementY, minElementY = coordinateRange(data, "Y")

    # Alter Max + Min to multiples of gridsize (to have a whole number of squares)
    maxX = floorArbitrary(maxElementX, gridsize) + gridsize
    minX = floorArbitrary(minElementX, gridsize)
    maxY = floorArbitrary(maxElementY, gridsize) + gridsize
    minY = floorArbitrary(minElementY, gridsize)

    return (
        maxElementX,
        minElementX,
        maxElementY,
        minElementY,
        maxX,
        minX,
        maxY,
        minY,
    )
