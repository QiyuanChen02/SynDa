from fetchPoints import fetchPoints
from findNeighbours import findNeighbours
from obtainSynapse import validateSynapses, getSynapse
from PIL import Image
from filterPoints import filterPoints
from interactiveVisualisation import interactiveVisualisation
from outputExcel import outputExcel
from generateGrids import generateGrids
from dimensions import getGridDimensions
from thresholds import (
    gridsize,
    colourThreshold,
    distanceThreshold,
    prePostDistanceLowerThreshold,
    prePostDistanceUpperThreshold,
)

preSynapseData = fetchPoints("input/Homer for Q 1.csv")
postSynapseData = fetchPoints("input/Syt for Q 2.csv")
maxX, minX, maxY, minY, *_ = getGridDimensions(
    gridsize, preSynapseData + postSynapseData
)
filteredPreSynapseData = filterPoints(
    preSynapseData,
    "input/synapses.png",
    maxX - minX,
    maxY - minY,
    "red",
    colourThreshold,
    distanceThreshold,
)
filteredPostSynapseData = filterPoints(
    postSynapseData,
    "input/synapses.png",
    maxX - minX,
    maxY - minY,
    "green",
    colourThreshold,
    distanceThreshold,
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
    prePostDistanceLowerThreshold,
    prePostDistanceUpperThreshold,
)

outputExcel(
    filteredPostSynapseData,
    closestNeighbours,
    closestNeighbourDistance,
    synapses,
    isValidSynapse,
)

gridSynapses = generateGrids(
    validSynapses, gridsize, minX, minY, maxX, maxY, isSynapse=True
)

inputImage = Image.open("input/synapses.png")
resizedImage = inputImage.resize((round(maxX - minX), round(maxY - minY)))

interactiveVisualisation(validSynapses, resizedImage)
