from helpers.fetchPoints import fetchPoints
from helpers.findNeighbours import findNeighbours
from helpers.obtainSynapse import getSynapse, validateSynapses
from helpers.filterPoints import filterPoints
from helpers.interactiveVisualisation import interactiveVisualisation
from helpers.outputImage import createDensityImage
from helpers.generateGrids import generateGrids
from helpers.dimensions import getGridDimensions
from helpers.fetchPaths import fetchPaths
from helpers.constants import GRIDSIZE, INPUT_FOLDER_NAME


"""This is the densityAnalyser code, which extracts the coordinates from 2 csv files
to create a density map, as well as a scatter plot of the synapses, then generates an interactive image.

The basic idea behind the density map is to create a 2D array of zeros representing the density, and then for every synapse center, use the coordinates of the synapse to increase the value of the square in the 2D array where the synapse is located.
Finally the array is converted into an image, where the color of the square is determined by the value of the square in the array.
"""

def analyseImageDensity(folderName, visualise=True):

    (
        preSynapsePath,
        postSynapsePath,
        inputImagePath,
        densityImagePath,
        synapseImagePath,
        synapseDataPath,
    ) = fetchPaths(folderName)

    preSynapseData = fetchPoints(preSynapsePath)
    postSynapseData = fetchPoints(postSynapsePath)
    (
        maxElementX,
        minElementX,
        maxElementY,
        minElementY,
        maxX,
        minX,
        maxY,
        minY,
    ) = getGridDimensions(GRIDSIZE, preSynapseData + postSynapseData)
    filteredPreSynapseData = filterPoints(
        preSynapseData,
        inputImagePath,
        maxElementX - minElementX,
        maxElementY - minElementY,
        "red",
    )
    filteredPostSynapseData = filterPoints(
        postSynapseData,
        inputImagePath,
        maxElementX - minElementX,
        maxElementY - minElementY,
        "green",
    )

    closestNeighbours, closestNeighbourDistance = findNeighbours(
        filteredPreSynapseData, filteredPostSynapseData
    )

    synapses = getSynapse(
        filteredPreSynapseData,
        filteredPostSynapseData,
        closestNeighbours,
        closestNeighbourDistance,
    )

    isValidSynapse, validSynapses = validateSynapses(
        synapses,
        closestNeighbours,
        closestNeighbourDistance,
        filteredPreSynapseData,
        filteredPostSynapseData,
    )

    meanSynapseDensity = len(validSynapses) * (GRIDSIZE ** 2) / ((maxX - minX) * (maxY - minY))
    print(f"Mean synapse Density: {meanSynapseDensity}")

    gridSynapses, gridDensity = generateGrids(
        validSynapses, GRIDSIZE, minX, minY, maxX, maxY
    )

    # Generate the images, overlays them and saves the image in the file densityImage.png the output directory
    imageDensity, image = createDensityImage(gridDensity, gridSynapses, GRIDSIZE, densityImagePath)

    if visualise:
        interactiveVisualisation(validSynapses, imageDensity)

if __name__ == "__main__":
    fileName = input("Enter the name of the folder you wish to analyse: ")
    analyseImageDensity(fileName)
