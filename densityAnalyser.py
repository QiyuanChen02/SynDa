from fetchPoints import fetchPoints
from findNeighbours import findNeighbours
from obtainSynapse import getSynapse, validateSynapses
from filterPoints import filterPoints
from interactiveVisualisation import interactiveVisualisation
from outputImage import createOutputImage
from generateGrids import generateGrids
from dimensions import getGridDimensions
from thresholds import (
    gridsize,
    colourThreshold,
    distanceThreshold,
    prePostDistanceLowerThreshold,
    prePostDistanceUpperThreshold,
)

"""This is the densityAnalyser code, which extracts the coordinates from 2 csv files
to create a density map, as well as a scatter plot of the synapses, then generates an interactive image.

The basic idea behind the density map is to create a 2D array of zeros representing the density, and then for every synapse center, use the coordinates of the synapse to increase the value of the square in the 2D array where the synapse is located.
Finally the array is converted into an image, where the color of the square is determined by the value of the square in the array.
"""

preSynapseData = fetchPoints("input/Homer for Q 1.csv")
postSynapseData = fetchPoints("input/Syt for Q 2.csv")
(
    maxElementX,
    minElementX,
    maxElementY,
    minElementY,
    maxX,
    minX,
    maxY,
    minY,
) = getGridDimensions(gridsize, preSynapseData + postSynapseData)
filteredPreSynapseData = filterPoints(
    preSynapseData,
    "input/synapses.png",
    maxElementX - minElementX,
    maxElementY - minElementY,
    "red",
    colourThreshold,
    distanceThreshold,
)
filteredPostSynapseData = filterPoints(
    postSynapseData,
    "input/synapses.png",
    maxElementX - minElementX,
    maxElementY - minElementY,
    "green",
    colourThreshold,
    distanceThreshold,
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
    prePostDistanceLowerThreshold,
    prePostDistanceUpperThreshold,
)

gridSynapses, gridDensity = generateGrids(
    validSynapses, gridsize, minX, minY, maxX, maxY
)

# Generate the images, overlays them and saves the image in the file densityImage.png the output directory
imageDensity, imageSynapse, image = createOutputImage(
    gridDensity, gridSynapses, gridsize
)

interactiveVisualisation(validSynapses, imageDensity)
