from PIL import Image

from helpers.fetchPoints import fetchPoints
from helpers.findNeighbours import findNeighbours
from helpers.obtainSynapse import validateSynapses, getSynapse
from helpers.filterPoints import filterPoints
from helpers.interactiveVisualisation import interactiveVisualisation
from helpers.outputExcel import outputExcel
from helpers.generateGrids import generateGrids
from helpers.dimensions import getGridDimensions
from helpers.constants import GRIDSIZE
from helpers.outputImage import createSynapseImage
from helpers.fetchPaths import fetchPaths

def analyseImageSynapse(folderName, visualise=True):
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
    maxX, minX, maxY, minY, *_ = getGridDimensions(
        GRIDSIZE, preSynapseData + postSynapseData
    )
    filteredPreSynapseData = filterPoints(
        preSynapseData,
        inputImagePath,
        maxX - minX,
        maxY - minY,
        "red",
    )
    filteredPostSynapseData = filterPoints(
        postSynapseData,
        inputImagePath,
        maxX - minX,
        maxY - minY,
        "green",
    )

    # Finds closest neighbours for all the post synapses
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

    outputExcel(
        filteredPostSynapseData,
        closestNeighbours,
        closestNeighbourDistance,
        synapses,
        isValidSynapse,
        synapseDataPath,
    )

    totalPoints = len(validSynapses)
    print(f"Total number of synapses: {totalPoints}")

    gridSynapses = generateGrids(
        validSynapses, GRIDSIZE, minX, minY, maxX, maxY, isSynapse=True
    )

    inputImage = Image.open(inputImagePath)

    resizedImage = inputImage.resize((round(maxX - minX), round(maxY - minY)))
    synapseImage = createSynapseImage(gridSynapses, resizedImage, synapseImagePath)

    if visualise:
        interactiveVisualisation(validSynapses, resizedImage)

if __name__ == "__main__":
    fileName = input("Enter the name of the folder you wish to analyse: ")
    analyseImageSynapse(fileName)