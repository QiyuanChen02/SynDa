from fetchPoints import fetchPoints
from findNeighbours import findNeighbours
from obtainSynapse import validateSynapses, getSynapse
from PIL import Image
from filterPoints import filterPoints
from interactiveVisualisation import interactiveVisualisation
from outputExcel import outputExcel
from generateGrids import generateGrids
from dimensions import getGridDimensions
from constants import GRIDSIZE, HOMER_SYNAPSE_PATH, SYT_SYNAPSE_PATH, INPUT_IMAGE_PATH
from outputImage import createSynapseImage

preSynapseData = fetchPoints(HOMER_SYNAPSE_PATH)
postSynapseData = fetchPoints(SYT_SYNAPSE_PATH)
maxX, minX, maxY, minY, *_ = getGridDimensions(
    GRIDSIZE, preSynapseData + postSynapseData
)
filteredPreSynapseData = filterPoints(
    preSynapseData,
    INPUT_IMAGE_PATH,
    maxX - minX,
    maxY - minY,
    "red",
)
filteredPostSynapseData = filterPoints(
    postSynapseData,
    INPUT_IMAGE_PATH,
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
)

gridSynapses = generateGrids(
    validSynapses, GRIDSIZE, minX, minY, maxX, maxY, isSynapse=True
)

inputImage = Image.open(INPUT_IMAGE_PATH)

resizedImage = inputImage.resize((round(maxX - minX), round(maxY - minY)))
synapseImage = createSynapseImage(gridSynapses, resizedImage)

interactiveVisualisation(validSynapses, resizedImage)
