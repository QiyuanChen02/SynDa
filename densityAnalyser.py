from fetchPoints import fetchPoints
from findNeighbours import findNeighbours
from obtainSynapse import getSynapse, validateSynapses
from filterPoints import filterPoints
from interactiveVisualisation import interactiveVisualisation
from outputImage import createOutputImage
from generateGrids import generateGrids
from dimensions import getGridDimensions
from constants import GRIDSIZE, HOMER_SYNAPSE_PATH, SYT_SYNAPSE_PATH, INPUT_IMAGE_PATH

"""This is the densityAnalyser code, which extracts the coordinates from 2 csv files
to create a density map, as well as a scatter plot of the synapses, then generates an interactive image.

The basic idea behind the density map is to create a 2D array of zeros representing the density, and then for every synapse center, use the coordinates of the synapse to increase the value of the square in the 2D array where the synapse is located.
Finally the array is converted into an image, where the color of the square is determined by the value of the square in the array.
"""

preSynapseData = fetchPoints(HOMER_SYNAPSE_PATH)
postSynapseData = fetchPoints(SYT_SYNAPSE_PATH)
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
    INPUT_IMAGE_PATH,
    maxElementX - minElementX,
    maxElementY - minElementY,
    "red",
)
filteredPostSynapseData = filterPoints(
    postSynapseData,
    INPUT_IMAGE_PATH,
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

gridSynapses, gridDensity = generateGrids(
    validSynapses, GRIDSIZE, minX, minY, maxX, maxY
)

# Generate the images, overlays them and saves the image in the file densityImage.png the output directory
imageDensity, image = createOutputImage(gridDensity, gridSynapses, GRIDSIZE)

interactiveVisualisation(validSynapses, imageDensity)
