from PIL import Image
import math
from constants import (
    POINTS_COLOUR,
    DENSITY_COLOUR,
    DENSITY_IMAGE_OUTPUT_PATH,
)


def getColourMap(gridDensity):
    # Define a color map for the synapses
    colorMapSynapses = [
        (0, 0, 0),
        POINTS_COLOUR,
    ]

    # Define a color map for the density grid.
    # Note that the maximum number of synapses in a square is used to determine the color of the squares, by dividing the number of synapses in a square by the maximum number of synapses and then converting it into an RGB tuple
    maximumGridValue = max(map(max, gridDensity))
    r, g, b = DENSITY_COLOUR
    colorMapDensity = [
        (
            math.floor(r * (i / maximumGridValue)),
            math.floor(g * (i / maximumGridValue)),
            math.floor(b * (i / maximumGridValue)),
        )
        for i in range(maximumGridValue + 1)
    ]
    return colorMapSynapses, colorMapDensity


def gridToImage(array, colorMap, scalingFactor, currentImage=None):
    # Determine the dimensions of the array
    height = len(array)
    width = len(array[0])

    # Scale up the dimensions (e.g scalingFactor 10 means 10x10 blocks for each array element)
    scaledHeight = height * scalingFactor
    scaledWidth = width * scalingFactor

    image = (
        currentImage
        if currentImage is not None
        else Image.new("RGB", (scaledWidth, scaledHeight))
    )

    for y in range(height):
        for x in range(width):
            value = array[y][x]
            color = colorMap[value]
            if color != (0, 0, 0):
                blockX = x * scalingFactor
                blockY = y * scalingFactor

                # Secondary loop to set the pixels of the block, with the scaling factor being the size of the block
                for i in range(scalingFactor):
                    for j in range(scalingFactor):
                        if blockX + i < image.width and blockY + j < image.height:
                            image.putpixel((blockX + i, blockY + j), color)

    return image


# This function overlays two images on top of each other, using the blend function of the PIL library.
def overlayImages(image1, image2, alpha=0.5):
    if image1.size != image2.size:
        raise ValueError("Both images must have the same dimensions.")

    # Create a new blank image with the same dimensions as the input images
    overlayedImage = Image.new("RGBA", image1.size)

    # Blend the two images together
    overlayedImage = Image.blend(image1.convert("RGBA"), image2.convert("RGBA"), alpha)
    return overlayedImage


def createOutputImage(gridDensity, gridSynapses, scalingFactor):
    colorMapSynapses, colorMapDensity = getColourMap(gridDensity)
    imageDensity = gridToImage(gridDensity, colorMapDensity, scalingFactor)
    combinedImage = gridToImage(
        gridSynapses, colorMapSynapses, 2, currentImage=imageDensity.copy()
    )
    combinedImage.save(DENSITY_IMAGE_OUTPUT_PATH)
    return imageDensity, combinedImage
