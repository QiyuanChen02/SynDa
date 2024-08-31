import math


# Creates a 2 dimensional array of 0s given by the length and width
def generateEmptyGrid(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")

    grid = [[0 for _ in range(width)] for _ in range(length)]
    return grid


def generateGrids(
    data,
    GRIDSIZE,
    minElementX,
    minElementY,
    maxElementX,
    maxElementY,
    isSynapse=False,
):
    width = maxElementX - minElementX
    height = maxElementY - minElementY
    gridDensity = generateEmptyGrid(int(height / GRIDSIZE), int(width / GRIDSIZE))
    gridSynapses = generateEmptyGrid(int(height), int(width))

    # Modifies the density and the points grid based on the coordinates in the data
    # The code takes the generated grid and adds 1 to the value of the density grid where the synapse is located.
    # For example, if the synapse is located in the top left square of the grid (which we can work out using the coordinates of the points), the value of that square will be increased by 1.
    # It also sets the value of the synapse grid to 1 where the synapse is located. This way, when the image is generated, the synapses will be visible.
    for coordinate in data:
        XCoordinate = float(coordinate[0])
        YCoordinate = float(coordinate[1])

        if not isSynapse:
            densityX = math.floor((XCoordinate - minElementX) / GRIDSIZE)
            densityY = math.floor((YCoordinate - minElementY) / GRIDSIZE)
            gridDensity[densityY][densityX] = gridDensity[densityY][densityX] + 1

        synapseX = math.floor((XCoordinate - minElementX))
        synapseY = math.floor((YCoordinate - minElementY))
        try:
            gridSynapses[synapseY][synapseX] = 1
        except IndexError:
            print("Synapse out of range...")

    if isSynapse:
        return gridSynapses
    else:
        return gridSynapses, gridDensity
